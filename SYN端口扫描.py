from scapy.all import *

def main():
    a = input('Destination IP:')
    # retry=3,
    c,b= sr(IP(dst=a) / TCP(sport=45415,dport=(int(1),int(20000)) ,flags='S'),timeout=30,verbose=False)
    c.summary()
    print('-'*50)
    #b.summary()
if __name__ == '__main__':
    main()