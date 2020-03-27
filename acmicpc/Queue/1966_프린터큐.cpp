#include <iostream>
#include <queue>
using namespace std;

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("input.txt", "rt", stdin);
	
	int n, m, i, j;
	int tc;	// test case
	int doc;	// document
	
	cin >> tc;
	
	while(tc--) {
		int result = 0;
		queue<pair<int, int> > q;
		priority_queue<int> pq;
		cin >> n >> m;
		for(i=0; i<n; i++){
			cin >> doc;
			q.push(make_pair(doc, i));
			pq.push(doc);
		}
		
		while(!q.empty()){
			int prior = q.front().first;
            int num = q.front().second;
            q.pop();
			if(pq.top() == prior){
				result++;
				pq.pop();
				if(num == m)	break;
			} else {
				q.push(make_pair(prior, num));
			}
		}
		cout << result << endl;
	}
		
	return 0;
}
