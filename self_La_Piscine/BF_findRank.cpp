#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;
/*
	Instead of using sorting,
	set everything to 1 and solve with brute force
*/
int main(){
	freopen("input.txt", "rt", stdin);
	
	int num;
	int score[101] = { 0, };
	int rank[101] = { 0, };
	
	cin >> num;
	
	for(int i=1; i<=num; i++){
		cin >> score[i];
		rank[i] = 1;
	}
	
	for (int i=1; i<=num; i++){
		for (int j=1; j<=num; j++){
			if(score[j]>score[i])	rank[i]++;
		}
	}	
	
	for (int i=1; i<=num; i++){
		printf("%d ", rank[i]);
	}
    
	return 0;
}
