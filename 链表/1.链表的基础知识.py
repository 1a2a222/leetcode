class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class singleLinklist:
    def __init__(self,node=None):
        self.head = node
    def is_empty(self):
        return self.head ==None
    def length(self):
        cur = self.head
        count = 0
        while cur!=None:
            count+=1
            cur = cur.next
        return count
    def travel(self):
        cur = self.head
        while cur!=None:
            print(cur.data,end=" ")
            cur = cur.next

    def add(self,item):
        #头部添加
        node = Node(item)
        node.next=self.head
        self.head = node
    def append(self,item):
        #尾部添加
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = node
    def insert(self,pos,item):
        pre = self.head
        count = 0
        node = Node(item)
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            while count<(pos-1):
                pre = pre.next
                count +=1
            #循环退出后
            node.next = pre.next
            pre.next = node
    def remove(self,item):
        cur = self.head
        pre = None
        while cur!=None:
            if cur.data ==item:
                if cur ==self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    def search(self,item):
        cur = self.head
        while cur!=None:
            if cur.data==item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == '__main__':
    l1 = singleLinklist()
    print(l1.is_empty())
    l1.append(1)
    print(l1.travel())
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)
    # print(l1.travel())
    l1.add(333)
    l1.insert(4,999)
    l1.insert(-9,888)
    l1.insert(99,777)
    print(l1.travel())
    l1.remove(888)
    print(l1.travel())
