import numpy as np

while True:
    try:
        r = np.random.rand(10000, 10000)
        rp = np.linalg.inv(r)
        print(rp)
    except:
        print("Error")