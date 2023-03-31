CMPUT404-assignment-websockets
==============================

CMPUT404-assignment-websockets

See requirements.org (plain-text) for a description of the project.

Make a shared state Websockets drawing program

Prereqs
=======
Create a virtual environment and install the required dependencies.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

Contributors / Licensing
========================

Generally everything is LICENSE'D under the Apache 2 license by Abram Hindle.

freetests.py is LICENSE'D under a BSD-like license:

From ws4py

Copyright (c) 2011-2023, Sylvain Hellegouarch, Abram Hindle, Elena Xu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
 * Neither the name of ws4py nor the names of its contributors may be used
   to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Contributors
============

* Mark Galloway
* Abram Hindle
* Cole Mackenzie

* Modications have been made by me on index.html and sockets.py
  * A majority of sockets.py is based off of broadcaster.py (see references below), and some parts were from my Assignment 4
  * A majority of index.html is based off broadcast.html (see references below), and some parts were form my Assignment 4

External Sources / References (some from Assignment 4)
========================
* https://www.w3schools.com/css/css3_buttons.asp (for creating hoverable buttons)
  * Author: W3Schools
  * Copyright 1999-2023 by Refsnes Data. All Rights Reserved.
  
* https://www.w3schools.com/howto/howto_js_active_element.asp (for adding an active class to the current element)
  * Author: W3Schools
  * Copyright 1999-2023 by Refsnes Data. All Rights Reserved.
 
* https://www.educative.io/answers/how-to-return-the-status-code-in-flask
  * For understanding how to return status codes in Flask
  * Contributor: Abhilash
  * Link to contributor: https://www.educative.io/profile/view/5104289219608576
  * Copyright ©2023 Educative, Inc. All rights reserved
  
* https://github.com/uofa-cmput404/cmput404-slides/tree/master/examples/WebSocketsExamples
  * To see examples of websockets being used 
  * The following are licensed under the Apache license, Copyright 2013-2023 Abram Hindle:
    * broadcaster.py 
    * chat.py
    * exercise.py
    * braodcast.html
    * chat.html
    * exercise.html
    * exercise2.html

Additional References Used
========================
* https://sdiehl.github.io/gevent-tutorial/
  * To get a better understanding of gevent
* https://docs.python.org/3/library/queue.html#
  * To get a better understanding of some of the methods used (e.g. put_nowait)
