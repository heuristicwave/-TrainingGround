#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int songs[1001], n;

int count(int size){
	int cnt=1;
	int sum = 0;
	
	/// Decide whether to increase the number of dvds
	for (int i=1; i<=n; i++){
		if(sum + songs[i] > size){
			cnt++;
			sum = songs[i]; // create new dvd
		} else {
			 sum += songs[i];
		}
	}
	
	return cnt;
}

int main(){
	freopen("input.txt", "rt", stdin);
	
	int dvd;
	int lo = 1, hi = 0;
	int mid, res;
	int maxPlaytime = -2147000000;
	
	cin >> n >> dvd;
	
	for(int i=1; i<=n; i++){
		cin >> songs[i];
		hi = hi + songs[i];
		if(songs[i]> maxPlaytime)	maxPlaytime = songs[i];
	}
	while(lo<=hi){
		mid = (lo+hi)/2;
		if(mid >= maxPlaytime && count(mid)<=dvd){
			res = mid;
			hi = mid - 1;			
		} else {
			lo = mid + 1;
		}
	}
	
	cout << res;
	
	return 0;
}
