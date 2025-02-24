class Node:
    def __init__(self,data=None):
        self.data=data
        self.link=None
    
class operations:
    def __init__(self,data=None):
        self.head=Node(data)

    def insert_at_pos(self,data):
        pos=int(input("enter the position"))
        t=Node(data)
        temp=self.head
        if pos==0:
            t.link=self.head
            self.head=t
            return
        else:
            j=0
            while temp!=None and j<pos-1:
                temp=temp.link
                j+=1
            if temp is None:
                print("position out of bound")
                return
            t.link=temp.link
            temp.link=t

    def delete_at_pos(self):
        pos=int(input("enter position od node to be deleted"))
        if pos==0:
            if self.head is None:
                print("list is empty")
            else:
                print("deleted node data is :",self.head.data)
                self.head=self.head.link
            return 
        else:
            j=0
            prev=None
            next=self.head
            while next is not None and j<pos:
                prev=next
                next=next.link
                j+=1
            if next is None:
                print("position valus is invalid")
                return
            if prev is not None: 
                prev.link=next.link
                print("deleted node data is :",next.data)

    def reverse(self):
        if self.head is None:
            print("list is empty")
            return
        prev=None
        next=self.head
        cur=self.head
        while(cur):
            next=cur.link
            cur.link=prev
            prev=cur
            cur=next
        self.head=prev

    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.link

l1=operations(10)
l1.insert_at_pos(20)
l1.insert_at_pos(30)
l1.insert_at_pos(40)
l1.display()
l1.delete_at_pos()
l1.display()
l1.delete_at_pos()
l1.display()
print()
l1.reverse()
l1.display()


