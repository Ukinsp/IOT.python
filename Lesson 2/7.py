import numpy as np
a = np.array([3, 2, 5, 4, 1, 7])

for i in range(3):
    x = np.argmin(a)
    print(x)
    a[x]=np.max(a)

# x = np.argmin(a)
# print(x)
# a[x]=np.max(a)
#
# x = np.argmin(a)
# print(x)
# a[x]=np.max(a)

