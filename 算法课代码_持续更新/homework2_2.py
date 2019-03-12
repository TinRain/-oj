class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next


class Palindrome:
    def rev(self, head):
        if None == head or None == head.next:
            return head
        pcur = head
        pnew = None
        pnext = None
        while pcur:
            pnext = pcur.next
            pcur.next = pnew
            pnew = pcur
            pcur = pnext
        return pnew

    def isPalindrome(self, head):
        if None == head or None == head.next:
            return True
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        slow = self.rev(slow)
        while slow:
            if slow.val != head.val:
                return False
            head = head.next
            slow = slow.next
        return True


while True:
    try:
        list_input = input().split()
        N = int(list_input[0])
        array = list_input[1:]

        linkedList = LinkedList()
        linkedList.initList(array)

        S = Palindrome()
        p = S.isPalindrome(linkedList.head)
        if p:
            print('true')
        else:
            print('false')
    except EOFError:
        break


