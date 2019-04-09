# -- coding:utf-8 --
import os
import subprocess
from Method import Log
import re


def activity():
    try:
        a = os.popen("adb shell dumpsys activity | grep 'mFocusedActivity'").readlines()[0]
        # print(a)
        pattern = re.compile(r'com.jingdong.app.mall\/(.*)Activity')
        b = pattern.search(a).group(1)+'Activity'
        Log.logger().info('当前activity:'+'['+b+']')
        return b
    except Exception as e:
        Log.logger().warning("activity can not get")


def get_top_activity():
        dat = subprocess.Popen("adb shell dumpsys activity top",
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True              #shell=True时，参数可以按字符串传入
                               )
        datt=str(dat.stdout.read(),encoding='utf-8')   #把字节串转换成字符串
        #print(datt)
        activity = re.compile('\s*ACTIVITY ([A-Za-z0-9_.]+)/([A-Za-z0-9_.]+) \w+ pid=(\d+)')
        # in Android8.0 or higher, the result may be more than one
        m = activity.findall(datt)
        if m:
            top=m[-1][1]
            return top
        else:
            raise Exception("Can not get top activity, output:%s" % dat)


def activity_s(top):
    try:
        # print(top)
        pattern = re.compile(r'(.*)Activity')
        b = pattern.search(top).group(1)
        c=b.split('.')[-1]
        #print(c)
        return c
    except Exception as e:
        Log.logger().warning("activity can not get")


def phone():
    a = os.popen("adb shell getprop ro.product.model").readlines()[0]
    Log.logger().info("设备型号："+a)
    return a


def screen_size():
    a = os.popen("adb shell wm size").readlines()[0]
    Log.logger().info("屏幕分辨率："+a)
    return a


def battery():
    a = os.popen("adb shell dumpsys battery").readlines()
    Log.logger().info("电池状况："+str(a))
    return a


def imei():
    a = os.popen("adb shell dumpsys iphonesubinfo").readlines()
    Log.logger().info("IMEI："+str(a))
    return a


def osversion():
    a = os.popen("adb shell getprop ro.build.version.release").readlines()[0]
    Log.logger().info("系统版本："+str(a))
    return a


def sdkversion():
    a = os.popen("adb shell getprop ro.build.version.sdk").readlines()[0]
    Log.logger().info("sdk版本："+str(a))
    return a


def android_id():
    a = os.popen("adb shell settings get secure android_id").readlines()[0]
    Log.logger().info("android_id："+str(a))
    return a


def ip_address():
    a = os.popen("adb shell ifconfig | grep Mask").readlines()
    Log.logger().info("IP地址："+str(a))
    return a


def mac_address():
    a = os.popen("adb shell cat /sys/class/net/wlan0/address").readlines()[0]
    Log.logger().info("Mac地址："+str(a))
    return a


def base_info():
    phone()
    screen_size()
    # battery()
    # imei()
    osversion()
    # sdkversion()
    mac_address()
    android_id()


if __name__ == '__main__':
    top=get_top_activity()
    activity_s(top)

