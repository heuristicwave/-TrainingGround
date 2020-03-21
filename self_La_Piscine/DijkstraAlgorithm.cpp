#include <iostream>
#include <vector>

#define x first
#define y second

using namespace std;

int ch[30], dist[30]; 	// check, distance
vector<pair <int, int> > map[30];

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, m, a, b, c, min;
	int i, j;
	cin >> n >> m;
	
	for(i=1; i<=m; i++){
		cin >> a >> b >> c;
		// Create direction graph adjacency list
		map[a].push_back(make_pair(b, c));
	}
	
	for(i=0; i<=n; i++) dist[i]=2147000000;
	dist[1] = 0;
	
	for(i=1; i<=n; i++){
		min = 0;
		for (j=1; j<=n; j++){
			if(ch[j]==0 && dist[j] < dist[min]){
				min = j;
			}
		}
		ch[min] = 1;	// after check, start at checked vertical
		for(j=0; j<map[min].size(); j++){
			int v = map[min][j].x;	// vertex from minimum
			// Value at the vertex that can go from minimum
			int cost = map[min][j].y;
			
			// relax~
			if(dist[v] > dist[min] + cost)	dist[v] = dist[min] + cost;
		}		
	}
	
	for(i=2; i<=n; i++){
		if(dist[i] != 2147000000)	cout << i << " : "<< dist[i] << endl;
		else cout << i << " : impossible" << endl;
	}	
	
	return 0;
}
