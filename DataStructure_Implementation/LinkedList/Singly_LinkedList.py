class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.val = 0
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.size == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            newHead = ListNode(val)
            newHead.next = self.head
            self.head = newHead
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.size == 0:
            self.head = self.tail = ListNode(val)
        else:
            node = ListNode(val)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node = self.getNodeAtIndex(index)
            newNode = ListNode(val)
            newNode.next = node.next
            node.next = newNode
            self.size += 1

    def getNodeAtIndex(self, index):
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        return cur

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            if self.head is None:
                self.tail = None
        else:
            node = self.getNodeAtIndex(index)
            deleted = node.next
            node.next = node.next.next
            deleted.next = None
            if index == self.size - 1:
                self.tail = node
        self.size -= 1
