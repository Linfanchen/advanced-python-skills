
import enum
import itertools


def iterate_list():
    """
    迭代列表
    """
    my_list = ['apple', 'banana', 'cherry']
    for index, value in enumerate(my_list):
        print(f"索引 {index} 的值是: {value}")

def iterate_list_start():
    """
    指定起始索引
    """
    my_list = ['apple', 'banana', 'cherry']
    for index, value in enumerate(my_list, start=2):
        print(f"索引 {index} 的值是: {value}")

def create_dict_from_list():
    """
    从列表创建字典
    """
    my_list = ['apple', 'banana', 'cherry']
    my_dict = {index:value for index, value in enumerate(my_list)}
    print(my_dict)
    print(type(my_dict))


def iterate_string():
    """
    迭代字符串
    """
    my_string = "hello"
    for index, char in enumerate(my_string):
        print(f"索引 {index} 的字符是: {char}")

def iterate_tuple():
    """
    迭代元组
    """
    my_tuple = ('apple', 'banana', 'cherry')
    for index, value in enumerate(my_tuple, start=5):
        print(f"索引 {index} 的值是: {value}")

def iterate_multi_index():
    """
    多级索引
    """
    nested_list = [
        ['apple', 'banana'],
        ['cherry', 'date'],
        ['fig', 'grape']
    ]
    for i, sub_list in enumerate(nested_list):
        for j, item in enumerate(sub_list):
            print(f"第一层索引 {i} 中的，第二层索引 {j} 的值是: nested_list[{i}][{j}] = {item}")

def iterate_with_zip():
    """
    同时迭代多个序列
    """
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['red', 'yellow', 'pink']
    for index, (item1,item2) in enumerate(zip(list1, list2)):
        print(f"索引 {index} 中的，第一个列表的值是: {item1}，第二个列表的值是: {item2}")

def iterate_and_filter():
    """
    过滤
    """
    my_list = [10, 20, 30, 40, 50]
    filtered_list = [(index, value) for index,value in enumerate(my_list) if index % 2 == 0]
    print(filtered_list)

def conbine_map_lambda():
    """
    enumerate 和 map 函数来对可迭代对象的每个元素应用函数，并获取索引。
    """
    my_list = [1, 2, 3, 4, 5]
    result = list(map(lambda x: (x[0], x[1] * 2), enumerate(my_list)))
    print(result)

def use_with_itertools():
    """
    itertools.cycle 函数来创建一个无限循环的迭代器，该迭代器会重复地遍历输入的可迭代对象。
    """
    my_list = ['apple', 'banana', 'cherry']
    cycled_list = itertools.cycle(my_list)
    for i, item in enumerate(cycled_list):
        print(f"Index: {i}, Item: {item}")
        if i >= 100:  # 限制输出
            break

if __name__ == '__main__':
    iterate_list()
    print("\n------------------\n")

    iterate_list_start()
    print("\n------------------\n")

    create_dict_from_list()
    print("\n------------------\n")

    iterate_string()
    print("\n------------------\n")

    iterate_tuple()
    print("\n------------------\n")

    iterate_multi_index()
    print("\n------------------\n")

    iterate_with_zip()
    print("\n------------------\n")

    iterate_and_filter()
    print("\n------------------\n")

    conbine_map_lambda()
    print("\n------------------\n")

    use_with_itertools()
    print("\n------------------\n")

