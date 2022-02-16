"""
Determining the flip coin using Random Function
"""

import random
output = (random.uniform(0 , 1))
if output < 0.5:
    print(((output/1)*100),"tail")
else:
    print(((output/1)*100) ,"head")