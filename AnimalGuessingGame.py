
class BstNode:

    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def get_new_node(self, data):
        """Makes a new node
        precondition: data
        postcondition: a new node
        """
        new_node = BstNode()                                    # Creates an object for the new node
        new_node.data = data                                    # Sets the new node equal to the data
        return new_node

    def insert(self, head, data):
        """Puts the data into the tree
        precondition: if the head is empty, puts the data into the head
        postcondition: the head with the data"""
        if head == None:
            head = self.get_new_node(data)                      # sets head to the new node with the data if it is empty
        else:
           head.data = data                                     # sets the date in the head the new data
        return head

    def make_tree(self, file, head):
        """Constructs the tree
        precondition: a file with questions and guesses and the head
        postcondition: the tree"""
        f = file.readline()                                     # reads the file
        if f == "Question:\n":
            f = file.readline()
            head = self.insert(head, f)                         # if the line is a question, reads the next line and
            head.left = self.make_tree(file, head.left)         # inserts the data into its node on the tree then recursively
            head.right = self.make_tree(file, head.right)       # calls on the left and right children
        else:
            f = file.readline()                                 # if it is a guess, reads the next line and inserts it into
            head = self.insert(head, f)                         # a node
        return head

    def traverse(self, head):
        """ it constructs the data in the tree and writes it where it belong in the game
        precondition: It checks that there is data in the head and that data can be distributed int each node of the tree
        """
        if head != None:                # if the head it is not empty it prints out the data in it
                                        # then it checks if the data is no and it it no it asks the user a question
                                        # and the user inserts a question and that question writes into the file
                                        # and we set up s new node for each question and guess which inserts data into the left and
                                        # right left of the left child
                                        # And we do the same thing when it is yes but we check the right child this time instead of the left
            print(head.data)
            user = input("yes or no?")
            if user == "no":
                if head.left.left == None and head.left.right == None:
                    print(head.left.data)
                    u = input("yes or no?")
                    if u == "no":
                        user2 = input("What was your animal?") + "\n"
                        print(user2)
                        question = input("What is your question?") + "\n"
                        question_node = self.get_new_node(question)
                        animal_node = self.get_new_node(user2)
                        question_node.right = animal_node
                        question_node.left = head.left
                        head.left = question_node
                    elif u == "yes":
                        print("I was right")
                else:
                    self.traverse(head.left)
            if user == "yes":
                if head.right.left == None and head.right.right == None:
                    print(head.right.data)
                    u = input("yes or no?")
                    if u == "no":
                        user2 = input("What was your animal?") + "\n"
                        print(user2)
                        question = input("What is your question?") + "\n"
                        question_node = self.get_new_node(question)
                        animal_node = self.get_new_node(user2)
                        question_node.right = animal_node
                        question_node.left = head.left
                        head.left = question_node
                    elif u == "yes":
                        print("I was right")
                else:
                    self.traverse(head.right)
        else:
            return head

    def write_file(self, head, openfile):
        """
        Updataes the file with the new question and animal
        precondition: make sure you have open file so that you can update a data on it
        poscondition: updated file
        """
        if head == None:
            return
        if head.left != None:
            openfile.write("Question:\n")                   # writes question before the actual question is written
            openfile.write(head.data)                       # writes the data in the head and recursively calls to the left
            self.write_file(head.left, openfile)            # and right children
            self.write_file(head.right, openfile)
        else:
            openfile.write("Guess:\n")                      # writes guess before the guess
            openfile.write(head.data)                       # writes the guess


def preorder(head):
    """Reads the file in a preorder format
    precondition: the head of the file
    postcondition: None"""
    if head == None:
        return
    print(head.data)                                        # if head is not empty then print out its data recursively
    preorder(head.left)                                     # to the left and right children
    preorder(head.right)


def main():
    head = None                                             # sets head to None
    tree = BstNode()                                        # makes a new object
    text = open("game_data", "r")                           # opens the file for reading
    head = tree.make_tree(text, head)                       # makes the tree
    tree.traverse(head)                                     # plays the game
    text.close()
    file = open("game_data", "w")                           # opens the file for writing
    file.seek(0)
    file.truncate()
    tree.write_file(head, file)                             # writes to the file
    file.close()
main()
