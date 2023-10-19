#练习题目6.1
class linknode:
    def __init__(self,val=0,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random
class linklist:
    def __init__(self):
        self.head=None
    def create1(self,data):
        self.head=linknode(0)
        cur=self.head
        for i in range(len(data)):
            node=linknode(data[i][0])
            cur.next=node
            cur=node
    def create2(self,data):
         self.head=linknode(0)
         node=linknode(0)
         for i in range(len(data)):
            cur=self.head
            x=0
            while x<i:
                cur=cur.next
                x+=1
            count=0
            node=cur
            if(data[i][1]!=None):
                while count<data[i][1]:
                    count+=1
                    cur=cur.next
                node.random=cur
            else:
                cur.random=None
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
    def output1(self):
        cur=self.head
        y=[]
        while cur.next:
            cur=cur.next
            y.append(cur.val)
        print(y)
        del y
    def output2(self):
        cur=self.head.next
        y=[]
        count=1
        while count<self.length():
            if(cur.random!=None):
                y.append(cur.random.val)
            cur=cur.next
            count+=1
        print(y)
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
    #将链表中的奇数位置上的节点排在前面，偶数位置上的节点排在后面，返回新的链表节点。
    def sort_(self):
        cur=self.head.next
        count=1
        while count<self.length():
            if count%2==0:
                self.delete(cur.val)
                self.insertRear(cur.val)
            count+=1
            cur=cur.next
    #回文链表
    def judge(self):
        cur=self.head.next
        x=[]
        while cur:
            x.append(cur.val)
            cur=cur.next
        if(x==list(reversed(x))):
            return True
        else:
            return False

l=linklist()
l.create1([[7,None],[13,0],[11,4],[10,2],[1,0]])
l.create2([[7,None],[13,0],[11,4],[10,2],[1,0]])
l.output2()
