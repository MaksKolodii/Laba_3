import socket
import threading
import time

from crypt_caesar import my_decode, my_encode

key = 8194

shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                decrypt = data.decode("utf-8")
                if not ("чату" in decrypt):
                    decrypt = my_decode(decrypt)
                print(decrypt)

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.2.109", 4050)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("[" + alias + "] => Приєднався до чату ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
            message = my_encode(message)
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= Залишив чат ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
