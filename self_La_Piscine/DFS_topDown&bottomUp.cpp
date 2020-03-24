#include <iostream>
using namespace std;

int dy[50];

// Top-Down, Memoization
int DFS(int n){
	if(dy[n] > 0)	return dy[n];	// Using previously obtained values
	if(n==1 || n==2)	return n;
	else return dy[n] = DFS(n-1) + DFS(n-2);
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n;
	cin >> n;
	
	cout << DFS(n);	
	
	/// Ignition - Bottom Up
//	dy[1] = 1;
//	dy[2] = 2;
//	
//	for(int i=3; i<=n; i++){
//		dy[i] = dy[i-2] + dy[i-1];
//	}
//	
//	cout << dy[n];
	
	return 0;
}
