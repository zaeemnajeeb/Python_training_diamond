############################################################
#
#       Type hints: Dict
#
############################################################

from typing import Dict

def sum_values(d:Dict[str,int]):
    return sum([d[key] for key in d])

salary = { "john":  34000,  "sara":  27000, "pedro": 52000, "tim":   12500, "zoe":   66000 }
names = { "john":  "brown", "sara":  "smith", "pedro": "phillipe", "tim":   "tonka", "zoe":   "zidane" }

try:
    print(sum_values(salary))   # ok, salary is Dict[str,int]  
    print(sum_values(names))    # names is not Dict[str,int]
except Exception as e:
    print(e)

############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

