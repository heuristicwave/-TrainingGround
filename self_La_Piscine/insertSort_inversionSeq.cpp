#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt", "rt", stdin);
	
	int n, pos;
	int i, j;
	
	cin >> n;
	
	vector<int> is(n+1), os(n+1);
	
	for(i=1; i<n+1; i++){
		cin >> is[i];
	}
	
	for(i=n; i>=1; i--){
		pos=i;
		for(j=1; j<= is[i]; j++){
			os[pos]=os[pos+1];
			pos++;
		}
		os[pos]= i;
	}
	
	for(i=1; i<n+1; i++){
		cout << os[i] << ' ';
	}
	
	return 0;
}
