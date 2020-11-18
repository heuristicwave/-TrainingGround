/*
    코린이를 위한 선수 지식

    Pair와 Triple 
    Pair를 사용해 2개의 변수를 한꺼번에 할당 받을 수 있고
    >> 2개의 객체를 저장할 수 있는 객체
    Triple을 사용하면 3개의 변수를 한꺼번에 할당 받을 수 있다
    >> 3개의 객체를 저장할 수 있는 객체

    더 알아보기 : https://codechacha.com/ko/kotlin-pair-and-triple/
*/

class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        val answer = mutableListOf<Int>()   // int형 가변 배열 형성
        for (index in commands.indices) {
            val (i, j, k) = commands[index]     // triple 을 사용해 배열의 요소 받기
            val conditionOne = array.slice(i - 1 until j)   // until로 범위 결정
            val conditionTwo = conditionOne.sorted()
            answer.add(conditionTwo[k - 1]) // 조건 3번을 answer 배열에 push
        }
        return answer.toIntArray()  // mutable 리스트를 문제 조건에 맞게 intArray로 변환
    }
}