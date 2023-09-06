class Student:

    name: None
    age: None
    address: None
    #私有成员变量
    __spec =  "jerry"

    #构造方法
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        
    def __play(self):
        print("大家好，我其实是假冒jerry的")

    def say(self):
        if self.name == self.__spec:
            print(self.__play())
        else:
            print("大家好，我是%s" %self.name)
        
    def say_2(self, msg):
        print(f"大家好，我是{self.name}{msg}")