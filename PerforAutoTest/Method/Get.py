import os
from Expand import BaseInfo
from Method import Log
import re
import subprocess


'''
可以在operation中写操作步骤加循环自动执行要测模块，自动获取数据 

'''


#取pid
def get_pid(package):
    cmd="adb shell \"ps | grep %s\""%(package)
    cmd5="adb shell \"ps -A | grep %s\""%(package)
    # print(os.popen(cmd).readlines())
    try:
        pid = os.popen(cmd).readlines()[0].split()[1]
    except IndexError:
        pid = os.popen(cmd5).readlines()[0].split()[1]
    Log.logger().info("获取pid:"+str(pid))
    return pid


#根据pid取uid
def get_uid(pid):
    cmd1="adb shell cat /proc/%s/status | grep Uid "%(pid)
    uid=os.popen(cmd1).readlines()[0].split()[1]
    Log.logger().info("获取uid:"+str(uid))
    return uid


#获取app版本号
def get_version(package):
    cmd1="adb shell dumpsys package %s | grep 'versionName'"%(package)
    try:
        version=os.popen(cmd1).readline().split("=")[1]
        return version
    except Exception as e:
        Log.logger().info(e)


#比较版本号大小
def compare_ver(v0,v1):
    ver0=int("".join(v0.split(".")))
    ver1=int("".join(v1.split(".")))
    if ver1>ver0:
        return True
    else:
        return False


#获取activity
def get_activiy(str_out):
    pattern=re.compile(r'([A-Za-z0-9_.]+)/.(.*)Activity')
    try:
        activity=pattern.search(str_out).group(2)
        #print(activity)
        return activity
    except Exception as e:
        Log.logger().info(e)


#矩阵转置
def get_reverse(data):
    cost=[]
    length=len(data[0])
    for i in range(length):
        cost.append([row[i] for row in data])
    return cost


#获取流量信息,是历史累计值
def get_net(pid,uid):
    cmd2="adb shell \"cat /proc/uid_stat/%s/tcp_snd\""%(uid)          #根据uid获取tcp_snd流量数据
    cmd3="adb shell \"cat /proc/uid_stat/%s/tcp_rcv\""%(uid)          #根据uid获取tcp_rcv流量数据
    cmd4 = "adb shell cat /proc/%s/net/dev" % pid                     #根据pid获取流量数据
    total_data=[]
    try:
        net1=os.popen(cmd2).readlines()[0]
        total_data.append(int(net1))
        net2 = os.popen(cmd3).readlines()[0]
        total_data.append(int(net2))
        BaseInfo.activity()
        Log.logger().info("netinfo(byte):"+"\n"+"tcp_snd "+net1+"tcp_rcv "+net2)
    except Exception as e:
        try:
            pattern = re.compile(r'(wlan.*)')
            net = os.popen(cmd4).readlines()
            b = pattern.findall(str(net))[0].split(',')[0].split()
            net1 = b[9]
            total_data.append(int(net1))                              #获取tcp_snd流量数据
            net2 = b[1]
            total_data.append(int(net2))                              #获取tcp_rcv流量数据
            BaseInfo.activity()
            Log.logger().info("netinfo(byte):" + "\n" + "tcp_snd " + net1 + "\n" + "tcp_rcv " + net2)
        except Exception as e:
            Log.logger().warning("get_net"+"\n"+str(e))
            return False
    # print(total_data)
    return total_data


#计算消耗的流量
def get_netcost(data):
    cost=get_reverse(data)
    net_snd=(cost[0][-1]-cost[0][0])/1024
    net_rcv=(cost[1][-1]-cost[1][0])/1024
    net=net_snd+net_rcv
    Log.logger().info("\n"+"net_snd:"+str(net_snd)+"KB"+"\t"+"net_rcv:"+str(net_rcv)+"KB"+"\t"+"net_total:"+str(net)+"KB")
    return net


#获取cpu信息
def get_cpu(package):
    cmd4 = "adb shell \"top -n 1 | grep %s\"" % (package)  # 根据包名 获取cpu使用情况
    try:
        cpu = os.popen(cmd4).readlines()[0].split()[2]
        BaseInfo.activity()
        Log.logger().info("cpuinfo:" + "\n" + cpu)
        return cpu
    except Exception as e:
        Log.logger().warning("get_cpu"+"\n"+str(e))
        return False


#获取内存信息
def get_mem(package):
    pattern=re.compile(r'\d+')
    cmd0="adb shell dumpsys meminfo | grep %s"%(package)          #根据包名获取内存使用情况
    try:
        mem1 = os.popen(cmd0).readlines()[0].split()[0]
        mem = int(mem1)/1024
    except ValueError:
        a = ''.join(pattern.findall(mem1))
        mem = int(a) / 1024
        # print(a)
        # print(b)
    top=BaseInfo.get_top_activity()
    Log.logger().info('当前activity: ' + top)
    Log.logger().info("meminfo:"+"\n"+str(mem)+"MB")
    return mem


if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    ver1=get_version(package)
    compare_ver("7.5.1",ver1)













