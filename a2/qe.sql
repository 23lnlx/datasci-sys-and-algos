SELECT count(*)
FROM (
    SELECT count(*) as countl
    FROM frequency fr
    GROUP BY fr.docid
)
WHERE (countl>300)
;
