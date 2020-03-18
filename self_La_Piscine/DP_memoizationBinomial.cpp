#include <iostream>
#include <algorithm>
using namespace std;

int dy[21][21];

int DFS(int n, int r){
	if(dy[n][r]>0)	return dy[n][r];	// cache hit !!
	if(n==r || r==0)	return 1;
	else	return dy[n][r] = DFS(n-1, r-1)+DFS(n-1, r);
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, r;
	cin >> n >> r;
	
	cout << DFS(n, r);
	
	return 0;
}
