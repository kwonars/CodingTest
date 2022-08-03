from collections import deque

# str로 마크한 정수 찾기
def checkStr(deq):
    for i in deq:
        if type('') == type(i):
            return True
        else:
            continue
    return False

# str과 int가 섞인 것 중 Max값 찾기
def getMax(deq):
    max = 0
    for i in deq:
        if max < int(i):
            max = int(i)
    return max


def solution(priorities, location):
    
    # 왼쪽으로 하나씩 뽑아내면서 마크된 값이 언제 출력되는지로 순서 계산
    
    # deq으로 변환
    prioritiesDeq = deque(priorities)
    
    # int를 str로 마크
    prioritiesDeq[location] = str(prioritiesDeq[location])

    answer = 0
    while(True):
        if int(prioritiesDeq[0]) == getMax(prioritiesDeq): # 첫째 원소가 최대값이면
            answer+=1 # 하나 내보낸 것 카운트
            if type(prioritiesDeq[0]) == type(''): # 내보내는 원소가 마크된 값이면 몇 번째 카운트인지 리턴
                return answer
            else: # 내보내는 원소가 마크된 값이 아니면 빼버림
                prioritiesDeq.popleft()
            
        else: # 첫째 원소가 최대값이 아니면
            prioritiesDeq.append(prioritiesDeq.popleft()) # 규칙때로 왼쪽에서 빼서 오른쪽에 넣어줌