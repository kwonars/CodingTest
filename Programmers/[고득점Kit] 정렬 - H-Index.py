def solution(citations):
    
    # 내림차순 정렬 후 하나씩 h 인덱스 조건이 되는지를 확인.
    # for문을 n회 돌 때 n-1번째 or n+1번째를 출력하는 로직을 주의해야함.
    # 이 경우 1번째와 n번째의 추가 조건문이 붙어야 함.
    
    # 내림차순 정렬
    sortedCitations = sorted(citations, reverse=True)

    # 1~n 편 확인
    n = len(sortedCitations)
    for idx, c in enumerate(sortedCitations):
        if c >= idx+1:
            if n == idx+1: # 검사하는 원소가 맨 끝까지 갔을 때
                return n
            else:
                continue
        else:
            answer = idx
            return answer
    