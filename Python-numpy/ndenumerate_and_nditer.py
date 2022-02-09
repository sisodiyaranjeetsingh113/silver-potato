import numpy as np
array_numpy=np.array([[[2],[2]],[[3],[4]],[[5],[6]]])
for i in np.nditer(array_numpy):
    print(i)
for index, i in np.ndenumerate(array_numpy):
    print(index,":",i)