# -*- coding: utf-8 -*-
import wmi
import random
print ('正在修改IP,请稍候...')
wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
if len(colNicConfigs) < 1:
    print ('没有找到可用的网络适配器')
    exit()
print ("-------------------------------------------------------\n")
for i in range(len(colNicConfigs)):
    print (str(i+1)+" : ",colNicConfigs[i].IPAddress)
print ("-------------------------------------------------------\n")
i=int(input("选择以太网卡：\n"))
objNicConfig = colNicConfigs[i-1]



i=int(input("---------------------------\n1、切换成校园网\n2、切换成联通网\n---------------------------\n"))
if(i==1):
    arrIPAddresses = ['192.168.2.11']
    arrSubnetMasks = ['255.255.255.0']
    arrDefaultGateways = ['192.168.2.1']
    arrGatewayCostMetrics = [1]
    arrDNSServers = ['114.114.114.114', '8.8.8.8']
    intReboot = 0
    returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask =arrSubnetMasks)
   
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置IP成功')
        intReboot += returnValue[0]
    else:
        print ('修改失败: IP或子网掩码设置发生错误')
      
    returnValue = objNicConfig.SetGateways(DefaultIPGateway = arrDefaultGateways, GatewayCostMetric = arrGatewayCostMetrics)
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置网关成功')
        intReboot += returnValue[0]
    else:
        print ('修改失败: 网关设置发生错误')
       

    returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = arrDNSServers)
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置DNS成功')
        intReboot += returnValue[0]
    else:
        print (str(returnValue)+'修改失败: DNS设置发生错误')
       
else:
    arrIPAddresses = ['10.253.201.100']
    arrSubnetMasks = ['255.255.224.0']
    arrDefaultGateways = ['10.253.223.254']
    arrGatewayCostMetrics = [1]
    arrDNSServers = ['114.114.114.114', '8.8.8.8']
    intReboot = 0
    
    returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask =arrSubnetMasks)
   
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置IP成功')
        intReboot += returnValue[0]
    else:
        print ('修改失败: IP或子网掩码设置发生错误')
       
    returnValue = objNicConfig.SetGateways(DefaultIPGateway = arrDefaultGateways, GatewayCostMetric = arrGatewayCostMetrics)
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置网关成功')
        intReboot += returnValue[0]
    else:
        print ('修改失败: 网关设置发生错误')
     

    returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = arrDNSServers)
    if returnValue[0] == 0 or returnValue[0] == 1:
        print ('设置DNS成功')
        intReboot += returnValue[0]
    else:
        print (str(returnValue)+'修改失败: DNS设置发生错误')
      
if intReboot > 0:
    print ('需要重新启动计算机')
print ('修改结束')