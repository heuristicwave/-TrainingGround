#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Block{
	int s;
	int h;
	int w;
	
	Block(int a, int b, int c){
		s = a; h = b; w = c;
	}
	
	// Descending by s
	bool operator< (const Block &b) const{
		return s > b.s; 	// b.s is called, called object is small then ever
		// return s < b.s;	// Ascending
	}
};

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, a, b, c;
	int i, j, res;
	int max_h = 0;
	
	cin >> n;
	
	vector<Block> T;
	vector<int> dy(n, 0);
	
	for(i=0; i<n; i++){
		cin >> a >> b >> c;
		T.push_back(Block(a, b, c));	// Type !!!
	}

	sort(T.begin(), T.end());
	dy[0] = T[0].h;
	res = dy[0];
	
	for(i=1; i<n; i++){
		max_h = 0;
		for( j=i-1; j>=0; j--){
			if(T[j].w > T[i].w && dy[j] > max_h ){
				max_h = dy[j];
			}
		}
		dy[i] = max_h+T[i].h;
		res = max(res, dy[i]);
	}
	
	cout << res;
	
	return 0;
}
