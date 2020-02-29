#include <iostream>
#include <vector>
#include <algorithm>
#define FOR(i,n) for(int i=0; i<(n); i++)
using namespace std;

int main(){
    int arr[9] = {};
    int sum = 0;
    vector<int> realDwarf;
    
    FOR(i, 9) {
        cin >> arr[i];
        sum += arr[i];
    }

    FOR(i, 9){
        for(int j=i+1; j<9; j++) {
            if (sum - arr[i] - arr[j] == 100){
                FOR(k, 9)
                    if ((k != i)&&(k != j))
                        realDwarf.push_back(arr[k]);
                break;
            }
        }
    }

    sort(realDwarf.begin(), realDwarf.end());
    FOR(i, 7)
        cout << realDwarf[i] << '\n';
    
    return 0;
}