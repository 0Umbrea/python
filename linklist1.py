#练习题目1.1

class linknode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class linklist:
    def __init__(self):
        self.head=None
    def create(self,data):
        self.head=linknode(0)
        cur=self.head
        for i in range(len(data)):
            node=linknode(data[i])
            cur.next=node
            cur=node
    def length(self)->int:
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count
    def find(self,val)->linknode:
        cur=self.head
        while cur:
            if(cur.val==val):
                return cur
            cur=cur.next
        return None
    def insertFront(self,val):
        node=linknode(val)
        node.next=self.head.next
        self.head.next=node
    def insertRear(self,val):
        node=linknode(val)
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node
    def insertInside(self,index,val):
        cur=self.head
        count=0
        while cur and count<index-1:
            cur=cur.next
            count+=1
        if not cur:
            return "erroe"
        node=linknode(val)
        node.next=cur.next
        cur.next=node
    def change(self,index,val):
        count=0
        cur=self.head
        while cur and count<index:
            count+=1
            cur=cur.next
        if not cur:
            return "error"
        cur.val=val
    def removeFront(self):
        if self.head:
            self.head = self.head.next
    def removeRear(self):
        if not self.head or not self.head.next:
            return 'Error'
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
    def removeInside(self, index):
        count = 0
        cur = self.head 
        while cur.next and count < index - 1:
            count += 1
            cur = cur.next   
        if not cur:
            return 'Error'
        del_node = cur.next
        cur.next = del_node.next


class mylinklist:
    def __init__(self):
        self.head=linknode()
    def get(self,index):        
        cur=self.head
        count=0
        while cur and count<index+1:
            cur=cur.next
            count+=1
        if not cur:
            return -1
        return cur.val
    def addAtHead(self,val):
        node=linknode(val)
        node.next=self.head.next
        self.head.next=node
    def addAtTail(self,val):
        node=linknode(val)
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node
    def addAtIndex(self,index,val):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        if index>count:
            return 
        if index==count:
            self.addAtTail(val)
        if index<0:
            self.addAtHead(val)
        node=linknode(val)
        cur=self.head
        count=0
        while cur and count<index:
            count+=1
            cur=cur.next
        node.next=cur.next
        cur.next=node
    def deleteAtIndex(self,index):
        count=0
        cur=self.head
        node=linknode()
        while cur and count<index-1:
            count+=1
            cur=cur.next
        if count<index-1:
            return 
        node=cur.next
        cur.next=node.next
    def output(self):
        cur=self.head
        y=[]
        while cur.next:
            cur=cur.next
            y.append(cur.val)
        print(y)
            


l=mylinklist()
l.addAtHead(1)
l.output()
l.addAtTail(3)
l.output()
l.addAtIndex(1,2)  
l.output()
x=l.get(1)
print(x)           
l.deleteAtIndex(1)
l.output()
x=l.get(1)
print(x)            