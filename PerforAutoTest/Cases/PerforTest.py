import time
from Method import Perfor,Log,Get
import xlwt
import os
from Expand import BaseInfo


def data_get(dict):
    if 0 in dict:
        data=dict[0][2]
        c=Get.get_reverse(data)
        dict[0].append(c)
        del dict[0][2]
        dict[0].append(dict[0][2][0])
        dict[0].append(dict[0][2][1])
        del dict[0][2]
        # print(dict[0])
        return dict[0]
    else:
        for key in dict:
            # print(dict[key])
            return dict[key]


def data_excel(dict):
    file = xlwt.Workbook()
    table = file.add_sheet("performance_data")
    for key in dict:
        if key == 3:
            data=Get.get_reverse(dict[3])
            x = len(data)
            text = ["tcp_snd", "tcp_rcv"]
            for j in range(x):
                table.write(j, 0, text[j])
                for i in range(len(data[j])):
                    table.write(j, i + 1, data[j][i])
        elif key == 2:
            data=dict[key]
            x = len(data)
            table.write(0, 0, "mem_info")
            for i in range(x):
                table.write(0, i + 1, data[i])
        elif key == 1:
            data=dict[key]
            x = len(data)
            table.write(0, 0, "cpu_info")
            for i in range(x):
                table.write(0, i + 1, data[i])
        else:
            data = data_get(dict)
            x = len(data)
            text = ["cpu_info", "mem_info", "tcp_snd", "tcp_rcv"]
            for j in range(x):
                table.write(j, 0, text[j])
                for i in range(len(data[j])):
                    table.write(j, i + 1, data[j][i])
        file.save('perfor_data.xls')
        Log.logger().info("数据写入excel完毕")
        return file


if __name__ == '__main__':
    string=' num表示数据采样的个数，平均3s采集一次数据，id=0取三种维度的数据，id=1表示取cpu数据，id=2表示取内存数据，id=3表示取流量数据' \
           ',id=4表示冷启动时间数据，id=5表示热启动时间数据。PS：测试启动时间目前只适用性能测试专用手机mate9 \n'
    print(string)
    package = "com.jingdong.app.mall"
    cmd='adb devices'
    a=os.popen(cmd).readlines()[1]
    if a=='\n':
        print("error:devices not found"+'\n'+"error:devices not found"+'\n'+"error:devices not found")
    num=int(input('请输入采样个数num：'))
    id=int(input('请输入id：'))
    print("请打开京东app,性能测试马上开始~")
    time.sleep(3)
    # os.system("adb shell am start -n %s/.main.MainActivity" % (package))
    try:
        BaseInfo.base_info()
        x = Perfor.perfor(package,num,id)
        if id < 4:
            data_excel(x)
    except Exception as e:
        Log.logger().error(e)
    input("Press <enter>")






