string=raw_input("enter string:")
count1=0
count2=0
count3=0
special=0
for i in string:
   if(i.islower()):
         count1=count1+1
   elif(i.isupper()):
          count2=count2+1
   elif(i.isdigit()):
          count3=count3+1
   else: 
        special=special+1
       

print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print("The number of digits:")
print(count3)
print("Special characters:")
print(special)


