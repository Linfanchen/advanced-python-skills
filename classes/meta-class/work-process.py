from collections import OrderedDict

"""
‌类定义阶段‌：
__prepare__：创建有序字典存储类属性
__new__：构造类对象，修改命名空间（自动添加__doc__和__slots__）
__init__：初始化类对象，此时类属性已固定

‌实例化阶段‌：
__call__：接管实例创建过程
调用用户定义的__new__和__init__
添加额外实例属性_creation_time

‌扩展控制点‌：
在元类中可拦截/修改类属性定义（如Django ORM字段收集）
控制实例化时的额外处理（如单例模式、对象池等）
通过__prepare__保留属性顺序（对API文档生成很重要）
"""
class MetaLogger(type):
    # -------------------- Phase 1: Class Preparation --------------------
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        """Create and return a namespace dictionary with order preservation"""
        print(f"Step-1: [__prepare__] Creating namespace | Class: {name} | Bases: {bases}")
        return OrderedDict()  # Preserve attribute declaration order

    # -------------------- Phase 2: Class Construction --------------------
    def __new__(cls, name, bases, namespace, **kwargs):
        """Construct and return the class object"""
        print(f"\nStep-2: [__new__] Building class | Namespace keys: {list(namespace.keys())}")

        # Auto-generate docstring if missing
        if '__doc__' not in namespace:
            namespace['__doc__'] = f"Auto-generated class {name}"

        # Enforce __slots__ definition
        # if '__slots__' not in namespace:
        #     namespace['__slots__'] = ()
        #     print("[__new__] Warning: __slots__ not defined, added empty tuple")

        # Create class using modified namespace
        new_class = super().__new__(cls, name, bases, dict(namespace))

        # Add custom class-level metadata
        new_class._meta_author = "MetaLogger"
        return new_class

    def __init__(cls, name, bases, namespace, **kwargs):
        """Initialize the class object"""
        super().__init__(name, bases, namespace)
        print(f"Step-3: [__init__] Initialized class | Final attributes: {dir(cls)[:4]}...\n")

    # -------------------- Phase 3: Instance Creation --------------------
    def __call__(cls, *args, **kwargs):
        """Control instance instantiation process"""
        print(f"Step-4: [__call__] Creating instance | Args: {args}, Kwargs: {kwargs}")

        # Create instance through normal inheritance chain
        instance = super().__call__(*args, **kwargs)

        # Attach instance metadata
        instance._created_at = "2023-10-01"
        print("Step-7: [__call__] Instance creation complete")
        return instance


class DataModel(metaclass=MetaLogger):
    """Custom data model class"""
    version = 1.0

    def __new__(cls, value):
        print("\nStep-5: [DataModel __new__] Allocating memory")
        return super().__new__(cls)

    def __init__(self, value):
        print("Step-6: [DataModel __init__] Initializing instance")
        self.value = value


if __name__ == "__main__":
    print("\n========= Class Definition Phase =========")

    print("\n========= Instantiation Phase =========")
    obj = DataModel(42)

    print("\n========= Final Instance Inspection =========")
    print(f"Step-8: Instance attributes: {vars(obj)}")
    print(f"Step-9: Class metadata: _meta_author={DataModel._meta_author}")
