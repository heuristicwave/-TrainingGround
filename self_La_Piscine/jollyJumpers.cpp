#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

int main(){
	// freopen("input.txt", "rt", stdin);
	
	int num;
	int a[100000] = { 0, };
	int index;
	
	cin >> num;
	
	for(int i=0; i<num; i++){
		cin >> a[i];
	}
	
	int count[num] = {0};

	for (int i=0; i<num; i++){
		index = abs(a[i] - a[i+1]);
		count[index]++;
	}	
	
	for (int i=1; i<num; i++){
		if(count[i] != 1){
			printf("NO\n");
			return 0;
		}	
	}
	
	printf("YES\n");
    
	return 0;
}
