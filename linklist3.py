#练习题目3.1
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
    def output(self):
        cur=self.head
        y=[]
        while cur.next:
            cur=cur.next
            y.append(cur.val)
        print(y)
        del y
    def overturn(self):
        z=[]
        cur=self.head
        while cur.next:
            cur=cur.next
            z.append(cur.val)
        z.reverse()
        self.create(z)
    def delete(self,val):
        cur=self.head
        while cur.next:
            node=cur
            cur=cur.next
            if(cur.val==val):
                node.next=cur.next

l=linklist()
l.create([1,2,6,3,4,5,6])
l.output()
l.delete(6)
l.output()
