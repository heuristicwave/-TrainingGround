#include <iostream>
using namespace std;

int n, condition;
int cnt = 0;
int a[11];	// array containing elements
int path[11]; // show elements that satisfies the condition

void DFS(int L, int sum){	
	if(L==n+1){
		if(sum == condition){
			cnt++;
			for(int i=1; i<L; i++){
				cout << path[i];
			}
			cout << endl;
		}	
	}
	else {	
		path[L] = a[L];	
		DFS(L+1, sum+a[L]);	// level ++, Use element to add value
		path[L] = -a[L];
		DFS(L+1, sum-a[L]);	// level ++, Use element to sub value
		path[L] = 0;
		DFS(L+1, sum);	// level ++, Not change
	}
}

int main() {
	//freopen("input.txt", "rt", stdin);
	
	cin >> n >> condition;
	for(int i=1; i<=n; i++){
		cin >> a[i];
	}	
	
	DFS(1, 0);	// parameter : level 1, sum of elements
	
	if(cnt == 0)	cout << -1 << endl;
	else	cout << cnt << endl;
	
	return 0;
}
