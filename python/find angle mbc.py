"""
angle MBC = angle MCB since AM = BM = MC
by a property of right triangle
"""

import math

ab = int(input())
bc = int(input())

if ab == bc:
    print("45°")
else:
    print(str(int(round(math.degrees(math.atan2(ab, bc))))) + "°")
    
