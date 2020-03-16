#include <iostream>
using namespace std;

int territory[701][701], dynamic[701][701];
int main() {
	freopen("input.txt", "rt", stdin);
	
	int width, height;
	int myW, myH;
	int max = -2147000000;
	int total = 0;
	
	cin >> height >> width;
	
	// input value
	for(int i=1; i<=height; i++){
		for(int j=1; j<=width; j++){
			cin >> territory[i][j];
			dynamic[i][j]=dynamic[i-1][j]+dynamic[i][j-1]
							-dynamic[i-1][j-1]+territory[i][j];
		}
	}
	
	cin >> myH >> myW;
	
	for(int i=myH; i<=height; i++){
		for(int j=myW; j<=width; j++){
			total=dynamic[i][j]-dynamic[i-myH][j]
					-dynamic[i][j-myW]+dynamic[i-myH][j-myW];
			if(total>max) max=total;	
		}
	}	
	
	cout << max << endl;
	return 0;
}

