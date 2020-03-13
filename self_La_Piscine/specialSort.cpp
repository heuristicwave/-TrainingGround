#include <iostream>
#include <cstdio>
#define SWAP(x, y, temp) ( temp = x, x = y, y = temp )
using namespace std;

int main(){
	//freopen("input.txt", "rt", stdin);
	
	int cnt = 0;
	int num;
	int negativePos[100] = { 0, };
	int positivePos[100] = { 0, };
	int nIndex = 0, pIndex = 0;
		
	cin >> num;
	
	int list[num];
	
	for(int i=0; i<num; i++){
		cin >> list[i];
	}
		
	for(int i=0; i<num; i++){
		if (list[i]>0){
			positivePos[pIndex] = list[i];
			pIndex++;
		} else {
			negativePos[nIndex] = list[i];
			nIndex++;
		}
	}

	for(int i=0; negativePos[i] != 0; i++) {
		printf("%d ", negativePos[i]);
	}
	for(int i=0; positivePos[i] != 0; i++) {
		printf("%d ", positivePos[i]);
	}	

	return 0;
}
