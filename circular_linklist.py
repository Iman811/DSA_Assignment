class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
        class circular_linkedlist:
            def __init__(self):
                self.start = None
        def insert_at_last(self,item):
            nd=node(item)
            if self.start is None:
                self.start=nd
                nd.next=self.start
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=nd
            nd.next=self.start
        def display(self):
            if self.start is None:
                print("List is empty")
            else:
                temp = self.start
                while True:
                    print(temp.data, end=" ")
                    temp = temp.next
                    if temp == self.start:
                        break
cl=circular_linkedlist()
cl.insert_at_last(10)
cl.insert_at_last(20)
cl.insert_at_last(30)
cl.insert_at_last(40)
cl.insert_at_last(50)
cl.display()



