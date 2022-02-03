import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return count

    while len(scoville) > 1:
        count += 1
        least_not_hot = heapq.heappop(scoville)
        second_not_hot = heapq.heappop(scoville)
        mix = least_not_hot + second_not_hot * 2

        min_scoville = min(mix, scoville[0]) if scoville else mix

        if min_scoville >= K:
            return count

        heapq.heappush(scoville, mix)
    return -1


solution([1, 2, 3, 9, 10, 12], 7)
print(solution([1, 2, 3, 9, 10, 12], 2000000000))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.52ms, 10.2MB)
# 테스트 7 〉	통과 (0.76ms, 10.3MB)
# 테스트 8 〉	통과 (0.06ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.36ms, 10.2MB)
# 테스트 11 〉	통과 (0.27ms, 10.3MB)
# 테스트 12 〉	통과 (0.81ms, 10.2MB)
# 테스트 13 〉	통과 (0.46ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.59ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (188.73ms, 16.3MB)
# 테스트 2 〉	통과 (420.17ms, 22MB)
# 테스트 3 〉	통과 (1987.59ms, 49.9MB)
# 테스트 4 〉	통과 (160.01ms, 14.9MB)
# 테스트 5 〉	통과 (1798.75ms, 51.8MB)
