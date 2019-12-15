import threading
import socket
import gevent
from queue import Queue
from gevent import monkey
from gevent import pool
monkey.patch_all()

q = Queue(65535)

def run1(flie,int,in_t):

    for i in range(int,in_t):
        try:
            s = sock()
            int_ = s.connect_ex((flie,i)) 
            s.settimeout(1)
            if int_ == 0:
                print('[*]port：%d open' % i)
            else:
                pass
            s.close()
        except Exception as e:
            print('[-]:结束 ',e)
            continue

def sing(a):
    print('[*]正在启动线程')
    print('[*]正在快速扫描')
    gevent.joinall([
        gevent.spawn(run1, a, 1, 32767),
        gevent.spawn(run1, a, 32767, 65535)
    ])

def main():
    a = input('请输入你的ip：')
    esing = threading.Thread(target=sing,args=(a,))
    esing.start()
    esing.join()

def sock():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    main()