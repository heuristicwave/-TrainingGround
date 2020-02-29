#include <iostream>
#define FOR(i,n) for(int i=0; i<(n); i++)
using namespace std;

int main() {
	int currentSum = 0;
	int maxSum[100000] = {};
	int num = 0;
	int arr[100000] = {};
    int result = 0;
    
	cin >> num;
	FOR(i, num)
		cin >> arr[i];

	FOR(i, num) {
		if (currentSum + arr[i] < 0)
			currentSum = 0;
		else
			currentSum += arr[i];
        
        maxSum[i] = currentSum;
	}
    
	FOR(i, num) {
		if (result < maxSum[i])
			result = maxSum[i];
	}
    cout << result;
    
	return 0;
}