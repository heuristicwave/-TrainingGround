#include <iostream>
using namespace std;

// Merge sorting uses Post-Order
void DFS(int n){
	if(n>7)	return;
	else {		
		//cout << n << ' ';	// Pre-Order
		DFS(n*2);	// left node
		//cout << n << ' ';	// In-Order
		DFS(n*2+1);	// right node
		//cout << n << ' ';	// Post-Order
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	DFS(1);
	
	return 0;
}
