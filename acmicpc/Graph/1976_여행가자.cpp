#include <iostream>
using namespace std;

int unf[201];
int path[1001];
int map[201][201]={0};

int find(int v){
	if(v==unf[v])	return v;
	else return unf[v] = find(unf[v]);	
}

void fn_union(int x, int y){
	x = find(x);
	y = find(y);
	
	if(x!=y) unf[x] = y;	// connect x & y
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
    
	int n;	// city
	int m;	// planCity
	int i, j;
	cin >> n >> m;

//	Using Vector	
//  unf = vector<int> (N+1,0);
//  path = vector<int> (M+1,0);	
	
	// Create UNF array
	for(i=1; i<=n; i++)	unf[i] = i;
	
	// Create Tree
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			cin >> map[i][j];
			
			if(map[i][j])	fn_union(i, j);
		}
	}
	
	for(i=1; i<=m; i++)	cin >> path[i];
	
    bool check = true;
    for(i=1; i<m; i++){
        if(find(path[i])!=find(path[i+1])){
            check=false;
            break;
        }
    }
    
    if(check)   cout<<"YES"<<endl;
    else cout<<"NO"<<endl;	
	
	return 0;
}
