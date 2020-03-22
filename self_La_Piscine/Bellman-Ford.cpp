#include <iostream>
#include <vector>
using namespace std;

int dist[101];

struct Edge{
	int s;
	int e;
	int val;
	Edge(int a, int b, int c){
		s = a;
		e = b;
		val = c;
	}
};

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int i, j, n, m;
	int a, b, c;
	vector<Edge> Ed;
	cin >> n >> m;
	
	for(i=1; i<=m; i++){
		cin >> a >> b >> c;
		Ed.push_back(Edge(a, b, c));
	}
	
	// Reset to extreme
	for(i=1; i<=n; i++){
		dist[i] = 2147000000;
	}
	
	dist[1] = 0; 	// Rule!
	
	// Bellman-Ford Algorithm
	for(i=1; i<n; i++){
		for(j=0; j<Ed.size(); j++){
			int s = Ed[j].s;
			int e = Ed[j].e;
			int w = Ed[j].val;
			if(dist[s] != 2147000000 && dist[s] + w < dist[e]){
				dist[e] = dist[s] + w;
			}
		}
	}
	
	// Verifying that a negative cycle exists
	for(j=0; j<Ed.size(); j++){
		int u = Ed[j].s;
		int v = Ed[j].e;
		int w = Ed[j].val;
		if(dist[u] != 2147000000 && dist[u] + w < dist[v]){
			cout << "-1" << '\n';
			return 0;
		}				
	}
	
	cout << dist[n] << '\n';
	return 0;
}
