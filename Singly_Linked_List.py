class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)           ## Create a new node
        new_node.next = self.head       ## Next of new node becomes the current head
        self.head = new_node            ## Head points to the new node, ensures that new nodes are inserted at the beginning

    def append(self, data):
        new_node = Node(data)           ## Create a new node
        if self.head is None:
            self.head = new_node        ## If list is empty, new node is the head node
            return
        last = self.head                
        while last.next:                ## Traverse list to find the last node
            last = last.next
        last.next = new_node            ## Make the new node the next node of the last node

    def delete(self,key):
        temp = self.head                ## Initialize temp to the head of the list as starting point
        if temp and temp.data == key:   ## If the head node itself holds the key, delete it
            self.head = temp.next       ## Move the head to the next node
            temp = None                 
            return


    def display(self):
        temp = self.head                ## Start at the head of the list
        while temp:
            print(temp.data,end=' ')    ## Print current node data
            temp = temp.next            ## Move to next node
        print()

# Example Usage
sllist = SinglyLinkedList()
sllist.prepend("coke")
sllist.prepend("sprite")
sllist.prepend("royal")
sllist.prepend("sarsi")

print("Prepend")
sllist.display()

sllist.append("mug")
sllist.append("c2")
print("append")
sllist.display()

sllist.delete("coke")
sllist.delete("sarsi")
print("Delete")
sllist.display()