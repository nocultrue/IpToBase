# python3
# coding:utf-8
# author:noculture time:2022/8/2
import sys



def iptoBase(ip):
    # ip地址转换为10进制
    ipnum = ip.split(".")
    tenIp = 0
    for i in range(4):
        tenIp += int(ipnum[i]) * 256 ** (3 - i)
    print("{0}{1}".format(ip, "转换为8进制结果："))
    print(tenIp)
    #ip地址转换为8进制
    octalIP='.'.join(["%04o" % int(x) for x in ip.split('.')])
    print("{0}{1}".format(ip, "转换为10进制结果："))
    print(octalIP)
    # ip地址转换为16进制
    hexadecimalIp = '.'.join(["%02X" % int(x) for x in ip.split('.')])
    print("{0}{1}".format(ip, "转换为16进制结果："))
    print("{0}{1}".format("0x",hexadecimalIp))
def help():
    print ('Usage:python3 IpToBase.py 127.0.0.1')

def main():

    try:
        if (sys.argv[1] is not None):
            iptoBase(sys.argv[1])
    except :

            help()
if __name__ == '__main__':
    main()

