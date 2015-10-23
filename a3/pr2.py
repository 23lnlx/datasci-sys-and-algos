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
    table_name = record[0]
    order_id = record[1]
    words = record[2:]
#    for w in words:
    mr.emit_intermediate(order_id, record)



def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    lists = list_of_values[1:]
    for v in lists:
        mr.emit((list_of_values[0]+v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
