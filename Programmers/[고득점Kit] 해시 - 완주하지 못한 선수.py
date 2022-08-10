def solution(participant, completion):
    
    # 먼저 정렬 후 어긋나는 부분을 찾아서 리턴

    sortedParticipant = sorted(participant)
    sortedCompletion = sorted(completion)
    
    for i in range(len(sortedParticipant)):
        if sortedParticipant[i] == sortedCompletion[i]:
            continue
        else:
            return sortedParticipant[i]