# Python2 test to grab banners for testing reachability

import optparse
import socket
from socket import *


def conn(host, port):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((host, port))
        results = connSkt.recv(100)
        print('[+]%d/tcp open'% port)
        connSkt.close()
    except:
        print('[-]%d/tcp closed'% port)

def port(host, ports):
    try:
        ip = gethostbyname(host)
    except:
        print("[-] No DNS resolution '%s': unknown host:" %host)
        return
