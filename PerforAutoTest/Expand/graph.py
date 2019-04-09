# -- coding:utf-8 --
import matplotlib.pyplot as plt
from Method import Get,Data
from scipy.interpolate import spline
import numpy as np
from Expand import BaseInfo

plt.rcParams['font.sans-serif']=['SimHei']    #使图标标题可以显示中文
plt.rcParams['axes.unicode_minus'] = False


def pint_mem(x):
    fig=plt.figure()                   #创建画板
    ax0=fig.add_subplot(111)
    # fig,ax=plt.subplot(nrows=2, ncols=1)
    # ax[0, 1].set(title='Upper Right')
    length=len(x)
    xs=[i for i in range(length)]
    data_obj={'x':xs,'y':x,}
    ax0.set(
           title=u'内存占用趋势图',
           xlabel=u'采集次序',
           ylabel=u'内存(单位:MB)')
    xnew=np.linspace(xs[0],xs[-1],300)          #使曲线变得光滑
    power_smooth=spline(xs,x,xnew)
    for x,y in zip(xs, x):   #在图上标注具体数值
        plt.text(x + 0.15, y, '%.0f' % y , ha='center', va='bottom', fontsize=10.5)
    ax0.plot(xnew,power_smooth,color='blue')
    ax0.scatter('x','y',color='blue',marker='D',data=data_obj)
    plt.xticks(range(0, length, 1))
    plt.show()


def pint_mem2(x,a):
    fig=plt.figure()
    ax0=fig.add_subplot(111)
    length=len(x)
    xs=[i for i in range(length)]
    data_obj={'x':xs,'y':x,}
    ax0.set(title=u'内存占用趋势图',xlabel=u'采集次序',ylabel=u'内存(单位:MB)')
    ax0.scatter('x','y',color='blue',data=data_obj)
    plt.xticks(range(0, length, 1))
    if a[0]==None and a[-1]==None:
        for x, y in zip(xs, x):  # 在图上标注具体数值
            plt.text(x + 0.15, y, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
    else:
        for x,y,a in zip(xs, x,a):   #在图上标注具体数其他内容
            plt.text(x + 0.15, y, '%s' % a , ha='center', va='bottom', fontsize=10.5)
    plt.plot('x','y',marker='o',data=data_obj)
    # plt.xticks(range(length),a)  #坐标轴显示activity
    plt.show()


if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    data=[]
    activity=[]
    print("-------------------------------------")
    for i in range(100):
      x=Get.get_mem(package)
      top=BaseInfo.get_top_activity()
      a=BaseInfo.activity_s(top)
      data.append(x)
      activity.append(a)
    num = len(data)
    Data.data_mem(data, activity, num)
    # pint_mem2(data,activity)






