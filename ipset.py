__author__ = 'zhangzhm'
# coding: utf-8

import os
import time
import traceback
import setdns
import time
import sys

def HKDetentionHouse():
    fo = open("ip.ini", "r+")
    cmdline1 = fo.readline()
    cmdline2 = fo.readline()
    #print('cmdline1=',cmdline1)
    #os.system('netsh interface ip set address "wireless" static 192.168.2.99  255.255.255.0 192.168.2.1')
    os.system(cmdline1)
    #os.system('netsh interface ipv4 add address name="wireless" addr=10.2.3.4 mask=255.255.255.0')
    #print('cmdline2=',cmdline2)
    os.system(cmdline2)
    time.sleep(5)
    os.system('route add 10.0.0.0 mask 255.0.0.0 10.2.3.1')
    setdns.DnsDef()
    fo.close()

def wirelessdhcp():  
    os.system('netsh interface ip set address "wireless" dhcp')
    setdns.DnsDef()

def lanstatic():
    os.system('netsh interface ip set address "lan" static 10.0.0.99 255.255.255.0 10.0.0.1')
    os.system('netsh interface ip set dns "lan" static 180.76.76.76')
    time.sleep(5)
    os.system('netsh interface ip add dnsservers name="lan" address=119.29.29.29 index=2')

def wirelessstatic():
    os.system('netsh interface ip set address "wireless" static 10.0.0.99 255.255.255.0 10.0.0.1')
    print('set ip finished')
    os.system('netsh interface ip set dns "wireless" static 180.76.76.76')
    time.sleep(5)
    os.system('netsh interface ip add dnsservers name="wireless" address=119.29.29.29 index=2')
    print('set dns 2 finished')

def landisabled():
    os.system(' netsh interface set interface "lan" disabled ')

def wirelessdisabled():
    os.system(' netsh interface set interface "wireless" disabled ')

def lanenabled():
    os.system(' netsh interface set interface "lan" enabled ')

def wirelessenabled():
    os.system(' netsh interface set interface "wireless" enabled ')

def PingIP():
    ip = input("input IP:  ")
    cmd = 'ping ' + ip 
    os.system(cmd)


def showIP():
    os.system('ipconfig /all')
    os.system("pause")
def routeprint():
    os.system("route print")
    os.system("pause")

def setip():
    print("=========================")
    print("\n1. hongkou \n")
    print("2. wireless DHCP\n")
    print("3. lan static  --  4. wireless static\n")
    print("5. disable lan |  6. disable wireless | 7. enable lan | 8. enable wiereless\n")
    print("9. test ip ping | 10. show IP | 11. show route | 12 renew DHCP\n")
    print("=========================")

    x = input("input number:")
    print("=========================")

    if x == '1':
        HKDetentionHouse()
    elif x == '2':
        wirelessdhcp()
    elif x == '3':
        lanstatic()
    elif x == '4':
        wirelessstatic()
    elif x == '5':
        landisabled()
    elif x == '6':
        wirelessdisabled()
    elif x == '7':
        lanenabled()
    elif x == '8':
        wirelessenabled()
    elif x == '9':
        PingIP()
    elif x == '10':
        showIP()
    elif x == '11':
        routeprint()
    elif x == '12':
        os.system("ipconfig /renew")
        os.system("pause")
    else:
        print("please choice:\n")

if __name__ =='__main__':     #主程序
    localtime = time.localtime(time.time())
    #print ("time:", localtime)
    #print(localtime.tm_hour)
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if (localtime.tm_hour >= 17):
        wirelessdhcp()
        print("set net dhcp success")
        sys.exit(0)
        

    while True:
        try:
            setip()
        except Exception:
            print("main fail", Exception)
            traceback.print_exc()

