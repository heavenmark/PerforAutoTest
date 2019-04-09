from Method import Get
import os
import time
from Method import Time
from Method import Data
from Method import Log
from Method import Action

''' perfor(package,num,id) ,package表示包名，num表示数据采样的个数，
    id=0取三种维度的数据，id=1表示取cpu数据，id=2表示取内存数据，id=3表示取流量数据   
 '''


def perfor(package,num,id):
    try:
        pid=Get.get_pid(package)
        uid=Get.get_uid(pid)
    except Exception as e:
        Log.logger().warning(e)
    data = []
    if id == 0:
        data0=[]
        data1=[]
        data2=[]
        for i in range(num):
            a = Get.get_cpu(package)
            data0.append(a)
            b = Get.get_mem(package)
            data1.append(b)
            c = Get.get_net(pid,uid)
            data2.append(c)
        data.append(data0)
        data.append(data1)
        data.append(data2)
        Get.get_netcost(data2)
    elif id == 1:
        for i in range(num):
            a = Get.get_cpu(package)
            data.append(a)
    elif id == 2:
        for i in range(num):
            b = Get.get_mem(package)
            data.append(b)
    elif id == 3:
        for i in range(num):
            c = Get.get_net(pid,uid)
            data.append(c)
        Get.get_netcost(data)
    elif id == 4:
        sub0 = Log.log_cat(package)
        time.sleep(2)
        log_data = []
        for i in range(num):
            Action.cold_start(package)
            sub3 = Time.time_cold(sub0)
            log_data.append(sub3)
        Log.logger().info(log_data)
        Data.data_time_cold(log_data, num)
        time.sleep(3)
    elif id == 5:
        sub0 = Log.log_cat(package)
        time.sleep(2)
        log_data = []
        for i in range(num):
            Action.warm_start(package)
            sub3 = Time.time_warm(sub0)
            log_data.append(sub3)
        Log.logger().info(log_data)
        Data.data_time_warm(log_data, num)
    else:
        print("请输入正确的id")
    dict0={id:data}
    time.sleep(3)
    return dict0


if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    # os.system("adb shell am start -n %s/.main.MainActivity" % (package))
    try:
        x=perfor(package,5,0)
    except KeyboardInterrupt:
        print("1111")
