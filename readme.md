# psi

***

- [ ] 模块导入

我们可以使用 "import" 和 "export" 命令来实现模块化

import: module_name
export: function_name

***

- [ ] 循环结构
      
可以使用 "loop" 命令来创建循环，然后使用数字来指定循环的次数。

loop 5: reply: "你好"

***

- [ ] 选择结构

用"?"代替if，用"!"代替else。

? x == y: x += 1
! y += 1

***

- [ ] 函数定义

使用def关键字定义函数，再用函数本身调用。

def greet(name): reply: Hello, {name}!
greet: baimianxiao

***

- [ ] 类型定义

定义列表和字典

list colors = red, blue, green
dict person = name: baimianxiao, age: 18

***

- [ ] 错误处理

使用try…catch…

try: riskyOperation
catch: reply: 这是错误处理

***

- [ ] 并行执行

使用&开启线程

task1 & task2: reply: 两个任务执行 ing

***

- [ ] 延迟执行

使用~<秒数>延迟进程

~5: reply: 延迟五秒回复

***

- [ ] 条件执行

|这个是条件执行，前面执行失败才会执行后面

riskyOperation | reply: 执行失败

***

- [ ] 导入包

使用import关键字

import: extraFeatures

***

- [ ] 注释语句

单行注释#，多行"""..."""

# 这是一条注释

"""
多行
注释
"""

***

- [ ] 数据流

我们可以使用 ">>" 和 "<<" 符号来表示数据流

input >> process >> output

***

- [ ] 事件监听

然后我们可以使用 "@" 符号来表示事件监听

@newMessage: reply: 一条新消息

***

- [ ] 模式匹配

我们可以使用 "~=" 符号来进行模式匹配

? message ~= "hello*": reply: 你好

***

- [ ] 断言

我们可以使用 "assert" 命令来进行断言

assert answer = correct: reply: Correct answer!

***

- [ ] 重复执行

*3: reply: 重复三次

***

- [ ] 别名

alias r := reply
r: 这是一个别名
