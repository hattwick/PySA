
# Python3 query AWS Route 53 response
# this sample just uses public hosts for tests



import socket

r53 = ['microsoft.com','bloomberg.com', 'amazon.com']



for host in r53:

    host = host.strip()

    ip = socket.gethostbyname(host)

    print(host, ip)




