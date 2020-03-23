#include <iostream>
#include <queue>
using namespace std;

int tomato[1001][1001];
int d[1001][1001];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};


int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
//	freopen("input.txt", "rt", stdin);
	
	int s, e, i, j;
	queue<pair <int, int> > q;
	int res = 0;
	
	cin >> s >> e;
	
	for(i=1; i<=e; i++){
		for(j=1; j<=s; j++){
			cin >> tomato[i][j];
			d[i][j] = -1;
			if(tomato[i][j] == 1){
				q.push({i, j});
				d[i][j] = 0;
			}
		}
	}
	
	while(!q.empty()){
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(i=0; i<4; i++){
			int cur_x = x  + dx[i];
			int cur_y = y  + dy[i];
			if(cur_x < 1 || cur_x > e || cur_y < 1 || cur_y > s)	continue;
			// Unripe tomatoes and unvisited places
			if(tomato[cur_x][cur_y] == 0 && d[cur_x][cur_y] == -1){
				d[cur_x][cur_y] = d[x][y] + 1;	// day accumlate
				q.push({cur_x, cur_y});
			}
		}
	}
	
	for(i=1; i<=e; i++){
		for(j=1; j<=s; j++){
			res = max(res, d[i][j]);
		}
	}
	
	// All tomatoes unripe
	for(i=1; i<=e; i++){
		for(j=1; j<=s; j++){
			if (tomato[i][j] == 0 && d[i][j] == -1)	res = -1;
		}
	}
	
	cout << res;
	return 0;
}
