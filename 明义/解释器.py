from code import InteractiveConsole
import sys
import traceback
from 翻译 import 翻译

class 中文报错控制台(InteractiveConsole):
    """
    封装Python控制台, 对输出进行转换
    """

    # 由InteractiveConsole.showsyntaxerror源码改写
    def showsyntaxerror(self, filename=None):
        type, value, tb = sys.exc_info()
        sys.last_type = type
        sys.last_value = value
        sys.last_traceback = tb
        if filename and type is SyntaxError:
            # Work hard to stuff the correct filename in the exception
            try:
                msg, (dummy_filename, lineno, offset, line) = value.args
            except ValueError:
                # Not the format we expect; leave it alone
                pass
            else:
                # Stuff in the right filename
                value = SyntaxError(msg, (filename, lineno, offset, line))
                sys.last_value = value
        if sys.excepthook is sys.__excepthook__:
            行 = traceback.format_exception_only(type, value)
            self.write(翻译.中文化(行))
        else:
            # If someone has set sys.excepthook, we let that take precedence
            # over self.write
            sys.excepthook(type, value, tb)

    # 由InteractiveConsole.showtraceback源码改写
    def showtraceback(self):
        sys.last_type, sys.last_value, 回溯信息 = 运行信息 = sys.exc_info()
        sys.last_traceback = 回溯信息
        try:
            行 = traceback.format_exception(运行信息[0], 运行信息[1], 回溯信息.tb_next)
            if sys.excepthook is sys.__excepthook__:
                self.write(翻译.中文化(行))
            else:
                # If someone has set sys.excepthook, we let that take precedence
                # over self.write
                sys.excepthook(运行信息[0], 运行信息[1], 回溯信息)
        finally:
            回溯信息 = 运行信息 = None

def 解释器():
    参数 = sys.argv[1:]

    # 运行解释器
    if len(参数) == 0:
        控制台 = 中文报错控制台()

        """
        参考: https://stackoverflow.com/questions/893053/seeing-escape-characters-when-pressing-the-arrow-keys-in-python-shell
        """
        try:
            import readline
        except ImportError:
            pass
        控制台.interact()
    # 运行Python源码
    elif len(参数)==1:
        源码 = 参数[0]
        with open(源码) as 文件:
            # 参考 https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3
            #内容 = compile(文件.read(), 源码, 'exec')
            内容 = 文件.read()
        try:
            exec(内容)
        except Exception:
            sys.last_type, sys.last_value, 回溯信息 = 运行信息 = sys.exc_info()
            原反馈信息 = traceback.format_exception(运行信息[0], 运行信息[1], 回溯信息.tb_next)
            print(翻译.中文化(原反馈信息))

if __name__=="__main__":
    解释器()