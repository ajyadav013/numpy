import numpy as np
import pickle
import shelve
# dt = np.dtype([('density', np.int32)])
# x = np.array([(393),(337),(256)], dtype=dt)
# print("X",x)
# print("Internal representation", repr(x))
# lst = [
#     [3.4, 8.7, 9.9],
#     [1.1, -7.8, -0.7],
#     [4.1, 12.3, 4.8]
# ]
#A = np.array(lst, dtype=i16)
#print(A)

# dt = np.dtype([('country', 'S20'),('density', 'i4'), ('area','i4'), ('population','i4')])

# x = np.array([
#     ('Netherlands', 393, 41526, 16928800),
#     ('Netherlands1', 393, 41526, 16928800),
#     ('Netherlands2', 393, 41526, 16928800),
#     ('Netherlands3', 393, 41526, 16928800),
#     ('Netherlands4', 393, 41526, 16928800),
#     ('Netherlands5', 393, 41526, 16928800),
#     ('Netherlands6', 393, 41526, 16928800),
#     ('Netherlands7', 393, 41526, 16928800),
# ],
#              dtype=dt
# )

# print(x['country'])
cities = ["Paris", "Dijon","Lyon","Strasbourg"]
fh = open("data.pkl","w+")
s = shelve.open("data.pkl")
pickle.dump(cities,fh)
fh.close()


