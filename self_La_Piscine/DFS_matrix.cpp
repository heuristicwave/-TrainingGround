#include <iostream>
using namespace std;

int node;
int map[21][21];
int check[30];
int cnt = 0;

void DFS(int v){
	if(v == node){
		cnt++;	
	} else{
		for(int i=1; i<=node; i++){
			if(map[v][i] == 1 && check[i] == 0){
				check[i] = 1;	// Check visit
				DFS(i);
				check[i] = 0;	// Uncheck other searches not to be affected
			}
		}
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	int edge, i, j;
	int from, to, value;
	
	cin >> node >> edge;
	
	for(i=1; i<=edge; i++){
		cin >> from >> to;
		map[from][to] = 1; 
	}	
	
	check[1] = 1;
	DFS(1);
	
	cout << cnt << endl;
	
	return 0;
}
