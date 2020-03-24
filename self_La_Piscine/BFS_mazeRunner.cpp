#include<iostream>
#include<queue>
using namespace std;
int map[30][30];
int dis[10][10];
int dx[4] = {0, 1, 0, -1}; 
int dy[4] = {1, 0, -1, 0};

struct Loc{
	int x;
	int y;
	Loc(int a, int b) {
		x = a;
		y = b;
	}
};

queue<Loc> Q;

int main() {
	freopen("input.txt", "rt", stdin);
	int i, j;
	int n = 7;
	
	for(i = 1; i <= n; i++){
		for(j = 1; j <= n; j++){
			cin >> map[i][j];
		}	
	}
	
	Q.push(Loc(1, 1)); // start point
	map[1][1] = 1;	// start mark !!

	while(!Q.empty()) {
		Loc tmp = Q.front();
		Q.pop();
		for(int i = 0; i < 4; i++) {
			int xx=tmp.x+dx[i];
			int yy=tmp.y+dy[i];
			if(map[xx][yy] == 0 && xx>=1 && xx<=7 && yy>=1 && yy<=7) {
				Q.push(Loc(xx, yy));
				map[xx][yy]= 1;
				dis[xx][yy] = dis[tmp.x][tmp.y]+1;
			}
		}
	}

	cout << dis[7][7];	// print destination
	return 0;
}
