class Node: 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 

class LinkedList: 
    def __init__(self): 
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data,end=' ')
            temp = temp.next

    def atStart(self,new_data):

        new_node=Node(new_data)

        new_node.next=self.head
        
        self.head=new_node

        print("After Insertation")

    def atEnd(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return
        
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    
    def atNode(self,prev_data,new_data):
        
        print("prev data is :",prev_data)
        if prev_data is None:
            print("previous not found")
            return

        new_node=Node(new_data)
        # curr=self.head
        # print("curr data is:",curr.data)
        
        # while curr.next!=prev_data:
        #     curr=curr.next
        #     print(curr.data)
        #     # print(curr.data,"and",prev_data)

        new_node.next=prev_data.next
        prev_data.next=new_node


    def reverse(self):
        prev=None
        curr=self.head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    # def atStartDelete(self):
    #         if self.head is None:
    #             print("Linked list is empty")
    #         else:
    #             curr=self.head
    #             self.head=curr.next
    #             curr.next=None

    def deleteNode(self, key): 
        temp = self.head 

        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
  
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
 
        if(temp == None): 
            return 

        prev.next = temp.next 
        temp = None 

    # def deleteAtTail(self):   
    #     temp = self.head
    #     while(temp.next is not None):
    #         temp = temp.next
    #     temp.next = None


class Test():
    pass
        

if __name__=='__main__': 

    llist = LinkedList() 

    
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 



    llist.head.next = second;
    second.next = third

    llist.deleteNode(3)

    print("after delete")

    llist.printList()
    print()

    
    llist.reverse()

    print("After reverse")

    llist.printList()

    llist.atStart(7)
    llist.atEnd(9)
    llist.atEnd(10)
    llist.atStart(6)
    print()
    llist.atNode(llist.head.next,18)
    llist.printList()
