import time
from machine import Pin
from neopixel import NeoPixel

# 定义红、绿、蓝三种颜色
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 22引脚连接灯带，灯珠数量30
pin = Pin(20, Pin.OUT)
np = NeoPixel(pin, 30)

KEY = Pin(4, Pin.IN, Pin.PULL_UP)  # 构建KEY对象

# 颜色列表
colors = [RED, GREEN, BLUE]
current_color_index = 0  # 当前颜色索引

# LED状态翻转函数
def fun(KEY):
    global current_color_index
    time.sleep_ms(10)  # 消除抖动
    if KEY.value() == 0:  # 确认按键被按下
        current_color_index = (current_color_index + 1) % len(colors)  # 切换到下一个颜色
        np.fill(colors[current_color_index])  # 设置当前颜色
        np.write()  # 写入数据

KEY.irq(fun, Pin.IRQ_FALLING)  # 定义中断，下降沿触发

# while True:
#     time.sleep(1)  # 主循环保持运行