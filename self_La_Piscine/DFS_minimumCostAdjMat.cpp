#include <iostream>
using namespace std;

int map[30][30];
int check[30];
int n;
int cost = 2147000000;

void DFS(int v, int sum){
	int i;
	if (v == n){
		if(sum < cost)	cost = sum;
	} else {
		for(i=1; i<=n; i++){
			// check possible routes
			if(map[v][i] > 0 && check[i] == 0){
				check[i] = 1;
				DFS(i, sum+map[v][i]);
				check[i] = 0;
			}
		}
	}
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	

	freopen("input.txt", "rt", stdin);
	
	int m, i, from, to, value;
	
	cin >> n >> m;
	
	for(i=1; i<=m; i++){
		cin >> from >> to >> value;
		map[from][to] = value;
	}
	
	check[1] = 1;
	DFS(1, 0);	// param : vertex, sum
	
	cout << cost << endl;
	
	return 0;
}
