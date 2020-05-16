import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost is not None:
        return True

def check_connectivity():
    request = requests.get("http://www.ifcode.ru")
    #print(type(request))
    if request.status_code == 200:
        return True

#g = check_localhost()
#print(g)

#v = check_connectivity()
#print(v)

