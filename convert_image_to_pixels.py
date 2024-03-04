import matplotlib.pyplot as plt
import numpy as np
im = plt.imread("cat_2_l.jpg", format='jpeg')
# take red channel
im_r = im[:, :, 0]
# print indexes where value is less than 10 (black)
for y,x in np.argwhere(im_r < 200):
    print(f"(top_x + {x}, top_y + {y}),")
# plt.imshow(im_r)
# plt.show()

(1,0),(2,0),(1,1),(2,1),(0,2),
(1,2),(2,2),(2,3),(3,3),(5,3),
(1,4),(2,4),(3,4),(4,4),(5,4),
(1,5),(2,5),(3,5),(4,5),(5,5),
(1,6),(2,6),(3,6),(4,6),(2,7),
(3,7),(2,8),(3,8),(3,9),(4,9),
(4,10),(3,11),(4,11),(3,12),(2,13),
(3,13),(2,14)