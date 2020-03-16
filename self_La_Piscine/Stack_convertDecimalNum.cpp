#include <iostream>
#include <stack>
using namespace std;

/*
	int stack[100], top = -1;
	
	void push(int x){
		stack[++top] = x;
	}
	
	int pop(){
		return stack[top--];
	}
*/

int main() {
	freopen("input.txt", "rt", stdin);
	
	int num, k;
	stack<int> s;
	
	char str[20] = "0123456789ABCDEF";
	cin >> num >> k;
	
	while(num>0){
		s.push(num%k);
		num = num/k;
	}
	
	// print converted decimal value
	while(s.empty()){	// top!=-1
		cout << str[pop()];	// printf("%c", str[pop()]);
	}
	return 0;
}

