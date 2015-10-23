import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    for k in range(5):
        if record[0] == 'a':
            mr.emit_intermediate((row,k),record)
        else:
            mr.emit_intermediate((k,col),record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key, list_of_values
    a=[]
    b=[]
    total=0
    for item in list_of_values:
        if item[0] == 'a':
            a.append((item[2], item[3]))
        else:
            b.append((item[1], item[3]))
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][0]==b[j][0]:
                total += a[i][1]*b[j][1]

    #  total += v
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
