#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt", "rt", stdin);
	
	int s, n;
	int i, j;
	int pos;
	int a;
	
	cin >> s >> n;
	
	int cache[n] = { 0, };
	
	for(int i=0; i<n; i++){
		cin >> a;
		pos = -1;
		for(j=0; j<s; j++)
			if(cache[j] == a)	pos = j;	// heat
		if(pos == -1){
			for(j=s-1; j>=1; j--)	cache[j]=cache[j-1];
		} else {
			for(j=pos; j>=1; j--)	cache[j]=cache[j-1];
		}
		cache[j] = a;
	}
	for(i=0; i<s; i++)	cout << cache[i] << ' ';
	
	return 0;
}
