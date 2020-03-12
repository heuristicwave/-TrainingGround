#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*

*/
int main(){
	freopen("input.txt", "rt", stdin);
	
	int num;
	int tmp;
	
	cin >> num;
	
	vector<int> check(num+1);
		
	for (int i=2; i<=num; i++){
		tmp = i;
		int j =2;
		while(1){
			if(tmp % j == 0){
				tmp = tmp / j;
				check[j]++;
			}
			else j++;
			if(tmp == 1) break;
		}
	}
    
    printf("%d! = ", num);
    for(int i = 2; i<=num; i++){
    	if(check[i] != 0)	printf("%d ", check[i]);
	}
	
	return 0;
}
