# coding: utf-8

from cffi import FFI

from constants import *
from error import *

ffi = FFI()

ffi.cdef('''

typedef struct {
    void *content;
    unsigned char flags;
    unsigned char vsm_size;
    unsigned char vsm_data [30];
} zmq_msg_t;

void* zmq_init(int);
void* zmq_socket(void *context, int type);
int zmq_bind(void *socket, const char *endpoint);
int zmq_connect(void *socket, const char *endpoint);
int zmq_send(void *socket, zmq_msg_t *msg, int flags);
int zmq_recv(void *socket, zmq_msg_t *msg, int flags);
typedef ... zmq_free_fn;

int zmq_msg_init(zmq_msg_t *msg);
int zmq_msg_init_size(zmq_msg_t *msg, size_t size);
int zmq_msg_init_data(zmq_msg_t *msg,
                      void *data,
                      size_t size,
                      zmq_free_fn *ffn,
                      void *hint);
size_t zmq_msg_size(zmq_msg_t *msg);
void *zmq_msg_data(zmq_msg_t *msg);
''')

C = ffi.verify('''
    #include <zmq.h>
''')