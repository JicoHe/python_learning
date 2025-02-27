import numpy as np
import matplotlib.pyplot as plt

# 创建时间轴
t = np.linspace(0, 10, 1000)

# 单位阶跃信号 u(t)，shift为位移
def unit_step(t,shift):
    return np.where(t >= shift, 1, 0)

# 绘制图像
plt.plot(t, u, label="Unit Step Function u(t)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Unit Step Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()