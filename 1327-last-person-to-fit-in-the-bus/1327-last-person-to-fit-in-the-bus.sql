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
