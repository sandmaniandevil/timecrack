#!/usr/bin/python

import socket
import time

HOST = raw_input("Enter the target IP:  ")
PORT = int(raw_input("Enter the target port:  "))

s = socket.socket()
