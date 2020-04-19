n, m = map(int, input().split())
videos = list(map(int, input().split()))


def count(dvdSize):
    dvdNum = 1  # First, NEED one dvd
    total = 0   # total of videos

    for i in range(n):
        if total+videos[i] > dvdSize:
            dvdNum += 1
            total = videos[i]
        else:
            total += videos[i]
    return dvdNum


start, end = 1, 0   # start는 최솟값 1, end는 0으로 초기화
max_playtime = 0    # max_playtime이 없어도 잘 동작함 속도를 높이기 위해 만듬
result = 0

for i in range(n):
    end += videos[i]
    if videos[i] > max_playtime:
        max_playtime = videos[i]


while start <= end:
    #print(f'start:{start} / end:{end}')
    mid = (start + end) // 2    # dvd size
    # print(mid)

    if mid >= max_playtime and count(mid) <= m:
        end = mid - 1
        result = mid  # If over, roll back
    else:
        start = mid + 1

print(result)
