from collections import deque

# 0으로 이루어진 bridge를 만듦
def buildBridge(bridgeLength):
    bridge = deque([])
    for i in range(bridgeLength):
        bridge.append(0)
    return bridge

def solution(bridge_length, weight, truck_weights):
    bridge = buildBridge(bridge_length)
    truckDeq = deque(truck_weights)
    
    timeCnt = 0
    totalWeightSum = 0
    while True:
        if len(truckDeq) > 0: # 남은 트럭이 있을 때
            
            # 다음 트럭이 들어올 수 있으면
            if totalWeightSum - bridge[0] + truckDeq[0] <= weight:
                totalWeightSum -= bridge[0]
                bridge.popleft()
                bridge.append(truckDeq.popleft())
                timeCnt += 1
                
                totalWeightSum += bridge[-1]

            else: # 다음 트럭이 들어오지 못하면
                totalWeightSum -= bridge[0]
                bridge.popleft()
                bridge.append(0)
                timeCnt += 1

        else: # 남은 트럭이 없으면

            return timeCnt + bridge_length