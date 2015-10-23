SELECT doc, max(maximum)
FROM(

    SELECT  fr1.docid as doc, sum(fr1.count*fr2.count) as maximum
    FROM frequency fr1 JOIN
    (
        SELECT * FROM frequency
        UNION
        SELECT 'q' as docid, 'washington' as term, 1 as count
        UNION
        SELECT 'q' as docid, 'taxes' as term, 1 as count
        UNION
        SELECT 'q' as docid, 'treasury' as term, 1 as count
    ) fr2 ON fr1.term = fr2.term
    WHERE fr2.docid = 'q'
    GROUP BY fr1.docid
)

;
