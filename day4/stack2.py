#rear insertion and deletion

class stack:
    def __init__(self,size=3):
        self.stk=[]
        self.size=size
        print("empty stack is created")
    def push(self):
        if len(self.stk)==self.size:
            print("stack is full")
            return
        elem=input("enter element to be inserted")
        self.stk.append(elem)
    def pop(self):
        if not self.stk:
            print("stack is empty")
            return
        elem=self.stk[-1]
        print("deleted element is",elem)
        self.stk.pop()
    def is_full(self):
        if len(self.stk)==self.size:
            print("stack is full")
        else:
            print("stack is not full")
    def is_empty(self):
        if len(self.stk)==0:
            print("stack is empty")
        else:
            print("stack is not empty")
    def top(self):
        if len(self.stk)==0:
            print("stack is empty")
            return
        print("top element is",self.stk[0])
    def dispaly(self):
        if len(self.stk)==0:
            print("stack is empty")
            return
        for i in range(len(self.stk)):
            print(self.stk[i],end=' ')
    def exit1(self):
        print("the program is exited")
        exit()
    def get_menu(self):
        menu={
            1:self.push,
            2:self.pop,
            3:self.top,
            4:self.is_full,
            5:self.is_empty,
            6:self.dispaly,
            7:self.exit1
        }
        return menu
    def run_menu(self):
        while True:
            choice=int(input("enter 1:push 2:pop 3:top 4:is_full 5:is_empty 6:display 7:exit \n enter your choice"))
            m=self.get_menu()
            m.get(choice)()
    
s=stack()
s.run_menu()

