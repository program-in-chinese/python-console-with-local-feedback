import re

class 翻译:
    字典 = {
        r"Traceback \(most recent call last\):": r"回溯 (最近的调用在最后):",
        r"AttributeError: '(.*)' object has no attribute '(.*)'": r"属性错误: '\1'个体没有'\2'属性",
        r"NameError: name '(.*)' is not defined": r"命名错误: 命名'\1'未定义",
        r"NameError: free variable '(.*)' referenced before assignment in enclosing scope": r"命名错误: 在闭合作用域中, 自由变量'\1'在引用之前未被赋值",
        r"SyntaxError: invalid syntax": r"语法错误: 不正确的语法",
        r"TypeError: unsupported operand type\(s\) for /: '(.*)' and '(.*)'": r"类型错误: 不支持/的操作数: '\1'和'\2'",
        r"TypeError: unsupported operand type\(s\) for \*\* or pow\(\): '(.*)' and '(.*)'": r"类型错误: 不支持**或pow()的操作数: '\1'和'\2'",
        r"TypeError: can't multiply sequence by non-int of type '(.*)'": r"类型错误: 不能用非整数的类型--'\1'对序列进行累乘",
        r'TypeError: can only concatenate list \(not "(.*)"\) to list': r'类型错误: 只能将list(而非"\1")联结到list',
        r"TypeError: must be str, not int": r"类型错误: 不能将整数自动转换为字符串",
        r"UnboundLocalError: local variable '(.*)' referenced before assignment": r"本地变量未定义错误: 本地变量'\1'在引用之前未被赋值",
        r"ZeroDivisionError: division by zero": r"除零错误: 不能被0除",
        }

    # 参考: https://docs.python.org/3/library/re.html#re.sub
    @staticmethod
    def 中文化单行(原始信息):
        for 英文模式 in 翻译.字典:
            if re.match(英文模式, 原始信息):
                return re.sub(英文模式, 翻译.字典[英文模式], 原始信息)
        return 原始信息

    @staticmethod
    def 中文化(原始信息):
        汉化行 = []
        for 某行 in 原始信息:
            汉化行.append(翻译.中文化单行(某行))
        return ''.join(汉化行)