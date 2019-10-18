"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        # Swap previous and next
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        # Create a new node for the head
        new_node = ListNode(value, None, self.head)

        # Test for empty nodes for both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Create a new node before the current head
        else:
            # Current head.prev points to the new node
            self.head.prev = new_node
            # Set head to new node
            self.head = new_node
        
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # Save the value before deleting
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):

        # Create a new node for the tail
        new_node = ListNode(value, self.tail, None)

        # Test for empty nodes for both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Create a new node after the current tail
        else:
            # Current tail.next points to the new node
            self.tail.next = new_node
            # Set the tail to new node
            self.tail = new_node
        
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Save the value before deleting
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # Return nothing if node is itself
        if node is self.head:
            return
        # Save the value to add later
        value = node.value
        # Delete the node or else we'll have a duplicate
        self.delete(node)
        # Add to head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Return nothing if node is itself
        if node is self.tail:
            return
        # Save the value to add later
        value = node.value
        # Delete the node or else we'll have a duplicate
        self.delete(node)
        # Add to tail
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1

        # There's only 1 node so set it to None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            # Set the head to the next node
            self.head = node.next
            # Delete the node and reset meta data of the pointers
            node.delete()
        elif node is self.tail:
            # Set the tail to the previous node
            self.tail = node.prev
            # Delete the node and reset meta data of the pointers
            node.delete()
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # If we have empty nodes
        if not self.head:
            return None
        
        max_val = self.head.value
        current = self.head

        # Iterate through the nodes and save the max value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
