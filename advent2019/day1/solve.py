modules = """85824
112173
142065
55390
111295
148584
123987
66433
95844
122580
146901
107700
63930
100389
139126
122243
65950
87443
137945
147755
86370
66749
133758
68317
147417
97202
75113
105996
103130
113328
128427
108580
131832
147958
137067
117676
61678
127254
51090
69924
58966
127437
144987
80181
85474
100216
119810
129946
84880
61614
107350
77076
93028
140464
86826
67901
118846
118658
63646
63328
106271
87376
90156
143507
139729
140393
70324
77304
81383
127336
144535
93496
145119
73128
103189
69519
95701
112919
104766
124188
69855
99495
147075
115498
115468
68706
51445
69871
134449
130838
105809
110721
50893
126521
81542
81384
148523
105748
93331
129279"""

from advent_lib import *

# total = 0 
# for mod in modules.split("\n"):
#     total += int(mod)//3 - 2

# print(total)
# aoc_submit(total, 1)

def get_fuel(start):
    fuel = start // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + get_fuel(fuel)

total = 0 
for mod in modules.split("\n"):
    total += get_fuel(int(mod))

print(total)
aoc_submit(total, 2)