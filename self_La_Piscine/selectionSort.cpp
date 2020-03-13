#include <iostream>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

using namespace std;

void selection_sort(int list[], int n){
	int min, temp;
	
	for(int i=0; i<n; i++){
		min = i;
		
		for(int j = i+1; j<n; j++){
			if(list[j]<list[min])	min = j;
		}
	
		if(i != min){
			SWAP(list[i], list[min], temp);
		}
	}
}

int main(){
	freopen("input.txt", "rt", stdin);
	
	int num;	
	cin >> num;
	
	int list[num];
	
	for(int i=0; i<num; i++){
		cin >> list[i];
	}
	
	selection_sort(list, num);
	
	for(int i=0; i<num; i++){
		printf("%d ", list[i]);	
	}	
	
	return 0;
}
