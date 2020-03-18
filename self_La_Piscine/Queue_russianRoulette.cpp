#include <iostream>
#include <queue>
using namespace std;

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, k;
	int i, x;
	int cp = 1;
	queue<int> Q;
	
	cin >> n >> k;
	
	for(i=1; i<=n ; i++){ 
		Q.push(i);
	}
	
	while(!Q.empty()) {	// !! exit condition !!
		// using queue principle
		for(i=1; i<k; i++){	// one loop, two elements pop
			Q.push(Q.front());
			Q.pop();
		}
		Q.pop();	// one element pop, 3 times
		if(Q.size() == 1){
			cout << Q.front() << endl;
			Q.pop();
		}
	}
	
	return 0;
}
