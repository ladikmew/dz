import numpy as np


def punkt(x0, y0, vy0, vx0, v0, m, k1, p, t, vxall, vyall, vtall):
    t += 0.1
    p += 1
    vy1 = vy0 + (-(9.8) - (k1 * vy0 / m) * t)
    vx1 = vx0 - ((k1 * vx0) / m) * t
    y1 = y0 + vy1 * t
    x1 = x0 + vx1 * t
    vxall.append(x1)
    vyall.append(y1)
    vtall.append(t)
    #     L0 = np.arctan(vy1/vx1)
    if p < 10:
        punkt(x1, y1, vy1, vx1, v0, m, k1, p, t, vxall, vyall, vtall)
    else:
        print(vxall)
        print(vyall)
        print(vtall)


vxall = []
vyall = []
vtall = []
punkt(0, 0, 0, 0, 10, 0.235, 0.1, 0, 0.1, vxall, vyall, vtall)
