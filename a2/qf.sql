SELECT count(*)
FROM (
    SELECT  DISTINCT fr.docid
    FROM frequency fr
    WHERE (fr.term LIKE 'transactions')

    INTERSECT

    SELECT  DISTINCT fr.docid
    FROM frequency fr
    WHERE (fr.term LIKE 'world')

    )
;
