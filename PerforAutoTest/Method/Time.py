import re
from Method import Log
from Method import Action
from Method import Get
from Method import Data
import time


def time_cold(op):
    start_time=0
    ver1=Get.get_version("com.jingdong.app.mall")
    if Get.compare_ver(ver1,"7.5.0"):
        n=2
    else:
        n=4
    for i in range(n):
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
            Log.logger().warning("get time_cold is fail")
    print(start_time)
    return start_time


def time_cold_new(op):
    ver1=Get.get_version("com.jingdong.app.mall")
    if Get.compare_ver(ver1,"7.5.0"):
        n=2
    else:
        n=4
    time = {}
    for i in range(n):
        str_out=op.stdout.readline()
        out = str_out.split()
        print(str_out)
        pattern = re.compile(r'\d+')
        activity=Get.get_activiy(str_out)
        try:
            if out!="\n" and len(out)>1:
                # print(out[-1])
                cell=pattern.findall(out[-1])
                if len(cell)==1:
                    a=int(cell[0])
                else:
                    a = int(cell[0]) * 1000 + int(cell[1])
            time[activity]=a
        except Exception as e:
            Log.logger().warning("get time_cold is fail")
    print(time)
    return time


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
        Log.logger().warning("get time_warm is fail")
    return start_time


if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    sub0=Log.log_cat(package)
    time.sleep(2)
    log_data=[]
    num=10
    for i in range(num):
        sub2=Action.cold_start(package)
        sub3=time_cold_new(sub0)
        if len(sub3)==4:
            log_data.append(sub3)
    #print(log_data)
    n=len(log_data)
    excel = Data.data_time_new(log_data,n)


