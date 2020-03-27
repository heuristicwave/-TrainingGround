#include<iostream>
#include<queue>
#include<vector>
using namespace std;
int map[21][21], ch[21][21];
int dx[4]={-1, 0, 1, 0};
int dy[4]={0, 1, 0, -1};

struct State {
	int x, y, dis;
	// Constructor
	State(int a, int b, int c){
		x = a;
		y = b;
		dis = c;
	}
	// Minimum heap
	bool operator< (const State &b) const {
		// If the distances are not the same, make the minimum heap by distance
		if(dis!=b.dis) return dis > b.dis;
		if(x!=b.x)	return x>b.x;	// Top priority
		else return y > b.y;	// Leftmost priority
	}
};

struct Lion{
	int x, y, s, ate;
	void sizeUp(){
		ate = 0;
		s++;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input.txt", "rt", stdin);
	
	int n, i, j;
	int res = 0;
	priority_queue<State> Q;
	
	Lion simba;	// create lion struct
	cin >> n;
	
	// Get info
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			cin >> map[i][j];
			if(map[i][j]==9){
				simba.x=i;
				simba.y=j;
				map[i][j]=0;
			}
		}
	}
	
	// Push state struct info
	Q.push(State(simba.x, simba.y, 0));
	simba.s = 2;
	simba.ate = 0;
	
	while(!Q.empty()){
		State tmp = Q.top();
		Q.pop();
		int x = tmp.x;
		int y = tmp.y;
		int z = tmp.dis;
		// Meets hunting conditions
		if(map[x][y] !=0 && map[x][y] < simba.s){
			simba.x = x;
			simba.y = y;
			simba.ate++;
			if(simba.ate >= simba.s)	simba.sizeUp();
			map[x][y] = 0;	// hunt complete
			// You can come back after the hunt, so remove your visit history
			for(i=1; i<=n; i++){
				for(j=1; j<=n; j++){
					ch[i][j] = 0;				
				}
			}
			while(!Q.empty()) 	Q.pop();
			res = tmp.dis;
		}
		for(i=0; i<4; i++){
			int xx = x + dx[i];
			int yy = y + dy[i];
			if(xx<1 || xx>n || yy<1 || yy>n || map[xx][yy]>simba.s || ch[xx][yy]>0)	continue;
			Q.push(State(xx, yy, z+1));
			ch[xx][yy] = 1;
		}
	}
	
	cout << res;
	return 0;
}
