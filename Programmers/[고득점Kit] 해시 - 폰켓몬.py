def solution(nums):
    
    # 유일한 원소들을 뽑음
    numSet = set(nums)
    uniqueList = list(numSet)
    
    # 유일한 원소들의 갯수가 N/2보다 크거나 같으면 최대 N/2 만큼 다양하게 뽑을 수 있음.
    if len(uniqueList) >= len(nums)/2:
        return len(nums)/2
    # 그렇지 않고 N/2보다 작으면, 유일한 원소의 갯수만큼 다양하게 뽑을 수 있음.
    else:
        return len(uniqueList)
    
    return False