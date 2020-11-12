## [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers)

ManagerId를 확인해서 해당되는 사람의 Salary보다 높은 사람의 이름만 출력하기

```json
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```



접근 방법 : 주어진 테이블이 하나 일때, 테이블이 2개인 것처럼 활용하기



**WHERE 사용**

```mysql
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;
```



**JOIN 사용**

```mysql
SELECT a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;
```





## [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order)

order 한적 없는 customer 목록 출력하기

```json
/* Customers */			/* Orders */		/* Result */
+----+-------+		+----+------------+		+-----------+
| Id | Name  |		| Id | CustomerId |		| Customers |
+----+-------+		+----+------------+		+-----------+
| 1  | Joe   |		| 1  | 3          |		| Henry     |
| 2  | Henry |  	| 2  | 1          |		| Max       |
| 3  | Sam   |		+----+------------+		+-----------+
| 4  | Max   |
+----+-------+
```



접근 방법 : `Customers` 테이블의 `Id`와 `Orders`테이블의 `CustomerId`가 동일함.



**WHERE 사용**

```mysql
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);
```



**JOIN 사용**

```mysql
SELECT Name AS 'Customers'
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL
```



