import matplotlib.pyplot as plt
import numpy as np
im = plt.imread("bitmaps/welcome_screen_2.jpg", format='jpeg')
# arbitrarily take red channel
im_r = im[:, :, 0]

with open("bitmaps/out.txt", "wt") as fp:
    for idx, y_x in enumerate(np.argwhere(im_r < 200)):
        y,x = y_x
        # print(f"({x}, {y}),", file=fp, end='\n' if idx%5==4 else '' )
        print(f"{y}, ", file=fp, end='\n' if idx%15==14 else '' )
