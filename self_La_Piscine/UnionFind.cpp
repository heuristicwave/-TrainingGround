#include <iostream>
#include <algorithm>
using namespace std;

int unf[1001];	// initial array

int Find(int v){
	if(v==unf[v])	return v;
	else return Find(unf[v]);
	// !! Path compression !!
	// return unf[v] = Find(unf[v]);
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
	
	int i, j, n, m;
	int a, b, fa, fb;
	
	// Get input info
	cin >> n >> m;	
	for(i=1; i<=n; i++){
		unf[i] = i;
	}
	
	// Create Union
	for(i=1; i<=m; i++){
		cin >> a >> b;
		Union(a, b);
	}
	
	// Friend Check
	cin >> a >> b;
	fa = Find(a);
	fb = Find(b);
	if(fa == fb)	cout << "YES" << endl;
	else cout << "NO" << endl;	
	
	return 0;
}
