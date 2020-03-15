#include <iostream>
#include <vector>
using namespace std;

int main(){
	freopen("input.txt", "rt", stdin);
	
	int roulette, turn;
	int pos = 0;
	int bp = 0;	// check last element
	int cnt = 0; // count removed elements
	cin >> roulette >> turn;
	
	vector<int> v(roulette+1);
	
	while(bp != roulette-1){
		pos++;
		if(pos>roulette) pos = 1;
		if(v[pos]==0){
			cnt++;
			if(cnt == turn){
				cnt = 0;
				v[pos] = 1;
				bp++;
			}
		}
		// if(bp == roulette-1)	break;
	}
	
	for(int i=1; i<=roulette; i++){
		if(v[i] == 0){
			cout << i;
			break;
		}	
	}
	
	return 0;
}

