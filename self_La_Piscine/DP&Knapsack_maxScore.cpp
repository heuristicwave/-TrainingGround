#include <iostream>
#include <vector>
using namespace std;

/// Do not use 2D array !!!
/// No map required, minimize use of vector !!!
int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("input.txt", "rt", stdin);
	
	int n, m, i, j;
	int qs, qt;	// quiz_scorem quiz_time 
	cin >> n >> m;	
	
	vector<int> dy(m+1, 0);
	
	for(i=0; i<n; i++){
		cin >> qs >> qt;
		// Record while counting the time behind the array
		for(j=m; j>=qt; j--){
			dy[j] = max(dy[j], dy[j-qt]+qs);	
		}
	}
	
	cout << dy[m];
	return 0;
}
