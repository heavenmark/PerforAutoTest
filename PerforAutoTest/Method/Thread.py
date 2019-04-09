# coding=utf-8
import threading
import os
from Method import Perfor
from apply import apply
import time


class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        apply(self.func, self.args)
        # time.sleep(10)


package = "com.jingdong.app.mall"
num=5
threads=[]
for i in range(1,4):
    t=MyThread(Perfor.perfor,(package,num,i),Perfor.perfor.__name__)
    threads.append(t)


if __name__ == '__main__':
    os.system("adb shell am start -n %s/.main.MainActivity" % (package))
    for i in threads:
        i.start()
    # for i in range(3):
    #     threads[i].join()


    # 主线程
    print('end')