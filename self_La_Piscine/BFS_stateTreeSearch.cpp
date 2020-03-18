#include <iostream>
#include <queue>
#include <vector>
using namespace std;

/// Reduce the time complexity by checking the same condition
int ch[10001];		// check
int d[3] = {1, -1, 5};	// distance

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int s, e, x, pos;
	queue<int> Q;
	
	cin >> s >> e;
	ch[s] = 1;
	
	Q.push(s);	// first start node check
	
	while(!Q.empty()){
		x = Q.front();
		Q.pop();	// deqeue
		for(int i=0; i<3; i++){	// +5, +1, -1
			pos = x+d[i];	// location update
			if(pos <= 0 || pos > 10000)	continue;
			if(pos == e){
				cout << ch[x] << endl;
				return 0;
			}
			if(ch[pos]==0){
				ch[pos] = ch[x]+1;	// ch[x] : num of go to x
				Q.push(pos);	// enqueue	
			}
		}
	}
		
	return 0;
}
