#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

/*	Optimization
	!!! DP - Formulate Consensus Process !!!
*/

int main(){
	freopen("input.txt", "rt", stdin);
	
	int sum = 0;
	int tempNum = 0;
	int num = 0;
	int max = -2146000000;
	
	cin >> tempNum >> num;
	
	vector<int> temp(tempNum);
	
	for(int i = 0; i < tempNum; i++){
		cin >> temp[i];
	}

	for(int i=0; i<num; i++){
		sum += temp[i];
	}
	max = sum;
	
	/// FORMULATE
	for(int i = num; i < tempNum; i++){
		sum += (temp[i] - temp[i-num]);
		if(sum > max) max = sum;
	}

/*  !!! Time Limit !!!	
	for(int i = 0; i < tempNum - num; i++){
		total = 0;
		for(int j = i; j < i + num; j++){
			total += temp[j];  
		}
		if(total > max) max = total;
	}
*/	
	printf("%d\n", max);
	
    return 0;
}
