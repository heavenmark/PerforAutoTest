import os
import logging
import subprocess


def logger():
    #创建logger，如果参数为空则返回root logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  #设置logger日志等级
    #这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        #创建handler
        fh = logging.FileHandler(r'../Data/logcat.log',encoding="utf-8")
        # fh = logging.FileHandler(r'logcat.log', encoding="utf-8")
        ch = logging.StreamHandler()
        #设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(filename)s - %(message)s",
            datefmt="%Y/%m/%d %X"
            )
        #为handler指定输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #为logger添加的日志处
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger #直接返回logger


def log_cat(package):
    os.system("adb shell logcat -c")
    cmd1="adb logcat | grep -i 'Displayed %s'"%(package)
    cmd2="adb logcat | findstr /C:'Displayed %s'"%(package)
    try:
        op=subprocess.Popen(cmd1,stdout=subprocess.PIPE,universal_newlines=True)
    except Exception as e:
        op=subprocess.Popen(cmd2,stdout=subprocess.PIPE,universal_newlines=True)
    logger().info("开始获取日志")
    return op


if __name__ == '__main__':

    logger().info("13333")