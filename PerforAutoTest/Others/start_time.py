import os
import time
import logging
import xlwt
import re
import subprocess

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def log_cat(package):
    os.system("adb shell logcat -c")
    cmd1="adb shell \"logcat | grep -i 'Displayed %s'\""%(package)
    op=subprocess.Popen(cmd1,stdout=subprocess.PIPE,universal_newlines=True)
    logger.info("开始获取日志")
    return op


def cold_start(package):                       #冷启动
    cmd0="adb shell pm clear %s" %(package)
    os.system(cmd0)
    time.sleep(2)
    logger.info("冷启动app")
    os.system("adb shell input tap 133 1717")    #125 1700   app所在位置
    time.sleep(1)
    os.system("adb shell input tap 779 1633")    #777 1577   权限弹框1
    time.sleep(1)
    # os.system("adb shell pm grant com.jingdong.app.mall android.permission.READ_PHONE_STATE")
    os.system("adb shell input tap 771 1591")    #780 1254   权限弹框2


def time_cold(op):
    start_time=0
    for i in range(2):
        out = op.stdout.readline().split()
        print(out)
        pattern = re.compile(r'\d+')
        try:
            if out!="\n" and len(out)>1:
                # print(out[-1])
                cell=pattern.findall(out[-1])
                if len(cell)==1:
                    a=int(cell[0])
                else:
                    a = int(cell[0]) * 1000 + int(cell[1])
            start_time = start_time+a
        except Exception as e:
            pass
    print(start_time)
    return start_time


def warm_start(package):                       #热启动
    cmd0="adb shell am force-stop %s" %(package)
    os.system(cmd0)
    time.sleep(2)
    logger.info("热启动app")
    os.system("adb shell input tap 133 1717")     #125 1700   app所在位置
    return 0


def time_warm(op):
    out = op.stdout.readline().split()
    pattern = re.compile(r'\d+')
    print(out)
    start_time=0
    try:
        cell=pattern.findall(out[-1])
        if len(cell) == 1:
            start_time = int(cell[0])
        else:
            start_time = int(cell[0]) * 1000 + int(cell[1])
        print(start_time)
    except Exception as e:
        pass
    return start_time


def data_cl(data,num):
    file=xlwt.Workbook()
    table=file.add_sheet("start_time",cell_overwrite_ok=True)
    table.write(0, 0, "cold_start")
    table.write(0, 1, "warm_start")
    try:
        for i in range(num):
            table.write(i+1,0 , data[i])
            table.write(i+1,1, data[num+i])
    except Exception as e:
        pass
    file.save("start_time.xls")
    logger.info("数据写入excel完毕")
    return file



if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    sub0=log_cat(package)
    time.sleep(2)
    log_data=[]
    num=3
    for i in range(num):
        sub2=cold_start(package)
        sub3=time_cold(sub0)
        log_data.append(sub3)
    print(log_data)
    time.sleep(3)
    os.system("adb shell input tap 821 2075")      #最后一次冷启动关闭后有个权限的弹框也要关闭才能继续进行
    for i in range(num):
        sub2=warm_start(package)
        sub3=time_warm(sub0)
        log_data.append(sub3)
    print(log_data)
    excel = data_cl(log_data,num)





















