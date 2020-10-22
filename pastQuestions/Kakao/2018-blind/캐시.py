'''
Error Handling
- 1. Cash Hit 상태에서 다음에 지워질 Key가 바뀌는 경우 (tc : 15)
- 2. 캐시 등록과정에서 중복 등록 제거, 여기서도 error 1 고려 (tc : 16, 19)
- 3. Cache Hit 최신화 작업 (tc : 11, 18, 20) 

# Error 3 : Before 
Cache가 [Jeju, Pangyo, NewYork] 일 때,
Pangyo가 i로 들어오면 Jeju를 popleft하고 append 하면서 순서 침해

while True:
    tmp = cache.popleft()
    if tmp == i:
        break
    cache.append(tmp)

# Error 3 : After
cache.remove(city)

모범답안 : https://github.com/onlybooks/algorithm-interview/blob/master/appendix-B/3.py
'''
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    def cacheUpdate(city):
        cache.remove(city)
        cache.append(city)

    for i in cities:
        i = i.lower()
        if len(cache) != cacheSize:
            if i in cache:  # 캐시 중복 등록 피하기
                cacheUpdate(i)
                answer += 1
                print(cache)
            else:
                answer += 5
                cache.append(i)
            continue

        if i in cache:
            cacheUpdate(i)
            answer += 1
        else:
            cache.popleft()
            answer += 5
            cache.append(i)
        # print(cache, answer)    # for debug

    return answer
