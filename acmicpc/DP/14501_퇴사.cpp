#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int n;
int T[15], P[15];
int cache[15];	// for DP

int solve(int day) {
	if (day > n)	return -987654321;	// like minus limit
	if (day == n)	return 0;	// exit

	int& ret = cache[day];
	if (ret != -1)	return ret;	// If you didn't get it before

	ret = max(solve(day + 1), solve(day + T[day]) + P[day]);
	return ret;
}

int main() {
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &T[i], &P[i]);
		cache[i] = -1;	// init cache
	}

	int ret = solve(0);
	printf("%d\n", ret);
	return 0;
}