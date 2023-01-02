import numpy as np
pathmap=np.ones((5,5,5),int)
for i in range(len(pathmap)):
    for j in range(len(pathmap[0])):
        pathmap[i][j][0]=0
print(pathmap)

import numpy as np
spathmap=np.ones((5,5,5),int)
for i in spathmap:
    for j in i:
        j[0]=0
print(spathmap)