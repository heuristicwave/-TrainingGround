#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int unf[1001];	// initial array

struct Edge{
	int v1;
	int v2;
	int val;
	Edge(int a, int b, int c){
		v1 = a;
		v2 = b;
		val = c;
	}
	// sort ascending by value
	bool operator<(Edge &b){	
		return val<b.val;
	}
};

int Find(int v){
	if(v==unf[v])	return v;
	else return unf[v] = Find(unf[v]);	// !! Path compression !!
}

void Union(int a, int b){
	a = Find(a);
	b = Find(b);
	if(a!=b) unf[a] = b;	// Connect A & B
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("input.txt", "rt", stdin);
	
	vector<Edge> Ed;
	int i, j, n, m;
	int a, b, c;
	int cnt = 0, res = 0;
	int fa, fb;
	
	// Get input info
	cin >> n >> m;	
	// Initialize all vertices as a single set
	for(i=1; i<=n; i++){
		unf[i] = i;
	}
	
	// Create Union
	for(i=1; i<=m; i++){
		cin >> a >> b >> c;
		Ed.push_back(Edge(a, b, c));
	}
	
	sort(Ed.begin(), Ed.end());
	
	for(i=0; i<m; i++){
		fa = Find(Ed[i].v1);
		fb = Find(Ed[i].v2);
		if (fa!=fb){
			res += Ed[i].val;
			Union(Ed[i].v1, Ed[i].v2);
		}
	}
	
	cout << res << '\n';
	return 0;
}
