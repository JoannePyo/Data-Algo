'''
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]

find out common string both list1 and list2
common string with the least index sum = list1[i] and list2[j] then i + j
'''


class Solution(object):
    def findRestaurant(self, list1, list2):

        hashmap = {}
        for i in range(len(list1)):
            hashmap[list1[i]] = i

        res = []
        min_sum = float("inf")
        for j in range(len(list2)):
            if list2[j] in hashmap:
                sum = j+ hashmap[list2[j]]
                if sum < min_sum:
                    min_sum = sum
                    res.append(list2[j])
                elif sum == min_sum:
                    res.append(list2[j])

        # 해쉬맵 초기화
        hashmap = {}
        for i in range(len(list1)):   
            hashmap[list1[i]] = i  
        
        restaurant = [] # 변수: 공통된 식당의 이름을 저장할 빈 리스트를 초기화합니다.

        min_sum = float("inf")  # 무한대 :float("inf") 이렇게 사용함으로써 초기값으로 무한대를 설정합니다.
        
        # 공통된 식당 찾기
        for j in range(len(list2)):   
            if list2[j] in hashmap: #list2의 각 원소를 순회하면서, 해당 원소가 list1의 해시맵에 존재하는지 확인합니다.
                sum = j + hashmap[list2[j]]  #존재한다면, 해당 원소의 인덱스와 list2에서의 인덱스를 더한 값을 sum에 저장합니다. 

                if sum < min_sum:   # sum이 현재까지의 최소 합계 min_sum보다 작으면, 
                    min_sum = sum   # min_sum을 업데이트하고 
                    restaurant.append(list2[j]) # 해당 식당을 추가합니다.
                elif sum == min_sum:             # sum이 min_sum과 같다면,
                    restaurant.append(list2[j])  # restaurant 리스트에 해당 식당을 추가합니다.
        return restaurant #restaurant 리스트에는 공통된 식당 이름이 저장되어 있으며, 이를 반환합니다.

solution = Solution

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
result = solution.findRestaurant(None, list1,list2)
print(result)