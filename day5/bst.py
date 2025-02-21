class Node:
    def __init__(self,data=0):
        self.left=None
        self.right=None
        self.data=data

class Bst:
    def __init__(self):
        self.root=None
        print("empty bst tree is created")
    def add_node(self):
        data=int(input("enter data of the new node : "))
        node=Node(data)
        if self.root is None:
            self.root=node
            return 
        temp1=self.root
        temp2=None
        while temp1!=None:
            temp2=temp1
            if data < temp1.data:
                temp1=temp1.left
            else:
                temp1=temp1.right
        if data < temp2.data:
            temp2.left=node
        else:
            temp2.right=node

    # def recur_add(self,node,val):
    #     if node is None:
    #         return Node(val)
    #     else:
    #         if node.data > val:
    #             node.left=self.recur_add(node.left,val)
    #         else:
    #             node.right=self.recur_add(node.right,val)
    #     return node
    def delete_node(self):
        data = int(input('Enter data of the node to be delete: '))
        temp1 = self.root
        temp2 = None
        while temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        # If node to be deleted is a leaf node:
        if temp1.left is None and temp1.right is None:
            print(f'Node with data {temp1.data} deleted')
            if temp2.left is temp1:
                temp2.left = None
            else:
                temp2.right = None
        # If node to be deleted has 2 children
        elif temp1.left is not None and temp1.right is not None:
            print(f'Node with data {temp1.data} deleted')
            temp3 = temp1.right.left
            if temp3 is None:
                temp1.right.left = temp1.left
                # temp2.right=temp1.right
                # return
            else:
                while temp3.left is not None:
                    temp3 = temp3.left
                temp3.left = temp1.left
            # if root is the node being deleted
            if temp1 is self.root:
                self.root = temp1.right
                return
            if temp2.left is temp1:
                temp2.left = temp1.right
            else:
                temp2.right = temp1.right
        # when node to be deleted has exactly one child
        else: 
            print(f'Node with data {temp1.data} deleted')
            #link = return () if temp1.left temp1.left else temp1.right
            link = temp1.left # assume temp1 has left child
            if temp1.right:
                link = temp1.right
            if temp2.left is temp1:
                temp2.left = link
            else:
                temp2.right = link

        data=int(input("enter data ato be deleted"))
        cur=self.root
        parent=None
        while(cur.data!=data):
            parent=cur
            if cur.data > data:
                cur=cur.left
            else:
                cur=cur.right
        if cur.left is None and cur.right is None:
            if parent.left is cur:
                parent.left=None
            else:
                parent.right=None
            return 
        if cur.left is None or cur.right is None:
            if cur.right is None:
                parent.right= 
        


    def inorder(self,root):
        if  root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

    def preorder(self,root):
        if  root:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if  root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')

    def search(self):
        if  not self.root:
            print("tree is empty")
            return
        data=int(input("enter data to be searched"))
        temp=self.root
        level=1
        while temp != None:
            if temp.data==data:
                print(f'node with data {data} found at level - {level}')
                return
            if data<temp.data:
                temp=temp.left
            else:
                temp=temp.right
            level+=1
        print(f'node with data {data} not found')        

    def exit1(self):
        print("program has exitted")
        exit()
    
class Menu:
    def match_choice(self,choice,bst):
        match choice:
            case 1: 
                bst.add_node()
            case 2: 
                if bst.root is None:
                        print("tree is empty")
                else:
                    bst.delete_node()
            case 3: 
                if bst.root is None:
                        print("tree is empty")
                else:
                    bst.inorder(bst.root)
            case 4: 
                if bst.root is None:
                        print("tree is empty")
                else:
                    bst.preorder(bst.root)
            case 5: 
                if bst.root is None:
                        print("tree is empty")
                else:
                    bst.postorder(bst.root)
            case 6: 
                if bst.root is None:
                        print("tree is empty")
                else:
                    bst.search()
            case 7:
                bst.exit1()
    
    def run_menu(self):
        bst=Bst()
        while True:
            choice=int(input("enter 1:add node 2:delete node 3:inorder traversal 4:preorder t 5:postorder t 6:search a node 7:exit \n enter your choice : "))
            self.match_choice(choice,bst)

def start_app():
    menu=Menu()
    menu.run_menu()

start_app()