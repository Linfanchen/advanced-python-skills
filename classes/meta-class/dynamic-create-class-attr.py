def test():
    """
    使用type函数动态创建了一个名为MyClass的类，并给它添加了一个属性attr
    """
    MyClass = type("MyClass", (object,), {"attr": "vanson"})
    obj = MyClass()
    print(obj.attr)  # 输出：value

if __name__ == "__main__":
    test()
