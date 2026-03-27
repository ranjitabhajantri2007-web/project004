class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LLiterators:
    def __init__(self):
        self.first=None
    def insert(self,data):
        newnode=Node(data)
        if self.first==None:
            self.first=newnode
        else:
            cur=self.first
            while(cur.next):
                cur=cur.next
            cur.next=newnode
    def __iter__(self):
        cur=self.first
        while cur:
            yield cur.data
            cur=cur.next
            
#Linked list iterators

L1=LLiterators()
L1.insert("Welcome To GPT Mudhol")
L1.insert("MyName Almeera")
print("content of the list are")
for x in L1:
    print(x,end=" ")
