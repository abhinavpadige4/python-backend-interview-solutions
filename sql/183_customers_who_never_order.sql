-- SQL Solution for LeetCode 183: Customers Who Never Order
-- Write a SQL query to find all customers who never order anything.

SELECT 
    Customers.Name AS Customers
FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.Id IS NULL;