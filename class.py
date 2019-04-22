import sys
class myclass:
      pass
x=5

obj = myclass()
obj.x = 123
print obj
print sys.getsizeof(obj)
print obj.x
print sys.getsizeof(obj)
print x
