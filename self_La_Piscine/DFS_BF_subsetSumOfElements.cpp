#include <iostream>
using namespace std;

int n;
int a[11];	// array containing elements
int total = 0;
bool flag=false;

void DFS(int L, int sum){
	if(sum > (total/2))	return;	// sum is bigger than total/2
	if(flag == true)	return;
	if(L==n+1){
		if(sum == (total - sum)){
			flag = true;
		}
	}
	else {		
		DFS(L+1, sum+a[L]);	// level ++, Use element to add value
		DFS(L+1, sum);	// level ++, No element is used, Not change
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	cin >> n;
	for(int i=1; i<=n; i++){
		cin >> a[i];
		total += a[i];
	}	
	
	DFS(1, 0);	// parameter : level 1, sum of elements
	
	if(flag) cout << "YES" << endl;
	else	cout << "NO" << endl;
	
	return 0;
}
