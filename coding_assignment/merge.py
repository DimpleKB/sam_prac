class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class operations:
    def __init__(self,data):
        self.head=Node(data)

    def insert(self,data):
        t=Node(data)
        if self.head is None:
            self.head=t
            return
        t.link=self.head
        self.head=t

    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.link
    
    

class merge:
    
    def merge_point_pos(self,r1,r2):
        temp1=r1.head
        temp2=r2.head
        l1=0
        l2=0
        while(temp1):
            l1+=1
            temp1=temp1.link
        while(temp2):
            l2+=1
            temp2=temp2.link
        temp1=r1.head
        temp2=r2.head
        if l1 > l2:
            for _ in range(l1-l2):
                temp1=temp1.link
        else:
            for _ in range(l2-l1):
                temp2=temp2.link
        while(temp1 and temp2):
            if temp1==temp2:
                print("yes")
                return
            temp1=temp1.link
            temp2=temp2.link
        print("no")


l1=operations(100)
l1.insert(200)
l1.insert(300)
l1.insert(40)
l1.insert(50)
l1.display()
print()
print()
l2=operations(100)
l2.insert(200)
l2.insert(300)
l2.insert(400)
l2.insert(500)
l2.display()

res=merge()
res.merge_point_pos(l1,l2)

