#include <iostream>
using namespace std;

void recursive(int n){
	if(n==0)	return;
	else {		
		// cout << n << ' ';	// DESCENDING
		recursive(n-1);	
		cout << n << ' ';	// ASCENDING, RISE!
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	int num;
	cin >> num;
	
	recursive(num);
	
	return 0;
}

