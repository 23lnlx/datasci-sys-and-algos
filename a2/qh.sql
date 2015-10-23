
    SELECT  sum(fr1.count*fr2.count)
    FROM frequency fr1 JOIN frequency fr2 ON fr1.term = fr2.term
    where fr1.docid ='10080_txt_crude'  and fr2.docid ='17035_txt_earn'


;
