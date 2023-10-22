class stack:
    def __init__(self,size=100):
        self.size=size
        self.stack=[]
        self.top=-1
    def is_empty(self):
        return self.top==-1
    def is_full(self):
        return self.top+1==self.size
    def push(self,val):
        if self.is_full():
            return Exception('Stack is full')
        self.stack.append(val)
        self.top+=1
    def pop(self):
        if self.is_empty():
            return Exception('Stack is empty')
        self.stack.pop()
        self.top-=1
    def peek(self):
        if self.is_empty():
            return Exception('Stack is empty')
        else:
            return self.stack[self.top]
        
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class lstack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top==None
    def push(self,val):
        cur=node(val)
        cur.next=self.top
        self.top=cur
    def pop(self):
        if self.is_empty():
            return Exception('Stack is empty')
        else:
            cur=self.top
            self.top=self.top.next
            del cur
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.top.value

class minstack:
    def __init__(self,size=100):
        self.stack=[]
        self.size=size
        self.top=-1
    def push(self,val):
        if self.top+1==self.size:
            return Exception("Stack is full")
        self.stack.append(val)
        self.top+=1
    def pop(self):
        if self.top==-1:
            return Exception("Stack is empty")
        else:
            self.stack.pop()
            self.top-=1
    def top1(self):
        if self.top==-1:
            return Exception("Stack is empty")
        else:
            print(self.stack[self.top])
    def getmin(self):
        if self.top==-1:
            return Exception("Stack is empty")
        else:
            print(min(self.stack))
        
l=minstack()
l.push(-2)
l.push(0)
l.push(-3)
l.getmin()
l.pop()
l.top1()
l.getmin()
                
