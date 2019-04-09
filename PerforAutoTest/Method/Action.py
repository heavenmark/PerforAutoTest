import threading
import os
import time
from Method import Log
from Method import Get
from Expand import BaseInfo
import xlwt


#自定义操作
def operation(num):
    x=136       #横坐标
    y=584      #纵坐标
    Log.logger().info("开始执行操作")
    while num>0:
        os.system("adb shell input tap %d %d" % (x, y))  # 点击坐标所在按钮
        time.sleep(5)
        os.system("adb shell input keyevent 4")  # 返回
        num = num - 1


def mainflow1(n):
    os.system("adb shell input tap 976 1760")     #点击我的
    time.sleep(n)
    os.system("adb shell input tap 142 248")     #点击登录
    time.sleep(n)
    os.system("adb shell input tap 113 584")     #点击输入框
    os.system("adb shell input text nj_test")
    os.system("adb shell input tap 134 769")     #点击输入框
    os.system("adb shell input text test123")


def mainflow2(n):
    os.system("adb shell input tap 264 142")     #点击搜索
    time.sleep(n)
    os.system("adb shell input text lining")
    time.sleep(n)
    os.system("adb shell input tap 1016 139")     ##点击搜索
    time.sleep(n)
    os.system("adb shell input tap 250 1450")     #点击商品
    time.sleep(n)
    os.system("adb shell input tap 666 1742")     #点击购物车
    time.sleep(n)
    os.system("adb shell input tap 531 1748")     #点击确定
    time.sleep(n)
    os.system("adb shell input tap 448 1752")     #点击购物车
    time.sleep(n)
    os.system("adb shell input tap 910 1733")     #点击结算
    time.sleep(n)
    os.system("adb shell input tap 895 1742")     #点击提交订单
    time.sleep(n)
    os.system("adb shell input tap 973 148")     #点击订单中心
    time.sleep(n)


#热启动
def warm_start(package):                       #热启动
    cmd0="adb shell am force-stop %s" %(package)
    os.system(cmd0)
    time.sleep(2)
    Log.logger().info("热启动app")
    os.system("adb shell input tap 133 1717")     #app所在位置
    return 0


#冷启动
def cold_start(package):                       #冷启动
    cmd0="adb shell pm clear %s" %(package)
    os.system(cmd0)
    ver1=Get.get_version(package)
    if Get.compare_ver(ver1,"7.5.0"):
        time.sleep(2)
        Log.logger().info("冷启动app")
        os.system("adb shell input tap 133 1717")    #app所在位置
        time.sleep(1)
        os.system("adb shell input tap 531 1591")    #权限弹框1
        time.sleep(1)
        os.system("adb shell input tap 792 1699")    #权限弹框2
        # os.system("adb shell pm grant com.jingdong.app.mall android.permission.READ_PHONE_STATE")
    else:
        time.sleep(2)
        Log.logger().info("冷启动app")
        os.system("adb shell input tap 133 1717")    #app所在位置
        time.sleep(1)
        os.system("adb shell input tap 531 1591")    #隐私页弹框1
        time.sleep(1)
        os.system("adb shell input tap 534 1711")    #欢迎页弹框2
        time.sleep(1)
        os.system("adb shell input tap 781 1719")    #位置页弹框3
        time.sleep(1)
        os.system("adb shell input tap 781 1680")    #权限弹框4
        time.sleep(1)
        os.system("adb shell input tap 781 1680")    #权限弹框5


if __name__ == '__main__':
    package = "com.jingdong.app.mall"

    def mem(package):                #实时获取activity对应内存大小并导入excel
        print("-------------------------------------")
        file = xlwt.Workbook()
        table = file.add_sheet("meminfo", cell_overwrite_ok=True)
        table.write(0, 0, "当前activity")
        table.write(0, 1, "内存大小MB")
        num=200
        for i in range(num):
          x=Get.get_mem(package)
          top=BaseInfo.get_top_activity()
          a=BaseInfo.activity_s(top)
          table.write(i + 1, 0, a)
          table.write(i + 1, 1, x)
          file.save(r'../Data/meminfo.xls')
        Log.logger().info("数据写入excel完毕")
        return file

    cold_start(package)
    t = threading.Thread(target=mem, args=(package,))
    t.setDaemon(True)
    t.start()
    mainflow1(3)
    time.sleep(2)
    if input("enter:") == "ok":
        mainflow2(20)



