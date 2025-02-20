def monday():
    print("studying")
def tuesday():
    print("exercise")
def wednesday():
    print("washing")
def thursady():
    print("hair care")
def friday():
    print("skin care")
def saturday():
    print("baking")
def sunday():
    print("chilling")
def other_day():
    print("it's invalid choice")
    exit()
to_do={1:monday,2:tuesday,3:wednesday,4:thursady,5:friday,6:saturday,7:sunday,8:other_day}
while(True):
    choice=int(input("enter 1:monday 2:tuesday 3:wednesday 4:thursady 5:friday 6:saturday 7:sunday 8:exit"))
    to_do.get(choice)()