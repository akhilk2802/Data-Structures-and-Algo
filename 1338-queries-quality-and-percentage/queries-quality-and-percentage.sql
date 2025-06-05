# Write your MySQL query statement below

-- quality -> average of the ratio between query rating and its position
-- poor query percentage -> the percentage of all queries with rating less than 3


-- SELECT query_name, () as quality, () as poor_query_percentage
-- FROM Queries
-- WHERE

-- SELECT query_name, ROUND(AVG(rating / position), 2) as quality FROM Queries GROUP BY query_name;
-- -- SELECT query_name, () as percentage FROM Queries GROUP BY query_name;
-- SELECT ROUND(
--     COUNT(CASE WHEN rating < 3 THEN 1 END) * 100.0 / COUNT(*),
--     2
--   ) AS poor_query_percentage
-- FROM Queries;

SELECT
query_name,
ROUND(AVG(rating / position), 2) as quality,
ROUND(SUM(CASE WHEN rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
FROM Queries
GROUP BY
query_name;

