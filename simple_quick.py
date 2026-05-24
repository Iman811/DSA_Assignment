# Create Circular Queue class
class CircularQueue:

    def __init__(self):

        # Create array size 8
        self.que=[0]*8

        # Front pointer
        self.front=-1

        # Rear pointer
        self.rear=-1

        # Queue size
        self.size=8


    # Insert operation
    def insert(self,n):

        # Full condition
        if ((self.front==0 and self.rear==self.size-1)
            or
            (self.front==self.rear+1)):

            print("***** Queue Full *****")
            return


        # First insertion
        if self.front==-1:

            self.front=0
            self.rear=0

        else:

            # Circular movement
            self.rear=(self.rear+1)%self.size


        # Insert element
        self.que[self.rear]=n

        print("Inserted:",n)


    # Delete operation
    def delete(self):

        # Empty queue
        if self.front==-1:

            print("Queue Empty")
            return None


        # Store deleted item
        n=self.que[self.front]

        print("Deleted:",n)


        # Last element removed
        if self.front==self.rear:

            self.front=-1
            self.rear=-1

        else:

            # Circular movement
            self.front=(self.front+1)%self.size


        return n


    # Display queue
    def display(self):

        if self.front==-1:

            print("Queue Empty")
            return


        print("Queue elements:")

        i=self.front

        while True:

            print(self.que[i])

            # Stop at rear
            if i==self.rear:

                break

            # Circular movement
            i=(i+1)%self.size


q1=CircularQueue()

while True:

    print("--- CIRCULAR QUEUE MENU ---")
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")

    choice=int(input("Enter choice:"))

    if choice==1:

        value=int(input("Enter value:"))
        q1.insert(value)

    elif choice==2:

        q1.delete()

    elif choice==3:

        q1.display()

    elif choice==4:

        break