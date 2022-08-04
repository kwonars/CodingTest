def solution(array, commands):
    
    # 파이썬 기본 함수를 통해 풀이
    
    answer = []
    for command in commands:
        sortedArray = array[command[0]-1:command[1]]
        sortedArray.sort() # 오름차순 정렬
        answer.append(sortedArray[command[2]-1])
    return answer