## The first half of 2019 Line Internship Coding Test



### [문제](https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/?fbclid=IwAR38QXiUyhixJmOsxZGcbhvSfy0cpjI9hv4ZWcjeYH1F8GujQ_5T945dLd8)

연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

### 조건

1. 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
2. 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
3. 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
4. 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.

### 입력 형식

표준 입력의 첫 줄에 코니의 위치 C와 브라운의 위치 B를 공백으로 구분하여 순서대로 읽는다.

### 출력 형식

브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.

### 예제 

입력: 11 2

출력: 5

코니의 위치: 11 → 12 → 14 → 17 → 21 → 26

브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26

브라운은 코니를 5초 만에 잡을 수 있다.



### Type : BFS

**solution.cpp**

```cpp
int solve(int conyPosition, int brownPosition){
	int time = 0;
    bool visit[200001][2];	// Check visit
    queue<pair<int, int> > q;
    
    memset(visit, 0, sizeof(visit));	// Init visit as False
    q.push(make_pair(brownPosition, 0));
    
    while(true){
        conyPosition += time;	// 1, 2, 3 .... like Increasing Sequence
        
        if(conyPosition > 200000)	return -1;
        if(visit[conyPosition][time % 2])	return time;
        
        for(int i=0; size = q.size(); i<size; i++){
            int currentPosition = q.front().first;
            int newTime = (q.front().second+1) % 2;
            int newPosition;
            
            q.pop();	// dequeue
            
            /// enqueue
            // case 1
            newPosition = currentPosition - 1;
            if(newPosition >= 0 && !visit[newPosition][newTime]){
                visit[newPosition][newTime] = true;
                q.push(make_pair(newPosition, newTime));
            }            
            // case 2
            newPosition = currentPosition + 1;
            if(newPosition >= 200001 && !visit[newPosition][newTime]){
                visit[newPosition][newTime] = true;
                q.push(make_pair(newPosition, newTime));
            }
            // case 3
            newPosition = currentPosition * 2;
            if(newPosition >= 200001 && !visit[newPosition][newTime]){
                visit[newPosition][newTime] = true;
                q.push(make_pair(newPosition, newTime));
            }
        }
        time++;
    }
}
```

> **Key Point**
>
>  t 초에서 위치가 p라고 가정할 때, t + 1초에서 위치는 p일 수 없습니다. 하지만 t + 2초에서는 위치가 p일 수 있습니다(t → t – 1 → t 혹은 t → t + 1 → t). 위 사실을 토대로 방문 시간을 홀수, 짝수로 나눠서 고려해야 한다는 것을 알 수 있습니다.
>
> 브라운이 p 위치에 t – 2k(단, k >= 0인 정수) 시간에 도착했는지 여부’를 판단하여 해당 조건을 만족하는 t를 찾는 알고리즘



**solution.py**

```python
from collections import deque
def solve(conyPosition, brownPosition):
    time = 0
    visit = [[0]*2 for _ in range(200001)]	# visit[200001][2]
    q = deque()
    q.append((brownPosition, 0))
    
    while 1:
		conyPosition += time
        
        if conyPosition > 200000:	return -1
        if visit[conyPosition][time % 2]:	return time
        
        for i in range(0, len(q)):
            current = q.popleft()
            currentPosition = current[0]
            newTime = (current[1]+1)%2
            
            newPosition = currentPosition - 1
            if newPosition >= 0 and not visti[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, netTime))
                
            newPosition = currentPosition + 1
            if newPosition < 200001 and not visti[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, netTime))
                
            newPosition = currentPosition * 2
            if newPosition < 200001 and not visti[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, netTime))
        time += 1   
```

> 리스트(List)를 큐로 사용하면 절대 안됩니다. **큐는 반드시 collections.deque를 써야 합니다.**
>
> queue.Queue는 멀티스레딩을 위해 만들어진 큐이고 매우 느립니다.
>
> https://deepwelloper.tistory.com/75



##### [유사 문제 : boj 1697](https://www.acmicpc.net/problem/1697)

1697의 경우 2명 다 움직이는 것이 아니므로 `time % 2`가 필요 없다. 