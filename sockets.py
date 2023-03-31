#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013-2023 Abram Hindle, Elena Xu
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import flask
from flask import Flask, request
from flask_sockets import Sockets
import gevent
from gevent import queue
import time
import json
import os

app = Flask(__name__)
sockets = Sockets(app)
app.debug = True

class World:
    def __init__(self):
        self.clear()
        # we've got listeners now!
        self.listeners = list() # list of listener functions
        
    def add_set_listener(self, listener):
        self.listeners.append( listener ) 

    def update(self, entity, key, value):
        entry = self.space.get(entity,dict())
        entry[key] = value
        self.space[entity] = entry
        self.update_listeners( entity )

    def set(self, entity, data):
        self.space[entity] = data
        self.update_listeners( entity )

    def update_listeners(self, entity):
        '''update the set listeners'''
        for listener in self.listeners:
            listener(entity, self.get(entity))

    def clear(self):
        self.space = dict()

    def get(self, entity):
        return self.space.get(entity,dict())
    
    def world(self):
        return self.space

myWorld = World()        

def set_listener( entity, data ):
    ''' do something with the update ! '''
    myWorld.set(entity, data) 

myWorld.add_set_listener( set_listener )

clients = list() # list of clients interacting with the canvas

# Reference: https://github.com/uofa-cmput404/cmput404-slides/blob/master/examples/WebSocketsExamples/broadcaster.py
# Combined the two functions send_all() and send_all_json()
def update_for_clients(obj):
    world_obj = json.dumps(obj) # turn object into a string
    for client in clients:
        client.put(world_obj)

class Client:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, v):
        self.queue.put_nowait(v) # put(item, block=False)

    def get(self):
        return self.queue.get()
        
@app.route('/')
def hello():
    '''Return something coherent here.. perhaps redirect to /static/index.html '''
    return flask.redirect("/static/index.html")

def read_ws(ws,client):
    '''A greenlet function that reads from the websocket and updates the world'''
    # XXX: TODO IMPLEMENT ME
    # Reference: https://github.com/uofa-cmput404/cmput404-slides/blob/master/examples/WebSocketsExamples/broadcaster.py
    try:
        while True:
            current_world = ws.receive() # read from the websocket what the current world looks like now
            if (current_world is not None): # there has been changes made to the world
                world_data = json.loads(current_world) # turn string into dict
                update_for_clients(world_data)
            else:
                break
    except:
        '''Done'''

@sockets.route('/subscribe')
def subscribe_socket(ws):
    '''Fufill the websocket URL of /subscribe, every update notify the
       websocket and read updates from the websocket '''
    # XXX: TODO IMPLEMENT ME
    # Reference: https://github.com/uofa-cmput404/cmput404-slides/blob/master/examples/WebSocketsExamples/broadcaster.py
    
    # for each client that is interacting with the canvas
    client = Client()
    clients.append(client)
    greenlet = gevent.spawn( read_ws, ws, client)  # run the greenlet function with the arguments passed in 

    try:
        while True:
            current_world = client.get() # the current state of the world
            ws.send(current_world)
    except Exception as e:
        print("WS Error %s" % e)
    finally:
        clients.remove(client)
        gevent.kill(greenlet)

# I give this to you, this is how you get the raw body/data portion of a post in flask
# this should come with flask but whatever, it's not my project.
def flask_post_json():
    '''Ah the joys of frameworks! They do so much work for you
       that they get in the way of sane operation!'''
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data.decode("utf8") != u''):
        return json.loads(request.data.decode("utf8"))
    else:
        return json.loads(request.form.keys()[0])

@app.route("/entity/<entity>", methods=['POST','PUT'])
def update(entity):
    '''update the entities via this interface'''
    if request.method == 'POST':
        json_data = flask_post_json()
        myWorld.set(entity, json_data) # set the data for that entity
        get_entity = myWorld.get(entity) # get that entity to be returned later
        return json.dumps(get_entity)

    if request.method == 'PUT':
        json_data = flask_post_json()

        x_value = json_data.get('x')
        y_value=  json_data.get('y')
        colour_value = json_data.get('colour')
        radius_value = json_data.get('radius')

        # check if x,y,colour, and radius exists
        if x_value is not None:
            myWorld.update(entity, 'x', x_value)
        if y_value is not None:
            myWorld.update(entity, 'y', y_value)
        if colour_value is not None: 
            myWorld.update(entity, 'colour', colour_value)
        if radius_value is not None:
            myWorld.update(entity, 'radius', radius_value)

        get_entity = myWorld.get(entity)
        return json.dumps(get_entity)

@app.route("/world", methods=['POST','GET'])    
def world():
    '''you should probably return the world here'''
    if request.method == 'GET' or request.method == 'POST':
        return myWorld.world()
    

@app.route("/entity/<entity>")    
def get_entity(entity):
    '''This is the GET version of the entity interface, return a representation of the entity'''
    return myWorld.get(entity)


@app.route("/clear", methods=['POST','GET'])
def clear():
    '''Clear the world out!'''
    if request.method == 'GET' or request.method == 'POST':
        myWorld.clear()
        return "Successfully cleared the world out!", 200



if __name__ == "__main__":
    ''' This doesn't work well anymore:
        pip install gunicorn
        and run
        gunicorn -k flask_sockets.worker sockets:app
    '''
    app.run()
