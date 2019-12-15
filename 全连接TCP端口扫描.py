import socket

def main():
    # 用户输入
    ss = input('ip：')
    aa = int(input('port：'))
    i = 1
    print('目标IP: %s'% ss)
    while i <= aa:
        port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print(ss,i)
        try:
            port.connect((ss, i))

            print('\t端口：%d' % i + '  open')
            i += 1
            port.close()
        except Exception as e:
            i += 1
    print('\t共扫描%d个port' % aa)
if __name__ == '__main__':
    main()
