# 이진탐색 (binary Search) - 1
"""
n = 원소갯수 (10)
target = 찾고자하는 값 (7) 
array = 숫자 리스트 (1 3 5 7 9 11 13 15 17 19)
"""

#재귀함수 이용
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    
    else:
        return binary_search(array, target, mid+1, end)

def solution():
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소가 존재하지 않습니다")
    else:
        print(result + 1, "번째 원소입니다.")

# solution()

"""
**왕초보질문주의**
**부끄럽지만일단질문**

binary search 
n = 원소갯수 (10)
target = 찾고자하는 값 (7) 
array = 숫자 리스트 (1 3 5 7 9 11 13 15 17 19)

while문 돌릴때요
첫번째 if문에서 return mid 값이 7이나왔다고 하면,
맨 하단 return None은 실행 안되나요?

return은 딱 한번만 실행되면 그 나머지는 무시하나요?
왠지 mid값 정해졌는데 아래 None으로 다시 덮어씌워질까봐 두려운 1인 

답변:

울고싶지않아 — Today at 11:32 PM
그럼 하진님 리턴하면 함수 끝나요?
while문 아직 돌아야해도 ?

코테 공부 더 빡시게... — Today at 11:32 PM
네네
while이고 뭐고 다 끝나요

"""
def binary_search(array, target, start, end):
    while start < end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n, target = 10, 7
array = [1, 3, 5, 7 ,9, 11, 13, 15, 17 ,19]
print(binary_search(array, target, 0, 6)+1)



        

