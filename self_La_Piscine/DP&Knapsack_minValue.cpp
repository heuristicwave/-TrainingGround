#include <iostream>
#include <vector>
using namespace std;

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, m;
	int i, j;
	cin >> n;
	
	vector<int> coin(n);
	for(i=0; i<n; i++)	cin >> coin[i];
	
	cin >> m;
	
	// Vector containing the minimum num of coin
	vector<int> dy(m+1, 1000);
	
	dy[0] = 0; // first vector init
	
	for(i=0; i<n; i++){
		for(j=coin[i]; j<=m; j++){
			// max param1 : before num,
			// param2 : sub one coin to dy, and add num(1)
			dy[j] = min(dy[j], dy[j-coin[i]] + 1);
		}
	}

	cout << dy[m];
	
	return 0;
}
