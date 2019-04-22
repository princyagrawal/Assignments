class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my age is " + str(self.age))
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc() 
p1.name="Princy"
print(p1.name)
p1.myfunc()
del p1.age
print(p1.age)

