#判断链表里是否有环


#一种办法是 我把遍历过的节点存set里 只要我再次在set里找到 那么久包含环
#正常退出不包含环
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        info = set() #存走过的节点
        ret = head
        while ret:
            if ret in info:
                return True
            info.add(ret)
            ret = ret.next
        
        return False


#另一种做法是 快慢指针 
#快的走两步 慢的走一步
#如果有环 快的一定会在某个时候与慢的重合
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False