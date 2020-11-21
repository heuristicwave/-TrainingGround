/*
    코린이를 위한 선수 지식

    함수 정의 방법
     - fun 함수이름 (변수이름: 변수타입: 리턴타입 {리턴값}
    
    람다 함수 정의 방법
     - {매개변수 -> 함수이름}
 */

class Solution {
    fun solution(n: Int): String {
        return "수박".repeat(n / 2) + if (n % 2 != 0) "수" else ""
    }
}

// 람다를 활용한 풀이
// 아직 repeat 되는 원리는 모르겟다
class SolutionTwo {
    fun solution(n: Int): String = getStringPattern(n)  // 함수를 정의함과 동시에 다른 함수 호출

    fun isEven(v: Int) = if (v % 2 === 0) "수" else "박"

    fun getStringPattern(n: Int): String {
        return Array(n) { i -> isEven(i) }.joinToString("") // '수', '박' 사이에 공백으로 join
    }
}