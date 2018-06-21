import os
import time
from public.fileReader import YamlReader


# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')

DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


class Config(object):
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)


# 获取当前项目根目录
def propath(prjname="RuanBang"):
    v_path = os.getcwd()
    v_thepath = v_path[:v_path.find(prjname)] + prjname + "/"
    return v_thepath


class UrlTest:
    # 修改当前测试URL地址
    def pc(self):
        self.url = Config().get('url')
        return self.url['urlTest']


# 休眠时间
def timesl(num):
    if 0 < num < 50:
        time.sleep(num)
    else:
        print("休眠时间非 大于0，小于50，请重新设置")
