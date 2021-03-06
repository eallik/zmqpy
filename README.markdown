zmqpy - (cffi) zeromq python bindings
=====================================

**This code is a work in progress**

The goal of this project is to provide a CPython/PyPy compatible ZeroMQ bindings
for the Python language.

It uses cffi (http://cffi.readthedocs.org) as integration mechanism with the
original code.

API Example
-----------

It looks like Pyzmq.

```python

import zmqpy

context = zmqpy.Context()

socket = context.socket(zmqpy.PUSH)
socket.bind('tcp://127.0.0.1:5555')

socket.send('message', zmqpy.NOBLOCK)

socket.close()
context.term()

```

Benchmarks
----------

This (naive) benchmark compares PyPy + zmqpy Vs Cpython + PyZMQ

It sends *10000000* 10 bytes message == "aaaaaaaaaa".

PyPy(*Trunk*) with Cffi

```sh
(pypy19)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  12.29s user 7.17s system 182% cpu 10.672 total
(pypy19)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  12.63s user 7.38s system 182% cpu 10.945 total
(pypy19)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  12.29s user 7.18s system 183% cpu 10.617 total
```

Python 2.7 + PyZMQ

```sh
(py27)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  25.86s user 18.67s system 191% cpu 23.279 total
(py27)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  25.93s user 18.57s system 190% cpu 23.386 total
(py27)felipecruz:benchmarks/ (master*) $ time python sender.py
python sender.py  26.79s user 19.24s system 190% cpu 24.109 total
```

Tests
-----

First time:

`pip install -r requirements.txt`

To actually run the tests:

`make test`

Coverage Report
---------------

First time:

`pip install -r requirements.txt`

And then:

`make coverage`
