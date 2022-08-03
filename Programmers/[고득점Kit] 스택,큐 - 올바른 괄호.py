from collections import deque

def symmetry(sDeq):
    lCnt = 0
    rCnt = 0    
    for i in sDeq:
        if i == '(':
            lCnt += 1
        else:
            rCnt += 1
            
    if lCnt != rCnt:
        return False
    else:
        return True

def solution(s):
    
    # 왼쪽 괄호만 담는 box를 구현하여
    # sDeq에 오른쪽 괄호들과 만나 모두 사라지면 정상괄호임을 이용
    
    sDeq = deque(s) # str을 deq으로 변환
    box = deque([]) # 담을 box을 deq으로 구현
    
    if not symmetry(sDeq): # 대칭성을 이루지 않으면 False
        return False
    
    
    while True: # 대칭성을 이뤘을 때
        
        if sDeq[0] == '(': # 왼쪽 괄호는 다 들여보내줌
            box.append(sDeq.popleft())
            
        else: # 오른쪽 괄호가 나왔을 때
            if len(box) == 0: # box가 비었으면 False
                return False
            elif box[-1] == ')': # box 우측에 오른쪽 괄호가 들었으면 False
                return False
            elif box[-1] == '(': # box 우측에 왼쪽 괄호가 들었으면 둘 다 빼줌
                box.pop()
                sDeq.popleft()
                
                if len(box) == len(sDeq) == 0: # 둘 다 빼고 둘 다 완전히 비었으면 정상 괄호
                    return True
                
        