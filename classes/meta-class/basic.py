def test():
    MyClass = type("MyClass", (object,), {"attr": "value"})
    obj = MyClass()
    print(obj.attr)  # 输出：value

if __name__ == "main":
    test()
