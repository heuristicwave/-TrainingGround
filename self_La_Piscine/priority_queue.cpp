#include <iostream>
#include <queue>
using namespace std;

int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);	
	freopen("input.txt", "rt", stdin);
	
	int a;
	priority_queue<int> pQ;
	
	// Max Heap
	while(true){
		cin >> a;
		if (a == -1)	break;
		if (a == 0){
			if(pQ.empty())	cout << -1 << endl;
			else {
				cout << pQ.top() << endl;	// root node
				pQ.pop();
			}
		}
		else pQ.push(a);
	}
	
	// Min Heap
	while(true){
		cin >> a;
		if (a == -1)	break;
		if (a == 0){
			if(pQ.empty())	cout << -1 << endl;
			else {
				cout << -pQ.top() << endl;	// root node
				pQ.pop();
			}
		}
		else pQ.push(-a);
	}
	
	return 0;
}