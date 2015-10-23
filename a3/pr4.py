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
    two_pers = tuple(sorted(record))
    mr.emit_intermediate(two_pers,1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for sym_friends in list_of_values:
        total += 1
    if total == 1:
        mr.emit(key)
        mr.emit((key[1],key[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
