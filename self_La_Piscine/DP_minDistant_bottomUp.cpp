#include <iostream>
using namespace std;

int map[21][21];
int dy[21][21];

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

	// dy consumption	
	for(i=1; i<=n; i++){
		dy[1][i] = dy[1][i-1] + map[1][i];	// right
		dy[i][1] = dy[i-1][1] + map[i][1];	// down
	}

	for(i=2; i<=n; i++){
		for(j=2; j<=n; j++){			
//			if(dy[i][j-1] > dy[i-1][j]){
//				dy[i][j] = dy[i-1][j] + map[i][j];
//			} else {
//				dy[i][j] = dy[i][j-1] + map[i][j];
//			}
			/// Using min algorithm
			dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + map[i][j];
		}
	}
	
	cout << dy[n][n];
	
	return 0;
}
