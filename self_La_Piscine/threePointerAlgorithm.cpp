#include <iostream>
using namespace std;

int a[1501];

/// Two Pointer Algorithm
int main() {
	freopen("input.txt", "rt", stdin);
	
	int num;
	int p2, p3, p5;
	int min = 2147000000;
	cin >> num;
	
	a[1] = 1;
	p2 = p3 = p5 = 1;
	
	for(int i = 2; i <= num; i++) {
		if(a[p2]*2<a[p3]*3)	min = a[p2]*2;
		else min = a[p3]*3;
		if(a[p5]*5<min)	min = a[p5]*5;
		
		if(a[p2]*2 == min)	p2++;
		if(a[p3]*3 == min)	p3++;
		if(a[p5]*5 == min)	p5++;
		a[i] = min;
	}
	
	cout << a[num] << endl;
	
	return 0;
}

