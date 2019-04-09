import os
import time
import logging
import xlwt
import re
'''
手动操作要测模块，自动获取数据 
created by shenyihao at 20180816
'''

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def performance(package,num):
    cmd="adb shell \"ps | grep %s\""%(package)                #取pid
    cmd5="adb shell \"ps -A | grep %s\""%(package)
    logger.info("获取pid")
    try:
        pid = os.popen(cmd).readlines()[0].split()[1]
    except IndexError:
        pid = os.popen(cmd5).readlines()[0].split()[1]
    cmd1="adb shell cat /proc/%s/status | grep Uid "%(pid)         #根据pid取uid
    logger.info("获取uid")
    uid=os.popen(cmd1).readlines()[0].split()[1]
    cmd0="adb shell dumpsys meminfo | grep %s"%(package)          #根据包名获取内存使用情况
    cmd2="adb shell cat /proc/uid_stat/%s/tcp_snd"%(uid)          #根据uid获取tcp_snd流量数据
    cmd3="adb shell cat /proc/uid_stat/%s/tcp_rcv"%(uid)          #根据uid获取tcp_rcv流量数据
    cmd4="adb shell top -n 1 | grep %s"%(package)                 #根据包名 获取cpu使用情况
    i=num      #设置操作次数
    mem_data=[]
    snd_data=[]
    rcv_data=[]
    cpu_data=[]
    total_data=[]
    logger.info("开始获取性能数据")
    pattern=re.compile(r'\d+')
    while i>0:
        try:
            mem1 = os.popen(cmd0).readlines()[0].split()[0]
            mem = int(mem1)
        except ValueError:
            a = ''.join(pattern.findall(mem1))
            mem = int(a)/1024
        mem_data.append(mem)
        logger.info("meminfo%d"%(num-i)+":"+"\n"+str(mem))
        net1=os.popen(cmd2).readlines()[0]
        snd_data.append(net1)
        net2 = os.popen(cmd3).readlines()[0]
        rcv_data.append(net2)
        logger.info("netinfo%d"%(num-i)+":"+"\n"+"tcp_snd "+net1+"tcp_rcv "+net2)
        cpu=os.popen(cmd4).readlines()[0].split()[2]
        cpu_data.append(cpu)
        logger.info("cpuinfo%d"%(num-i)+":"+"\n"+cpu+"\n\n")
        i=i-1
    try:
        snd_cs = int(snd_data[-1]) - int(snd_data[0])     #tcp_snd流量数据
        rcv_cs = int(rcv_data[-1]) - int(rcv_data[0])     #tcp_rcv流量数据
        tcp_cs = str(snd_cs + rcv_cs)                     #总共消耗的流量
        total_data.append(tcp_cs)
    except ValueError:
        print("获取不到netinfo")                  #总共消耗的流量
    total_data.append(snd_data)
    total_data.append(rcv_data)
    total_data.append(mem_data)
    total_data.append(cpu_data)
    logger.info("性能数据获取完毕")
    return total_data

def data_cl(data):
    file=xlwt.Workbook()
    table=file.add_sheet("performance_data")
    x=len(data)
    text=["tcp_consume","tcp_snd","tcp_rcv","mem_info","cpu_info"]
    for j in range(x-1):
        table.write(j, 0, text[j])
        for i in range(len(data[j])):
            table.write(j, i+1, data[j][i])
    table.write(x-1,0,text[-1])
    table.write(x-1,1,data[-1])
    file.save("performance_data.xls")
    logger.info("数据写入excel完毕")


if __name__ == '__main__':
    try:
        while True:
            package = "com.jingdong.app.mall"
            time.sleep(5)
            num = 20
            logger.info("打开app,开始手动操作要测的模块")
            data = performance(package, num)
            try:
                excel = data_cl(data)
            except:
                logger.error("数据写入excel失败")
    except KeyboardInterrupt or IndexError:
        pass











