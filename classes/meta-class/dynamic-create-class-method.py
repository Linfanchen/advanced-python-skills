class Meta(type):
    def __new__(cls, name, bases, dct):
        dct["greet"] = lambda self: f"Hello from {name}"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())  # 输出：Hello from MyClass