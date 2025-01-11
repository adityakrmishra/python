import socket
import re
import sys
def connect(username,password):
    sample = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    