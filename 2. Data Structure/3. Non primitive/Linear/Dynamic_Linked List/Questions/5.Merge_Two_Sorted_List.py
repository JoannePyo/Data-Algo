'''
Merge Two Sorted Lists (Easy)

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
'''

'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

class ListNode(object):     
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
'''
time complexity: O(n + m) 여기서 n과 m은 각각 두 개의 입력 리스트인 list1과 list2의 길이입니다. 이는 두 리스트를 한 번씩만 순회하면서 병합하기 때문에 선형 시간이 소요됩니다.
space complexity: O(n + m) 재귀 호출 스택에는 최대 n + m개의 호출이 쌓일 수 있습니다. 또한, 재귀 호출에 따라 새로운 ListNode 인스턴스가 생성되므로, 두 리스트의 길이의 합에 비례하는 공간이 소비됩니다.
'''

# 주어진 입력에 대한 테스트
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)
