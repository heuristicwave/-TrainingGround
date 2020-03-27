#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

vector<pair<int, int> > pz;	// pizzeria location vector
vector<pair<int, int> > hs;	// house location vector
int ch[20];
int m, dis;
int res = 2147000000;
int sum = 0;
int i, j;
	
void DFS(int L, int s){
	if(L>pz.size()) return;
	if(s==m){
		sum = 0;
		for(i=0; i<hs.size(); i++){
			int x1 = hs[i].first;
			int y1 = hs[i].second;
			dis = 2147000000;
			for(j=0; j<m; j++){
				int x2 = pz[ch[j]].first;
				int y2 = pz[ch[j]].second;
				dis = min(dis, abs(x1-x2)+abs(y1-y2));
			}
			sum += dis;
		}
		if(sum<res)	res = sum;
	} else {
		ch[s] = L;
		DFS(L+1, s+1);
		DFS(L+1, s);
	}
}

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int n, val;

	cin >> n >> m;
	
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			cin >> val;
			if (val==1)	hs.push_back(make_pair(i, j));
			else if (val==2) pz.push_back(make_pair(i, j));
		}
	}
	DFS(0, 0);
	cout << res;
	
	return 0;
}

