def avg(a=9,b=1):
    print("the avg is",(a+b)/2)
avg(4) #a=4 le lega and b =1 (default)
avg(4,8) #take both
avg() #default lega dono ke liye
# def avg(*number) this means ki no. ko ab wo tuple me dega......
def avg(*number):
    print(type(number))
    total=0
    for i in number:
        total+=i
    print("the avg is",total/len(number))
avg(2,3,4,5,6,7,8,9)
# Def avg(**number) - this means ki Dictionaly he no./Argument
# def name(**details):
   # print(type(details))
   # print("the details are:")
   # for key,value in details.items():
   #     print(f"{key} is {value}") #F string will learn in next page
def name(**name):
    print("hello",name["fname"],name["mname"],name["lname"])
name(fname="harry",mname="james",lname="potter")
name(lname="potter",fname="harry",mname="james")