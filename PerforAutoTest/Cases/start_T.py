import os
import time
from Method import Time
from Method import Data
from Method import Log
from Method import Action

if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    sub0=Log.log_cat(package)
    time.sleep(2)
    log_data=[]
    num=15
    # for i in range(num):
    #     sub2=Action.cold_start(package)
    #     sub3=Time.time_cold(sub0)
    #     log_data.append(sub3)
    # Log.logger().info(log_data)
    # time.sleep(3)
    # os.system("adb shell input tap 821 2075")      #最后一次冷启动关闭后有个权限的弹框也要关闭才能继续进行
    for i in range(num):
        sub2=Action.warm_start(package)
        sub3=Time.time_warm(sub0)
        log_data.append(sub3)
    Log.logger().info(log_data)
    excel = Data.data_time_warm(log_data,num)



