# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""


def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:  # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    # f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("../data/bill.txt")
    append_to_file("../data/bill.txt", "郑源涵,2023-01-03,300000,消费,正式")
