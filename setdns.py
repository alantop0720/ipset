# -*- coding: UTF8 -*-
# python3  pass

import wmi


def DnsDef():
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    if len(colNicConfigs) < 1:
        print("没有找到可用的网络适配器")
        exit()
    objNicConfig = colNicConfigs[0]
    arrDNSServers = ['223.5.5.5']
    returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)
    if returnValue[0] == 0:
        print("modify dns ok,dns is 223.5.5.5")
    else:
        print("modify dns fail")

		
if __name__ =='__main__':     #主程序
    DnsDef()
    print("main")
