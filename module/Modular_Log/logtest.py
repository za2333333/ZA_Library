import logging,time,os
from functools import wraps
import traceback

"""handler是什么？"""
# logging模块中包含的类
# 用来自定义日志对象的规则（比如：设置日志输出格式、等级等）
# 常用子类；StreamHandler、FileHandler
# StreamHandler 控制台输出日志
# FileHandler 日志输出到文件

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))    # 基础路径

# 存放日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,"log")
if not os.path.exists(LOG_PATH):    # 判断括号里的文件是否存在的意思，括号内的可以是文件路径
    os.mkdir(LOG_PATH)  # 用于以数字权限模式创建目录

class Logger():

    def __init__(self):
        # 创建日志路径和时间
        """知识点解析 #time strftime()函数接收以时间元组，并返回以可读字符串表示当地的时间，格式由参数format决定。"""
        # 日志命名，format函数笔记中有
        self.logname = os.path.join(LOG_PATH,"{}.log".format(time.strftime("%Y%m%d")))
        # 创建一个logger日志对象
        self.logger = logging.getLogger("log")  # 将log初始化
        # 设置默认的日志级别
        self.logger.setLevel(logging.DEBUG) # 设置日志等级
        # 创建日志格式对象
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        )
        """模块参数详解：
            %(asctime)s：字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
            %(filename)s：调用日志输出函数的模块的文件名
            %(lineno)d：调用日志输出函数的语句所在的代码行
            %(levelname)s：文本形式的日志级别
            %(message)s：用户输出的消息"""

        # 创建FIleHandler对象
        """mode = 'a'"""
            # a=append=追加，即 给文件保存写入的内容，不是覆盖之前已有文件中内容，而是放在最后，追加到最后
            # 一般append追加，适用于log日志的处理，保留之前log，追加写入新log
        self.filelogger = logging.FileHandler(self.logname,mode='a',encoding='UTF-8')
            # FileHandler继承自StreamHandler。将日志信息输出到磁盘文件上
            # 可以理解为用UTF-8的格式追加log到logname的文件中
            # 个人理解为：handler是控制log文件的，logger是控制程序文件的，logger.addHandler(handler)，确定程序的log要写到哪个文件
        # 创建StreamHandler对象
        self.console = logging.StreamHandler()
            # 能够将日志信息输出到sys.stdout, sys.stderr或者类文件对象（更确切点，就是能够支持write()和flush()方法的对象）
            # 可以理解为logger中添加StreamHandler，可以将日志输出到屏幕上

        # FileHandler对象自定义日志级别
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)

        # 设置两个地方的格式
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)

        # logger日志对象加载FIleHandler对象
        self.logger.addHandler(self.filelogger)
        # logger日志对象加载StreamHandler对象
        self.logger.addHandler(self.console)

Logger = Logger().logger

def decorate_log(func):
    @wraps(func)
    # @wraps(view_func)的作用: 不改变使用装饰器原有函数的结构(如name, doc)，即不改变hbp()的结构
    # 在hbp()使用__name__返回的是hbp,使用__doc__返回的是hbp的注释
    def log(*args,**kwargs):
        # *args表示任何多个无名参数，它是一个tuple；** kwargs表示关键字参数，它是一个dict
        Logger.info(f'------开始执行{func.__name__}-----')
        try:
            func(*args,**kwargs)
        except Exception as e:
            print(e)
            Logger.error(f'------{func.__name__}执行失败：{e}------')
            Logger.error(f"{func.__name__} is error,here are details:{traceback.format_exc()}")
            # 通过tracebackmodule来打印和格式化traceback的相关信息
            raise e
        else:
            Logger.info(f'------{func.__name__}执行成功------')
    return log

@decorate_log
def hbp():
    # print('开始执行hbp')
    assert 1 == 1

if __name__ == '__main__':
    hbp()

    # Logger.info("---测试开始---")
    # Logger.error("---测试结束---")
    # Logger.debug("---测试结束---")