from collections import deque
# double-ended queue

# 벡터 합 계산
def vecAdd(vecA, vecB):
    vecSum = deque([])
    if len(vecA) != len(vecB):
        return "Error"
    for idx, a in enumerate(vecA):
        vecSum.append(vecB[idx] + a)
    return vecSum

# 첫 번째부터 몇번 째까지 100보다 큰 지 리턴
def continuousOver100Num(progDeq):
    
    if len(progDeq) == 0:
        return -1
    
    for idx, p in enumerate(progDeq):
        if p < 100:
            return idx
        else:
            continue

    return len(progDeq)

def solution(progresses, speeds):
    
    # 덱으로 바꿔줌
    progressesDeq = deque(progresses)
    speedsDeq = deque(speeds)
    
    end = False
    answer = []
    while(not end):

        updatedProgressesDeq = vecAdd(progressesDeq, speedsDeq) # 최초 프로그레스 진행
        contNum = continuousOver100Num(updatedProgressesDeq) # 최초 프로그레스 계산

        if contNum > 0: # 맨 앞에거부터 끝난게 있으면
            for i in range(contNum): # 그 수만큼 반복하여 popleft 시킴.
                updatedProgressesDeq.popleft()
                speedsDeq.popleft()
            answer.append(contNum) # 답을 위한 return 값에 추가

            progressesDeq = updatedProgressesDeq # 최초값 수정
            
            if len(updatedProgressesDeq) == 0: # 모든 progresses를 다 popleft 시켰으면 끝냄
                end = True

        else: # 맨 앞부터 끝난거 없으면
            progressesDeq = updatedProgressesDeq # 최초값 업데이트하여 반복
            continue

    return answer