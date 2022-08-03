from collections import deque
# double-ended queue 활용

def solution(arr):
    
    # 오른쪽 deque에서 왼쪽 list로 옮겨오는 구조로 진행
    
    deqArr = deque(arr)
    answer = []
    
    # 0일 때 빈 answer 출력
    if len(deqArr) == 0:
        return answer
    
    # 초기값 저장
    answer.append(deqArr.popleft())
    # 초기값 저장 후 끝났을 경우 바로 return
    if len(deqArr) == 0:
        return answer
    
    # 이후 반복 진행
    end = False
    while(not end):
        if answer[-1] == deqArr[0]:
            deqArr.popleft()
            if len(deqArr) == 0:
                end = True
        else:
            answer.append(deqArr.popleft())
            if len(deqArr) == 0:
                end = True
    
    return answer