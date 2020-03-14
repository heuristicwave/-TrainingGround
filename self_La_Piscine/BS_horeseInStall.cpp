#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int count(int len, vector<int> &v){
	int i, cnt = 1, pos=v[1];

	for(i=2; i<=v.size(); i++){
		if(v[i] - pos >= len){
			cnt++;
			pos = v[i];
		}
	}
	return cnt;
}

int main(){
	// freopen("input.txt", "rt", stdin);
	
	int num, horse, res;
	int lo, hi;
	int mid; 
	
	cin >> num >> horse;
	
	vector<int> stall(num);
	
	for(int i=1; i<=num; i++){
		cin >> stall[i];
	}
	
	sort(stall.begin(), stall.end());
		
	lo = stall[1];
	hi = stall[num];
	
	while(lo<=hi){
		mid = (lo+hi)/2;
		if(count(mid, stall)>=horse){
			res = mid;
			lo = mid + 1;			
		} else {
			hi = mid - 1;
		}
	}
	
	cout << res;
	
	return 0;
}
