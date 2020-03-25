#include <iostream>
using namespace std;

int map[21][21];
int dy[21][21];	// memoization

int DFS(int x, int y){
	if(dy[x][y]>0)	return dy[x][y];	// memoization
	if(x==1 && y==1)	return map[1][1];
	else{
		// 2D array edge boundary processing
		if(y==1)	return dy[x][y] = DFS(x-1, y)+map[x][y];
		else if(x==1)	return dy[x][y] = DFS(x, y-1)+map[x][y];
		// Not edge
		else return dy[x][y] = min(DFS(x-1, y), DFS(x, y-1))+map[x][y];
	}
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, i, j;
	cin >> n;
	
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			cin >> map[i][j];
		}
	}

	cout << DFS(n, n);
	
	return 0;
}
