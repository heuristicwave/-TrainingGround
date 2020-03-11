#include <iostream>
#include <cstdio>
using namespace std;

/*	Optimization
	!! Insert flag to win or lose !!
	!! Judgment of the game result when drawn !!
	!! Using flags !! Not Score !!
*/

int main(){
	// freopen("input.txt", "rt", stdin);
	
	int a[11];
	int b[11];
	int flag = 0;
	int scoreA = 0;
	int scoreB = 0;
		
	for (int i = 1; i<=10; i++){
		cin >> a[i];
	}
	
	for (int i = 1; i<=10; i++){
		cin >> b[i];
		
		if(a[i] > b[i])	{
			scoreA += 3;
			flag = 1;
		}
		else if(a[i] < b[i]){
			scoreB += 3;
			flag = 2;
		}	
		else {
			scoreA += 1;
			scoreB += 1;
		}		
	}
	
	cout << scoreA << ' ' << scoreB << '\n';

	if (a[1] == b[1]){
		if (flag == 0) printf("D\n");
		else if (flag == 1) printf("A\n");
		else printf("B\n");		
	}
	else if (scoreA > scoreB) printf("A\n");
	else printf("B\n");
	
    return 0;
}
