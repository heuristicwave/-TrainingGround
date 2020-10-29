## MYSQL

COUNT 결과 값끼리의 연산

```mysql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION -- DISTINCT : 중복제거 --
```

> total 값 구하는 `SUM`과 구분!
>
> ```mysql
> SELECT SUM(POPULATION) / COUNT(POPULATION)	-- 평균 구하기 --
> -- 소수점 나올때 ROUND() 적용해 정수형 출력 가능 --
> -- ROUND : 반올림 / FLOOR : 소수점 내림 / CEILING : 소수점 올림 -- 
> ```



**[Weather Observation Station 5](https://www.hackerrank.com/challenges/weather-observation-station-5/problem) (LENGTH & UNION)**

```mysql
-- 1행, CITY만 두면 길이는 짧은데 도시 이름이 안짧은거 포함됨 --
(SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY ASC LIMIT 1)
UNION
(SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC LIMIT 1)
```



**[Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6/problem) (REGEXP)**

```mysql
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP'^[aeiou]'	-- ^ : 첫번째 문자 매칭 / [] : 문자열 셋, 이어서 쓰면 |의 효과 --

-- 문자열 뒤라면 '[aeiou]$' 사용 --
-- 문자열 셋에 해당 하지 않는 것은 '[^aeiou]$' 사용(문자열 셋 안에 ^) --
```

**LIKE 사용**

```mysql
-- 문자열 앞은 A%, 반대로 문자열 뒤는 %A --
WHERE CITY like('a%') or CITY like('e%') or CITY like('i%') or CITY like('o%') or CITY like('u%'); 

-- 9번 문제 NOT --
WHERE CITY NOT LIKE 'a%' and CITY NOT LIKE 'e%' and CITY NOT LIKE 'i%' and CITY NOT LIKE 'o%' and CITY NOT LIKE 'u%'
```

**문자열 앞과 뒤로** 

```mysql
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$'
-- . 어떠한 글자이든지 상관없이 하나 --
-- * 앞에 글자가 0개 이상있는 경우 --
-- .* 어떠한 글자이든지 상관없이 --
-- AND로 대체 하기 -- 
WHERE city REGEXP '^[aeiou]' and city REGEXP '[aeiou]$'

-- 문자열 셋 사이에 | 를 적용하면 or 효과 --
```



[Higher Than 75 Marks](https://www.hackerrank.com/challenges/more-than-75-marks/problem) (정렬 기준 2개 : 이름 끝자리 3개 기준 정렬, ID )

```mysql
SELECT NAME FROM STUDENTS WHERE Marks > 75
ORDER BY RIGHT(NAME, 3), ID
```



## JOIN

### INNER (default)

```mysql
SELECT <출력 대상>
FROM <첫 번째 테이블>
	INNER JOIN <두 번째 테이블>
	ON <조인 조건>
[WHERE <검색 조건>]
```

> [연습문제](https://www.hackerrank.com/challenges/asian-population/problem)



### GROUP BY

집계를 위한 용도로 사용, GROUP BY 절에서 조건을 주려면 `HAVING` 사용

[평균과 GROUP BY](https://www.hackerrank.com/challenges/average-population-of-each-continent/problem)

