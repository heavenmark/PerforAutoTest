import xlwt
from Method import Log
from Method import Get
from Method import Perfor
import os


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


def data_excel(dict):                        #适用PerforTest
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
        file.save(r'../Data/perfor_data.xls')
        Log.logger().info("数据写入excel完毕")
        return file


def data_time(data,num):                    #适用start_T
    file=xlwt.Workbook()
    table=file.add_sheet("start_time",cell_overwrite_ok=True)
    table.write(0, 0, "cold_start")
    table.write(0, 1, "warm_start")
    try:
        for i in range(num):
            table.write(i+1,0 , data[i])
            table.write(i+1,1, data[num+i])
    except Exception as e:
        Log.logger().warning("data_time writing is fail")
    file.save(r'../Data/start_time.xls')
    Log.logger().info("数据写入excel完毕")
    return file


def data_time_new(data,num):               #v7.5.0以上的启动时间
    file=xlwt.Workbook()
    table=file.add_sheet("start_time",cell_overwrite_ok=True)
    table.write(0, 0, "PrivacyActivity")
    table.write(0, 1, "WelcomeActivity")
    table.write(0, 2, "LocationObtainActivity")
    table.write(0, 3, "MainFrameActivity")
    try:
        for i in range(num):
            table.write(i+1,0 , data[i]['main.privacy.Privacy'])
            table.write(i+1,1, data[i]['main.Welcome'])
            table.write(i+1,2 , data[i]['main.LocationObtain'])
            table.write(i+1,3 , data[i]['MainFrame'])
    except Exception as e:
        Log.logger().warning("data_time writing is fail")
    file.save(r'../Data/start_cold_new.xls')
    Log.logger().info("数据写入excel完毕")
    return file


def data_time_cold(data,num):
    file=xlwt.Workbook()
    table=file.add_sheet("start_time",cell_overwrite_ok=True)
    table.write(0, 0, "cold_start")
    # table.write(0, 1, "warm_start")
    try:
        for i in range(num):
            table.write(i+1,0 , data[i])
            # table.write(i+1,1, data[num+i])
    except Exception as e:
        Log.logger().warning("data_time writing is fail")
    file.save(r'../Data/start_cold.xls')
    Log.logger().info("数据写入excel完毕")
    return file


def data_time_warm(data,num):
    file=xlwt.Workbook()
    table=file.add_sheet("start_time",cell_overwrite_ok=True)
    table.write(0, 0, "warm_start")
    # table.write(0, 1, "warm_start")
    try:
        for i in range(num):
            table.write(i+1,0 , data[i])
            # table.write(i+1,1, data[num+i])
    except Exception as e:
        Log.logger().warning("data_time writing is fail")
    file.save(r'../Data/start_warm.xls')
    Log.logger().info("数据写入excel完毕")
    return file


def data_mem(data,activity,num):
    file=xlwt.Workbook()
    table=file.add_sheet("meminfo",cell_overwrite_ok=True)
    table.write(0, 0, "当前activity")
    table.write(0, 1, "内存大小MB")
    try:
        for i in range(num):
            table.write(i+1,0 , activity[i])
            table.write(i+1,1, data[i])
    except Exception as e:
        Log.logger().warning("data_time writing is fail")
    file.save(r'../Data/meminfo.xls')
    Log.logger().info("数据写入excel完毕")
    return file


if __name__ == '__main__':
    package = "com.jingdong.app.mall"
    os.system("adb shell am start -n %s/.main.MainActivity" % (package))
    x=Perfor.perfor(package,3,0)
    data_excel(x)

