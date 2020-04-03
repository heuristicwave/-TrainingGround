# ACMICPC

## 삼성 SW 역량 테스트 기출

### [퇴사](https://www.acmicpc.net/problem/14501)

[어떻게 풀 수 있을까?](https://www.youtube.com/watch?v=VEbh7lCu7Ic&list=PLdHw4xVmS1psZInw07xdgZmnQcIrXru8J&index=8)

```c++
DP[day] = max(DP[day + 1], DP[day + T[day]] + P[day])
```

day에서 시작해서 퇴사일까지 최대 값을 DP[day]에 저장

DP[day] 는 두가지 중에 최대값을 저장

- 오늘의 스케쥴 진행 : DP[day + T[day]] + P[day]
- 오늘의 스케쥴 미진행 : DP[day + 1]



```c
solve(0) = max(solve(1), solve(3) + 10) // 1일차, solve(1) : 미진행, solve(3) + 10 : 진행 
	solve(1) = max(solve(2), solve(6) + 20)
		solve(2) = max(solve(3), solve(3) + 10)
			solve(3) = max(solve(4), solve(4) + 20)
    			solve(4) = max(solve(5), solve(6) + 15)
    				solve(5) = max(solve(6), solve(8) + 40)	// solve(7) 이상은 없음
    					solve(6) = max(solve(7), solve(8) + 200)
    						solve(7) = 0
    						solve(8) = -00 // minus infinity
// return : 0-0-15-35-45-45-45
```



#### 필요 지식

[C++, The difference between pointer and reference](https://gracefulprograming.tistory.com/11)