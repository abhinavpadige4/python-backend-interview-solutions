-- SQL Solution for LeetCode 180: Consecutive Numbers
-- Write a SQL query to find all numbers that appear at least three times consecutively.

SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.Id = l2.Id - 1 AND l1.Num = l2.Num
JOIN Logs l3 ON l2.Id = l3.Id - 1 AND l2.Num = l3.Num;