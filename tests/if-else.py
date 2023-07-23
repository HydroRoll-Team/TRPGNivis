"""
@TODO 包括`tests\if-else.py`在内的各种示例文件的介绍
"""

from psi import Psi

psi_instance = Psi("? a == 1: reply: 你好")
print(psi_instance)
psi_instance.execute()
result = psi_instance.get_result()
print(result)