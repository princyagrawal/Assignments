#to get a single string from 2 srings seperated by space and swap the first two characters of each string

a="hello"
b="world"

print a+" "+b


print(b[:2]+a[2:]+" "+ a[:2] + b[2:])

#print(c)
