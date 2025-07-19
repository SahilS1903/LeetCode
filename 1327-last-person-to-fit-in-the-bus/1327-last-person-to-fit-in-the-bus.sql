# Write your MySQL query statement below
SELECT person_name
FROM Queue
WHERE turn = (
    SELECT MAX(q2.turn)
    FROM Queue q2
    WHERE (
        SELECT SUM(q1.weight)
        FROM Queue q1
        WHERE q1.turn <= q2.turn
    ) <= 1000
);



-- # Write your MySQL query statement below
-- SELECT 
--     q1.person_name
-- FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
-- GROUP BY q1.turn
-- HAVING SUM(q2.weight) <= 1000
-- ORDER BY SUM(q2.weight) DESC
-- LIMIT 1