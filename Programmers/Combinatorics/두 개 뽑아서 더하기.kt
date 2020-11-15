/*
    코린이를 위한 선수 지식
    
    - Collections(자바에서 데이터를 저장하는 기본 자료구조)
    - listOf, SetOf => Immutable 하게 각각 리스트와 집합(중복 불가 리스트)을 생성
    - 조합, 2중 for문으로 요소를 선택하고 2개가 같은 경우 제거

    * indices : iterable한 array의 index 순회
    * toTypedArray() : collection을 배열로 변환

*/
class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()        
        var sumOfTwo = mutableSetOf<Int>()  // 갯수가 몇개 인지 모르니 가변 리스트 생성

        for (i in numbers.indices) {    // numbers에 들어 있는 요소만큼 인덱스 순회 
            for (j in numbers.indices) {
                 if(i == j) continue
                 // println("선택한 두 수 : $i, $j")
                 sumOfTwo.add(numbers[i] + numbers[j])  // push
            }
        }        
        answer = sumOfTwo.sorted().toIntArray() // 정렬 후, int형 array로 변환
        
        return answer
    }
}