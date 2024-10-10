class Student:

    def __init__(self, name, title, age):
        self.name = name
        self.title = title
        self.age = age

    def hello(self):
        print(self.name)

    def upgrade (self):
        self.age += 60 
 
s = Student("Lev", "Egorov", 18)
s.hello()
s.upgrade()
print(s.age)


#print(type(s))  # <class '__main__.Student'>
#print(id(s))    # 12448112

#t = Student()
#print(type(t))  # <class '__main__.Student'>
#print(id(t))    # 12423408
