#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt", "rt", stdin);
	
	int n, m;
	int i, j;
	int fp = 1;
	int sp = 1;
	int mp = 1;
	
	cin >> n;	
	vector<int> first(n+1);	
	for(i=1; i<n+1; i++){
		cin >> first[i];
	}
	
	cin >> m;
	vector<int> second(m+1);
	for(i=1; i<m+1; i++){
		cin >> second[i];
	}
	
	vector<int> merge(n+m+1);
	
	/// Using while, satisfy two conditions
	while(fp<=n && sp<=m){
		if(first[fp]<second[sp]){
			merge[mp] = first[fp];
			mp++;	// WRITE
			fp++;	// LIKE
		} else {
			merge[mp] = second[sp];
			mp++;	// LINES
			sp++;	// 42, 43
		}
	}	
	while(fp<=n)	merge[mp++] = first[fp++];
	while(sp<=m)	merge[mp++] = second[sp++];
		
	for(i=1; i<n+m+1; i++){
		cout << merge[i] << ' ';
	}
	
	return 0;
}
