#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
	Use merge sort when N is large
*/
int main(){
	freopen("input.txt", "rt", stdin);
	
	int num;
	int cnt = 0;
	
	cin >> num;
	
	vector<int> rank(num+1);
	
	for(int i=1; i<=num; i++){
		cin >> rank[i];
	}
	
	printf("1 ");	
	for (int i=2; i<=num; i++){
		cnt = 0;
		for (int j=i-1; j>=1; j--){
			if(rank[j]>=rank[i]) cnt++;
		}
		printf("%d ", cnt+1);
	}
    
	return 0;
}
