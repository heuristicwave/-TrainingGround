#include <iostream>
#include <cstdio>
using namespace std;

void insert_sort(int a[], int n){
	
	int copy, temp;
	int i, j;
	
	for(i=1; i<n; i++){
		copy = a[i];
		for(j = i-1; j>=0; j--){
			if(a[j]>copy){
				a[j+1] = a[j];
			} else break;
		}
		a[j+1] = copy;
	}
}

int main(){
	freopen("input.txt", "rt", stdin);
	
	int a[100];
	int n;
	int i, j;
	
	cin >> n;
	
	for(i=0; i<n; i++){
		cin >> a[i];
	}

	insert_sort(a, n);
	
	for(i=0; i<n; i++){
		cout << a[i] << ' ';
	}	
	cout << '\n';
	return 0;
}
