#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int ch[30];		// check
int dis[30];	// distance

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, m, a, b, x;
	vector<int> map[30];	
	queue<int> Q;
	
	cin >> n >> m;
	
	for(int i=1; i<=m; i++){
		cin >> a >> b;
		map[a].push_back(b);	// a -> b, One-way
	}
	
	Q.push(1);	// Problem condition, starting at 1
	ch[1] = 1;	// first start node check
	
	while(!Q.empty()){
		x = Q.front();1
		Q.pop();	// deqeue
		for(int i=0; i<map[x].size(); i++){
			if(ch[map[x][i]] == 0){
				ch[map[x][i]] = 1;
				// enqeue the visited node
				Q.push(map[x][i]);	// connect the next link
				// Add 1 to the previous one to increase
				dis[map[x][i]] = dis[x] + 1;
			}
		}
	}
	
	for(int i=2; i<=n; i++){
		cout << i << ':' << dis[i] << endl;
	}
	
	return 0;
}
