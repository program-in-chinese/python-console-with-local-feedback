## Python3报错信息中英对应列表

下面列出报错实例, 对应中文. 最后列出相关Python编译器源码

### 语法错误
参考: https://docs.python.org/3/tutorial/errors.html#syntax-errors
```python
>>> while True print('好啊')
  File "<stdin>", line 1
    while True print('好啊')
                   ^
SyntaxError: invalid syntax
语法错误: 不正确的语法
```

### 运行时错误

#### 除零错误(ZeroDivisionError)
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
除零错误: 不能被0除
```

#### 命名错误(NameError)
- 实例1
```python
>>> 学
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '学' is not defined
命名错误: 命名'学'未定义
```
- 实例2
参考: https://stackoverflow.com/questions/43778685/nameerror-free-variable-type-referenced-before-assignment-in-enclosing-scop?rq=1
```python
>>> def foo():
...     def bar():
...             print(type)
...     bar()
...     type = 1
...
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in foo
  File "<stdin>", line 3, in bar
NameError: free variable 'type' referenced before assignment in enclosing scope
命名错误: 在闭合作用域中, 自由变量'type'在引用之前未被赋值
```

#### 本地变量未定义错误(UnboundLocalError)
参考: https://stackoverflow.com/questions/18002794/local-variable-referenced-before-assignment-in-python
```python
>>> def 上课():
...     学生 = 学生*2
...
>>> 上课()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in 上课
UnboundLocalError: local variable '学生' referenced before assignment
本地变量未定义错误: 本地变量'学生'在引用之前未被赋值
```

#### 类型错误(TypeError)
参考: https://docs.python.org/3.6/tutorial/errors.html#exceptions
但与文档不一致"TypeError: Can't convert 'int' object to str implicitly"
```python
>>> '2'+2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
类型错误: 不能将整数自动转换为字符串
```

```python
>>> '2'/'1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
类型错误: 不支持/操作数: 字符串和字符串
>>> '2'**2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
类型错误: 不支持**或pow()的操作数: 字符串和整数
>>> '2'*'2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
类型错误: 不能用非整数的类型--字符串对序列进行累乘
>>> [1]+'2'
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
类型错误: 只能将list(而非"str")联结到list
```

#### 属性错误(AttributeError)
```python
>>> [1,2,3].length
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'list' object has no attribute 'length'
属性错误: 'list'个体没有'length'属性
```
