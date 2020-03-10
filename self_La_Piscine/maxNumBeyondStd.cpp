#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	//freopen("input.txt", "rt", stdin);
	
	int time; 
	int sound;
	int check = 0;
	int a[100] = { 0, };
	int max = -2147000000;
	
	cin >> time >> sound;
	
	for (int i = 0; i<time; i++){
		cin >> a[i];
		
		if (a[i] > sound) check++;
		else check = 0;
		
		if (check > max) max = check;
	}
	
	if (max == 0) printf("-1\n");
	else printf("%d\n" , max);
	
    return 0;
}
