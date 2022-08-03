from collections import deque # double-ended queue 활용

# 첫 번째 원소에서 얼마나 멀리 떨어지는지를 계산하는 함수.
def howManyTimes(priceList):
    time = 0
    # 처음부터 탐색
    for idx, i in enumerate(priceList):
        if priceList[0] > i: # 작은 걸 발견했을 때
            time = idx
            return time
        else: # 발견하지 못했을 때
            if len(priceList) == idx+1: # 끝에 도달했을 때
                time = idx
                return time
            else: #끝이 아닐 때
                continue

def solution(prices):

    answer = []
    priceDeq = deque(prices)
    
    # 첫 번째 원소에서 얼마나 떨어져있는지를 구하는 함수 howManyTimes를 구함
    # popleft를 이용하여 howManyTimes에 대입하는 방식으로 계산.
    # a[i:] 류의 코드는 계산이 오래 걸리므로 반복문 내 사용을 금할 것.

    for i in range(len(prices)):
        answer.append(howManyTimes(priceDeq))
        if len(priceDeq) > 0:
            priceDeq.popleft()
        else:
            continue
        
    return answer