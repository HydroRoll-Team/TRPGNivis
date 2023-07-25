---
hide:
 - path
 - navigation
 - toc
---

<div align="center">

    <h1><font color="#002fa7">P</font>si CLI</h1>

    <q>Psi 是一个函数式编程语言，同时也是一个CLI语言，旨在通过人机交互实现指定的功能。该语言的设计目标是简单、易用、易学，同时也是一个多范式语言，支持函数式、命令式、面向对象、面向过程等多种编程范式。</q><br />
    <b>它是骰主以及插件或模型作者入门水系的关键。</b>

</div>

::cards:: cols=2

- title: 词法分析器模块
  content: |
    词法分析器模块负责将源代码转换为一系列标记（tokens）。它识别语言的基本元素，如标识符、关键字、运算符和字面量。
    <!-- `['OPERATOR', 'IDENTIFIER', 'SEPARATOR', 'SEPARATOR', 'CONTROL', 'IDENTIFIER', 'OPERATOR', 'INTEGER', 'SEPARATOR', 'IDENTIFIER', 'SEPARATOR', 'IDENTIFIER', 'OPERATOR', 'IDENTIFIER', 'SEPARATOR', 'IDENTIFIER', 'SEPARATOR', 'EOF']` -->
- title: 语法分析器模块
  content: |
    语法分析器模块接收词法分析器模块生成的标记序列，并将其转换为抽象语法树（AST）。AST是一种类似树状的数据结构，以更接近编程语言的语法结构的方式表示源代码。
- title: 内置类型模块
  content: |
    此模块定义了Psi语言的内置类型，如列表和字典。它提供了用于创建和操作这些类型实例的函数。
- title: 错误处理模块
  content: |
    此模块提供了在运行时捕获和处理错误的机制。它定义了一组异常类和用于抛出和捕获这些异常的函数。
- title: 执行环境模块
  content: |
    此模块定义了Psi语言的执行环境，包括变量的作用域和生命周期。它提供了用于在执行环境中定义和查找变量的函数。
- title: 解释器模块
  content: |
    此模块的主要任务是遍历AST并在执行环境中执行相应的操作。

::/cards::

<!-- <object data="/res/main.pdf" type="application/pdf" style="width: 40%; height: 200px">
    <embed src="/res/main.pdf" type="application/pdf" style="width: 40%; height: 40%;"/>
</object> -->
