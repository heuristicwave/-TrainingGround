#include <iostream>
#include <vector>
using namespace std;

int col[11];
int row[11];

int main() {
	// freopen("input.txt", "rt", stdin);
	
	int size, total;
	cin >> size;
	int block[size][size] = { 0, };
	
//	vector<int> row(size);	// Static arrays are
//	vector<int> col(size);	// faster than vectors
	
	for(int i=0; i<size; i++)	cin >> col[i];
	for(int i=size; i>0; i--)	cin >> row[i];
	
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			block[j][i] = col[i];
		}
	}
	
	// my mistake i+1, 
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			if(block[i][j] > row[i+1]){
				block[i][j] = row[i+1];
			}
		}
	}
	
	// calculate total
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			total += block[i][j];
		}
	}
	cout << total << endl;
	return 0;
}
