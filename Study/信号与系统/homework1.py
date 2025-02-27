import numpy as np
import matplotlib.pyplot as plt

# 创建时间轴
t = np.linspace(-1, 4, 1000)


# 定义单位阶跃信号 u(t) 函数
def u_t(time, shift):
    return np.where(time >= shift, 1, 0)


# 计算 f(t)
f = -(t-1)* (u_t(t, 0) - u_t(t, 1))

# 绘制信号
plt.plot(t, f, label="f(t)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("f(t)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
