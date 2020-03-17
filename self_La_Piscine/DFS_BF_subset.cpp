#include <iostream>
using namespace std;

/*
	Testcase input 3
	2*2*2 = 8
	=> 7 subsets and 1 emptyset
*/ 

int n;
int ch[11];	// Check array notation for pre-order

void DFS(int L){
	
	if(L==n+1){
		for(int i=1; i<=n; i++){
			if(ch[i]==1)	cout << i << ' ';
		}
		cout << endl;
	}
	else {		
		ch[L] = 1; // go left
		DFS(L+1);	// level ++
		ch[L] = 0;	// right
		DFS(L+1);	// search right node
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	cin >> n;
	
	DFS(1);	// parameter : level 1
	
	return 0;
}
