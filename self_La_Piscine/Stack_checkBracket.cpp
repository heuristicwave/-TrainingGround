#include <iostream>
#include <stack>
using namespace std;

int main() {
	freopen("input.txt", "rt", stdin);
	
	stack<int> s;	
	char str[50];
	int flag = 1;
	
	cin >> str;	// scanf("%s", &str);
	
	for(int i=0; str[i] != '\n'; i++){
		if(str[i] == '(')	s.push(str[i]);
		else {
			if(s.empty()){
				cout << "NO" << endl;
				flag = 0;	// )(
				break;
			} else s.pop();
		}
	}
	
	if(s.empty() && flag ==1)	cout << "YES" << endl;
	else if(!s.empty() && flag == 1)	cout << "NO" << endl;
	
	return 0;
}

