#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;


struct Data {
	int money;
	int when;
	// Params constructor initialization
	Data(int a, int b){
		money = a;
		when = b;
	}
	/// Descending order
	// The form of large data in front and small data in the back.
	bool operator< (const Data &b) const {
		return when > b.when;
	}
};

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, i, j;
	int a, b;
	int res = 0;
	int max = -2147000000;
	vector<Data> T;	// Vector storing struct
	priority_queue<int> pQ;
	
	cin >> n;
	for(i=1; i<=n; i++){
		cin >> a >> b;
		T.push_back(Data(a, b));
		if(b>max)	// the latest possible date
			max = b;
	}
	
	sort(T.begin(), T.end());	// sort by date
	j = 0;
	for(i=max; i>=1; i--){	// start from last date
		// enqueue
		for(; j<n; j++){
			if(T[j].when<i)	break;
			pQ.push(T[j].money);			
		}
		
		if(!pQ.empty()){
			res+=pQ.top();
			pQ.pop();
		}
	}
	
	cout << res << endl;
	
	return 0;
}
