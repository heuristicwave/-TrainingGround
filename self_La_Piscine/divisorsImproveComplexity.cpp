#include <cstdio>

int cnt[500001];
int main() {
	freopen("input.txt", "rt", stdin);
	
	int n;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		// Improve time complexity, using multiple
		for(int j=i; j<=n; j=j+i){
			cnt[j]++;
		}
	}
	
	for(int i=1; i<=n; i++){
		printf("%d ", cnt[i]);
	}
	
	return 0;
}
