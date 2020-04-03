#### 특정 갯수 만큼 인자 값을 받을 때

```c
while (scanf("%d %d",&a,&b) == 2)
```

#### 그대로 출력하기

```c
scanf("%[^\n]\n", s);
```

```c
    char c;
    while ((c = getchar()) && c != EOF) {
        printf("%c",c);
    }
```
> **한 줄 다 입력 받기**
```c
getline(cin, s); 
```

### Vector
```cpp
vector<int> a = {1, 2, 3, 4, 5};
for (vector<int>::iterator it = a.begin(); it != a.end(); ++it) {
    cout << *it << ' ';
} 
```



## Python3

#### [A + B](https://www.acmicpc.net/problem/10951)

```python
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
```

```c++
#include <iostream>
using namespace std;

int main() {
    int a, b;
    while(scanf("%d %d", &a, &b) == 2){
        cout << a+b << "\n";
    }
}
```

