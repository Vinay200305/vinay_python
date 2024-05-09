Q-1 : Why Do You Use the Zip () Method in Python? 

=> In Python, the zip() function is used to combine two or more lists into a single iterable, where elements 
   from corresponding positions are paired together.

=> The resulting iterable contains tuples, where the first element from each list is paired together, 
   the second element from each list is paired together, and so on.

EXAMPLE : 
    name = [ "MANAV", "KETAN", "RADHA", "YAGNESH" ]
    roll_no = [ 4, 1, 3, 2 ]
    mapped = zip(name, roll_no)
    print(set(mapped))