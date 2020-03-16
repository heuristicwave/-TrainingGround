#include <iostream>
using namespace std;

int map[51][51];
int main() {
	freopen("input.txt", "rt", stdin);
	
	int node, edge, i, j;
	int from, to, value;
	
	cin >> node >> edge;
	
	for(i=1; i<=edge; i++){
		cin >> from >> to >> value;
		map[from][to] = value; 
	}	
	
	for(i=1; i<=node; i++){
		for(j=1; j<=node; j++){
			cout << map[i][j] << ' ';
		}
		cout << '\n';
	}
	
	return 0;
}
