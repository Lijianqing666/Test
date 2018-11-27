class Str():
    def __init__(self,name,expected_type):
        self.name = name
        self.expected_type = expected_type # 限制name传入类型
    def __get__(self, instance, owner):
        '''获取'''
        print("get-->",instance, owner)
        # 防止类访问name属性
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        '''控制/设置传入的值'''
        print("set-->",instance,value)
        if not isinstance(value,self.expected_type): # if传入的类型不是限制的类型则会报错
            raise TypeError("兄弟, 你是来捣乱的吧!")

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("del-->", instance)
        instance.__dict__.pop(self.name)


class Int():
    def __get__(self, instance, owner):
        print("int 调用...")

    def __set__(self, instance, value):
        print("int 配置...")

    def __delete__(self, instance):
        print("int 删除...")

class People():
    name = Str('name',str) # name被Str代理
    # age = Int() # age被Int代理

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

if __name__ == '__main__':
    # p1 = People('alex',18,100)
    # p1.name

    # # 赋值
    # print(p1.__dict__)
    # p1.name = 'egonlin'
    # print(p1.__dict__)
    #
    # # 删除name
    # del  p1.name
    # print(p1.__dict__)

    # 用类操作属性name
    # People.name # 报错, 类去操作属性时, 会将None传给instance
    # print(People.name)# 来自<__main__.Str object at 0x00000000021184E0>
    # p1 = People(666,18,100) # 报错
    p1 = People('alex',18,100)
    # p1.__dict__['name']
    print(p1.__dict__['name'])