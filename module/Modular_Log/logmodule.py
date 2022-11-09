import time,os,logging
import traceback
from functools import wraps

# 定义基础路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 定义log目录的存放路径
LOG_PATH = os.path.join(BASE_PATH,'log')

# 判断路径文件是否存在
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

# 创建日志类
class Logger():
    def __init__(self):
        # 定义日志名称与路径
        self.logname = os.path.join(LOG_PATH,"{}.log".format(time.strftime("%Y%m%d")))
        # 创建日志对象
        self.logger = logging.getLogger("log")
        # 设置日志等级
        self.logger.setLevel(logging.DEBUG)
        # 设置日志格式对象
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s] :%(message)s'
        )
        # 创建FileHander对象
        self.filelogger = logging.FileHandler(self.logname,mode='a',encoding='UTF-8')
        # 创建StreamHandler对象
        self.console = logging.StreamHandler()
        # 设置对象级别
        self.filelogger.setLevel(logging.DEBUG)
        self.console.setLevel(logging.DEBUG)
        # 设置对象格式
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        # 加载对象
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

# 创建日志对象
Logger = Logger().logger

def message_log(func):
    @wraps(func)
    def log(*args,**kwargs):
        Logger.info(f'------开始执行{func.__name__}------')
        try:
            func(*args,**kwargs)
        except Exception as e:
            Logger.info(f'------{func.__name__}执行失败------')
            Logger.info(f'------{func.__name__}报错，错误信息如下：{traceback.format_exc()}')
            # raise e
        else:
            Logger.info(f'------{func.__name__}------执行通过')
    return log

@message_log
def test1():
    assert 1 == 2

if __name__ == '__main__':
    test1()