class Foo():
    def test(self):
        print("from the test")

class Bar(Foo):
    pass

if __name__ == '__main__':
    f1 = Foo()
    print(isinstance(f1,Foo)) # 检查一个实例是否属于该类
    print(issubclass(Bar,Foo)) # 检查一个类是否是由前一个类派生出来的
    