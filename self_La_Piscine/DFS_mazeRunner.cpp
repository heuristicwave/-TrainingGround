#include <iostream>
using namespace std;

int map[10][10];
int check[10][10];
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int cnt = 0;

void DFS(int x, int y){
	int xx, yy;
	
	if(x == 7 && y == 7){	// destination
		cnt++;
	} else{
		for(int i=0; i<4; i++){
			xx = x + dx[i];
			yy = y + dy[i];
			if(xx<1 || xx>7 || yy<1 || yy>7)	continue;
			if(map[xx][yy] == 0 && check[xx][yy]==0){
				check[xx][yy] = 1;	// check the way past
				DFS(xx, yy);
				check[xx][yy] = 0;
			}
		}
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	int i, j;
	
	for(i=1; i<=7; i++){
		for(j=1; j<=7; j++){
			cin >> map[i][j];
		}
	}	
	
	check[1][1] = 1;	// !!!! start point check !!!!
	DFS(1, 1);	// start location
	
	cout << cnt << endl;
	
	return 0;
}
