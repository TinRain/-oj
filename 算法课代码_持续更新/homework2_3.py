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


def reverseKNode2(head, k):
    def reverse2(head, left, right):
        pre = None
        start = head
        while head != right:
            next = head.next
            head.next = pre
            pre = head
            head = next
        if left != None:
            left.next = pre
        start.next = right

    if head == None or head.next == None or k < 2:
        return head
    pre = None
    cur = head
    count = 0
    while cur != None:
        count += 1
        next = cur.next
        if count == k:
            start = head if pre == None else pre.next
            head = cur if pre == None else head
            reverse2(start, pre, next)
            pre = start
            count = 0
        cur = next
    return head


while True:
    try:
        list_input = input().split()
        N = int(list_input[0])
        array = list_input[1:-1]
        K = int(list_input[-1])
        linkedList = LinkedList()
        linkedList.initList(array)
        node = reverseKNode2(linkedList.head, K)
        s = ''
        while node:
            s = s + node.val + ' '
            node = node.next
        print(s.strip())
    except EOFError:
        break