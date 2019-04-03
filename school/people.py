"""
@Auther: HeTongHao
@Date: 18/9/3 16:35
@Description: 练习类的继承
"""


class People:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("我的名字是:%s,年龄是:%d" % (self.name, self.age))


class Student(People):
    grade = 0

    def __init__(self, name, age, grade):
        People.__init__(self, name, age)
        # super(Student, self).__init__(age, grade)
        self.grade = grade

    def show(self):
        print("我的名字是:%s,年龄是:%d,今年读%d年级" % (self.name, self.age, self.grade))
