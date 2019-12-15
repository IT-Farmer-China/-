import gevent
import socket
import time
from gevent import monkey
from gevent import pool
monkey.patch_all()

def run(i,flie):
    try:
        time.sleep(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        int_ = s.connect_ex((flie,i))
        if int_ == 0:
            print('[*]port：%d open' % i)
        else:
            pass
        s.close()
    except Exception as e:
        print('[-]错误: ',e)

def main():
    gevent.pool.Pool(5)
    list = []
    flie = input('请输入目标IP：')
    for i in range(1,65535):
        list.append(gevent.spawn(run,i,flie))
    print('[*]正在启动线程')
    print('[*]正在快速扫描')
    gevent.joinall(list)

if __name__ == '__main__':
    main()