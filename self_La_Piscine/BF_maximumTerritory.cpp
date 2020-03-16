#include <iostream>
using namespace std;
/*
	Testcase A 
	10 19
	6 7 7 2 4 5 6 7 2 1 3 6 4 4 7 7 7 9 7 
	2 1 3 9 1 1 2 2 3 7 5 8 4 1 7 2 8 1 3 
	4 5 9 2 3 3 7 1 9 3 6 1 7 4 8 2 5 8 8 
	3 2 6 9 7 1 7 8 9 5 4 4 9 6 1 9 8 1 8 
	9 1 6 8 2 7 6 4 1 2 1 3 1 3 6 9 8 1 2 
	9 2 9 7 1 4 5 3 6 2 4 4 7 8 1 5 7 2 3 
	1 2 9 2 1 6 8 5 6 8 9 8 6 4 1 3 6 4 9 
	7 7 7 5 4 7 8 1 9 5 8 2 2 8 2 9 1 8 6 
	5 7 2 4 3 4 4 3 8 7 5 2 2 9 9 8 9 8 5 
	3 5 3 6 8 4 4 1 8 7 7 3 8 3 1 7 7 4 8 
	5 6
	
	In test case A,
	starting from 1 and including <= and
	starting from 0 to < are different results.
*/
int main() {
	freopen("input.txt", "rt", stdin);
	
	int width, height;
	int myW, myH;
	int max = -2147000000;
	int total = 0;
	
	cin >> height >> width;
	
	int territory[height+1][width+1];

	// input value
	for(int i=1; i<=height; i++){
		for(int j=1; j<=width; j++){
			cin >> territory[i][j];
		}
	}
	
	cin >> myH >> myW;
	
	for(int i=1; i<=height-myH+1; i++){
		for(int j=1; j<=width-myW+1; j++){
			total = 0;	// calculate my territory
			for(int k=i; k<i+myH; k++){
				for(int l=j; l<j+myW; l++){
					total += territory[k][l];
				}
			}
			if(total > max)	max = total;
		}
	}	
	
//	// input value
//	for(int i=0; i<height; i++){
//		for(int j=0; j<width; j++){
//			cin >> territory[i][j];
//		}
//	}
//	
//	cin >> myH >> myW;
//	
//	for(int i=0; i<height-myH; i++){
//		for(int j=0; j<width-myW; j++){
//			total = 0;	// calculate my territory
//			for(int k=i; k<i+myH; k++){
//				for(int l=j; l<j+myW; l++){
//					total += territory[k][l];
//				}
//			}
//			if(total > max)	max = total;
//		}
//	}	
	cout << max << endl;
	return 0;
}

