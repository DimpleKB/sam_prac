#front insertion and rear deletion using circular queue

class c_queue:
    def __init__(self,size=3):
        self.c_q=[0]*size
        self.size=size
        self.rear=-1
        self.front=0
        self.count=0
    def insert(self):
        if self.count==self.size:
            print("circular queue is full")
            return
        ele=int(input("enter element value"))
        self.rear=(self.rear+1)%self.size
        self.c_q[self.rear]=ele
        self.count+=1
    def delete(self):
        if self.count==0:
            print("circular queue is empty")
            return 
        print("deleted value is",self.c_q[self.front])
        self.front=(self.front+1)%self.size
        self.count-=1
    def display(self):
        if self.count==0:
            print("circular queue is empty")
            return
        i=self.front 
        for j in range(self.count):
            print(self.c_q[i],end=' ')
            i=(i+1)%self.size
        print()
    def exit1(self):
        print("program is exitted")
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
        while(True):
            choice=int(input("enter 1:insert 2:delete 3:display 4:exit \n your choice:"))
            m=self.get_menu()
            if choice in m:
                m[choice]()
c_q=c_queue()
c_q.run_menu()



