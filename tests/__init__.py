from os.path import join, abspath, dirname

DIR = dirname(abspath(__file__))

token_dict = {}  # 创建一个空字典

with open(join(DIR, '..', 'psi', 'Grammar', 'Token'), 'r') as file:
    for line in file:
        if line := line.strip():
            values = line.split()  # 使用空格分割行，得到值列表
            code = values[0]  # 第一个值为代码
            symbol = values[1] if len(values) > 1 else None  # 第二个值为符号，如果没有第二个值，则设置为None
            token_dict[code] = symbol  # 将代码和符号添加到字典中

# 将字典中的键值对转换为多个变量及其对应的值
for code, symbol in token_dict.items():
    globals()[code] = symbol

# 打印变量及其对应的值
print(LPAR)
print(RPAR)
print(AWAIT)
# 其他变量...