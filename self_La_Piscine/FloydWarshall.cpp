#include <iostream>
#include <vector>
using namespace std;

// int map[201][201] = { M, }; // 2d vector is better 

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("input.txt", "rt", stdin);
	
	int n, m, i, j, k;
	int from, to, cost;
	cin >> n >> m;	
	
	// 	Create 2D distant vector. (5000 role is 'M')
	vector<vector<int> > dis(n+1, vector<int>(n+1, 5000));
	
	for(i=1; i<=n; i++)	dis[i][i] = 0;	// node to node, self
	for(i=1; i<=m; i++){
		cin >> from >> to >> cost;
		dis[from][to] = cost;
	}
	
	// Using DP strategy => Floyd Warshall Algorithm
	for(k=1; k<=n; k++){
		for(i=1; i<=n; i++){
			for(j=1; j<=n; j++){
				// dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
				if(dis[i][j]>dis[i][k]+dis[k][j]){
					dis[i][j] = dis[i][k] + dis[k][j];
				}
			}
		}
	}
	
	// Print Output
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			if(dis[i][j] == 5000){
				cout << "M ";
			} else	cout << dis[i][j] << " ";
		}
		cout << endl;
	}	
		
	return 0;
}
