# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
with open("../data/bill.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    content = [line for line in lines if "测试" not in line]

with open("../data/bill.txt.bak", 'w', encoding='utf-8') as file:
    file.writelines(content)
print(f"文件处理完成，备份文件为bill.txt.bak。")
