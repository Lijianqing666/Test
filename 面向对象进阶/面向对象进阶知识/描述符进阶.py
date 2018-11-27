class Typed():
    '''定义格式'''
    def __init__(self,name, expected_type):
        '''初始化'''
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        '''获取'''
        # 判断传入的值是否为None
        if instance is None:
            return self
        return self.name

    def __set__(self, instance, value):
        '''设置'''
        # 判断设置的值格式是否正确
        if not isinstance(value,self.expected_type): # 如果出入的值格式不正确报错
            raise TypeError("你他娘的真是个天才!")

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        '''删除'''
        instance.__dict__.pop(self.name)

class People():
    '''类属性, 被Typed约束'''
    name = Typed('name',str)
    age = Typed('name',int)
    salary = Typed('name',float)

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

if __name__ == '__main__':
    p1 = People('liyunlong',25,666.6) # 类型正确不报错
    # p1 = People(6,25,666.6) # 报错
    # p1 = People('liyunlong',25,666) #报错
    print(p1)
    print(People.__dict__)
    print(p1.name)
    print(p1.age)
    print(p1.salary)