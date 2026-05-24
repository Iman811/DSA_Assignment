# Create Stack class
class Stack:

    # Constructor
    def __init__(self):

        # Create array of size 8 filled with 0
        self.stk = [0] * 8

        # Top points to top element
        # -1 means stack is empty
        self.top = -1

        # Maximum size of stack
        self.size = 8


    # Push operation
    def push(self, n):

        # Check overflow condition
        if self.top == self.size - 1:

            print("***** Stack Overflow *****")

        else:

            # Move top one step ahead
            self.top += 1

            # Insert element
            self.stk[self.top] = n

            print("Inserted item:", n)


    # Pop operation
    def pop(self):

        # Check empty stack
        if self.top == -1:

            print("***** Stack Underflow *****")
            return None

        else:

            # Store top element
            n = self.stk[self.top]

            # Move top backward
            self.top -= 1

            print("Deleted item:", n)

            return n


    # Display stack
    def display(self):

        # Stack empty
        if self.top == -1:

            print("***** Stack is Empty *****")

        else:

            print("Stack (top to bottom):")

            # Print from top to bottom
            for i in range(self.top, -1, -1):

                print(self.stk[i])


# Create object
s1 = Stack()


while True:

    print("--- STACK MENU ---")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        value = int(input("Enter value: "))
        s1.push(value)

    elif choice == 2:

        s1.pop()

    elif choice == 3:

        s1.display()

    elif choice == 4:

        print("Exiting...")
        break

    else:

        print("Invalid choice")