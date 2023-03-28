""" 
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ The LinkedList code from before is provided below.                         │
  │ Add three functions to the LinkedList.                                     │
  │ "get_position" returns the element at a certain position.                  │
  │ The "insert" function will add an element to a particular                  │
  │ spot in the list.                                                          │
  │ "delete" will delete the first element with that                           │
  │ particular value.                                                          │
  │ Then, use "Test Run" and "Submit" to run the test cases                    │
  │ at the bottom.                                                             │
  │                                                                            │
  └────────────────────────────────────────────────────────────────────────────┘
 """


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current.next:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            current.next = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position == 0:
            return self.head
        count = 1
        current = self.head
        while current:
            if count == position:
                return current
            current = current.next
            count += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return
        count = 1
        current = self.head
        while current:
            if count == position-1:
                temp_loc = current.next
                current.next = new_element
                current.next.next = temp_loc
                return
            current = current.next
            count += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
# Should also print 3

# Test insert
ll.insert(e4, 3)
# Should print 4 now

# # Test delete
ll.delete(1)
# Should print 2 now
# Should print 4 now
# Should print 3 now
