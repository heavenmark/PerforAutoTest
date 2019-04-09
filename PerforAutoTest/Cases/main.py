from Expand import BaseInfo
from Method import Perfor,Log
from Method import Data

'''  num表示数据采样的个数，平均3s采集一次数据，id=0取三种维度的数据，id=1表示取cpu数据，id=2表示取内存数据，id=3表示取流量数据' \
           ',id=4表示冷启动时间数据，id=5表示热启动时间数据。PS：测试启动时间目前只适用性能测试专用手机mate9
 '''

if __name__ == '__main__':

    package = "com.jingdong.app.mall"
    # os.system("adb shell am start -n %s/.main.MainActivity" % (package))
    num=int(input('请输入采样个数num：'))
    id=int(input('请输入id：'))
    BaseInfo.base_info()
    x = Perfor.perfor(package,num,id)
    Data.data_excel(x)




