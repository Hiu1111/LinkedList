class Node: #creates the node for the LinkedList 
  def __init__(self, value):
    self.value = value #value of the node 
    self.next = None #next is set to None by default


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self, value):
        new_node = Node(value)
        if self.head is None: #checks if the head exists, if it doesnt exist it means theres no nodes inside our linkedlist. meaning we would set the node to our head. 
            self.head = new_node #sets it here 
        else: #if head does exist 
            current = self.head #current value is set to head 
            while current.next: #while loop runs as long as current is pointing at a valid value 
                current = current.next #continues to update until pointer is pointing at a invalid value 
            current.next = new_node #once loop breaks we add our new node at the end 

    def delete(self, value): 
        if self.head is None: #Checks for our first condition if the list contains a node, which is head
            return #return nothing since there is nothing to delete
        elif self.head.value == value: #checks if the head's value matches the deleted value 
            self.head = self.head.next #removes the head as the pointer is updated to the one after 
            return 
        
        current = self.head 

        while current.next and current.next.value != value: #iterates through the LinkedList to find the node to delete. it ends the loop once the value is found 
            current = current.next 

        if current.next is None: #checks if node is not found in the list 
             print("Value to delete cannot be found")
        else:
                current.next = current.next.next #skips the node over and deletes it 
        
    def get(self, index):
        current = self.head 
        counter = 0
        while current: 
            if counter == index:
                return current.value
            current = current.next
            counter += 1
        raise IndexError("Index out of bounds")  #Raise error if the value we are trying to get is not in our list 


            
