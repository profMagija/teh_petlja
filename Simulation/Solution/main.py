import matplotlib.pyplot as plt
import numpy as np

DELTA_T = 0.01
G = -9.81
DRAG_K = -0.99
DEG = np.pi / 180.0

def get_initial_cond(vstart, alpha):
    return 0.0, 0.0, vstart * np.cos(alpha), vstart * np.sin(alpha)

def sim_stop(x, y):
    return y < 0

def norm_2(x, y):
    return np.sqrt(x * x + y * y)

def integrate_speed(vx, vy, dt):
    v = norm_2(vx, vy)
    drag_a = DRAG_K * v * v
    
    drag_a_x = drag_a * (vx / v)
    drag_a_y = drag_a * (vy / v)

    vx1 = vx + drag_a_x * dt
    vy1 = vy + G * dt + drag_a_y * dt
    return vx1, vy1

def integrate_pos(x, y, vx, vy, dt):
    x1 = x + vx * dt
    y1 = y + vy * dt
    return x1, y1

def update_max_h(max_h, x, y):
    if y > max_h:
        return y
    else:
        return max_h

def update_max_range(max_range, x, y):
    if y > 0 and x > max_range:
        return x
    else:
        return max_range

def plot_xy(xs, ys):
    axis = plt.axes()
    axis.set_aspect(1)
    plt.plot(xs, ys)
    plt.show()

def main():
    
    x, y, vx, vy = get_initial_cond(10.0, 45 * DEG)
    x_arr, y_arr = [x], [y]
    max_h = 0
    max_range = 0

    while not sim_stop(x, y):
        vx, vy = integrate_speed(vx, vy, DELTA_T)
        x, y = integrate_pos(x, y, vx, vy, DELTA_T)

        x_arr.append(x)
        y_arr.append(y)

        max_h = update_max_h(max_h, x, y)
        max_range = update_max_range(max_range, x, y)

    plot_xy(x_arr, y_arr)
    print('max_h =', max_h)
    print('max_range =', max_range)


if __name__ == '__main__':
    main()