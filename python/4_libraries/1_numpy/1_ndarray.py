import numpy as np

one_D_arr = np.array([a for a in range(10)])

two_D_arr = np.array(
    # [[a for a in range(5)], [a for a in range(5,10)]],
    # [[a for a in range(10,15)], [a for a in range(15,20)]]
    [[1,2,3], [4,5,6], [7,8,9]]
)

three_D_arr = np.array(
    [
        [
            [1,2], [3,4]
        ], 
        [
            [5,6], [7,8]
        ],
        [
            [9,10], [11,12]
        ]
    ]
)


print("shape and size of one d array is", one_D_arr.shape, one_D_arr.size, sep=" - ")
print("shape and size of two d array is", two_D_arr.shape, two_D_arr.size, sep=" - ")
print("shape and size of three d array is", three_D_arr.shape, three_D_arr.size, sep=" - ")
