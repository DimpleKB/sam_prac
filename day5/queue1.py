#front delete and rear insertion in linear queue

class queue:
    def __init__(self,size=3):
        self.q=[]
        self.size=size
        self.front=0
        self.rear=-1
    def insert(self):
        if len(self.q)==self.size:
            print("queue is full")
            return 
        ele=int(input("enter element"))
        self.q.append(ele)
        self.rear+=1
    def delete(self):
        if self.front>self.rear:
            print("queue is empty")
            return
        print("element deleted is",self.q[self.front])
        self.front+=1
    def display(self):
        if self.front>self.rear:
            print("queue is empty")
            return
        for i in range(self.front,self.rear+1):
            print(self.q[i],end=' ')
        print()
    def exit1(self):
        print("program is exicted")
        exit()
    def get_menu(self):
        menu={
            1:self.insert,
            2:self.delete,
            3:self.display,
            4:self.exit1
        }
        return menu
    def run_menu(self):
        while True:
            choice=int(input("enter 1:insert 2:delete 3:display 4:exit\n enter your choice:"))
            m=self.get_menu()
            if choice in m:
                m[choice]()

q=queue()
q.run_menu()
