#include <iostream>
#include <stack>
#include <vector>
using namespace std;

/// Use the control pointer, like comparing experimental and control group

int main() {
	freopen("input.txt", "rt", stdin);
	
	int num, work;
	int cp = 1; 	// control pointer
	stack<int> s;	// For Experimental Group
	
	cin >> num;
	
	vector<char> str;
	for(int i=1; i<=num; i++){
		cin >> work;
	
		s.push(work);
		str.push_back('P');
		
		while(1){
			if(s.empty())	break;
			if(cp == s.top()){
				s.pop();
				cp++;
				str.push_back('O');
			}
			else	break;
		}
	}
	
	if(!s.empty())	cout << "impossible" << endl;
	else {
		for (int i=0; i<str.size(); i++)	cout << str[i];
	}
	
	return 0;
}

