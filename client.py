#coding-utf-8
import socket
import msgpack

def rodar_rotinas():

    host='localhost'

    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=(host, 9898)
    mysock.connect(addr)

    try:
        # msg=b"ola\n"
        msg = execution()
        mysock.sendall(msg)
    except socket.errno as e:
        print("Socket error ", e)
    finally:
        while True:
            msg = mysock.recv(1024)
            if not msg:
                break
            fallback(msgpack.unpackb(msg))
        mysock.close()


def execution():
    return msgpack.packb(['execute_test()', 'send_sms()', 'send_email()'])
    # fallback('ok')

def fallback(fallback):
    print(fallback)


rodar_rotinas()
