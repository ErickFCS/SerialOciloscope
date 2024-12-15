import serial
import matplotlib.pyplot as plt
from collections import deque
import time

# Set up the serial connection
ser = serial.Serial("COM7", 115200)  # Replace 'COM3' with your Arduino port

# Set up the plot
plt.ion()
fig, ax = plt.subplots()
x1 = deque(maxlen=230)
y1 = deque(maxlen=230)
x2 = deque(maxlen=230)
y2 = deque(maxlen=230)
x3 = deque(maxlen=230)
y3 = deque(maxlen=230)
x4 = deque(maxlen=230)
y4 = deque(maxlen=230)
(line1,) = ax.plot(x1, y1, label="mt1")
(line2,) = ax.plot(x2, y2, label="mt2")
(line3,) = ax.plot(x3, y3, label="mt3")
(line4,) = ax.plot(x4, y4, label="mt4")
ax.set_xlim((-20, 250))
ax.set_ylim((-600, 2200))
cant = 0
plt.legend()
plt.title("PID")
plt.xlabel("Samples")
plt.ylabel("Value")

while True:
    time.sleep(.1)
    try:
        data = ser.readline().decode().strip()
        print(data)
        data = data.split("\t")
        if data:
            print(data)
            if cant > 230:
                cant = 0
                x1.clear()
                y1.clear()
                x2.clear()
                y2.clear()
                x3.clear()
                y3.clear()
                x4.clear()
                y4.clear()
            try:
                y1.append(float(data[0]))
                x1.append(cant)
                y2.append(float(data[1]))
                x2.append(cant)
                y3.append(float(data[2]))
                x3.append(cant)
                y4.append(float(data[3]))
                x4.append(cant)
            except:
                ...
            line1.set_xdata(x1)
            line1.set_ydata(y1)
            line2.set_xdata(x2)
            line2.set_ydata(y2)
            line3.set_xdata(x3)
            line3.set_ydata(y3)
            line4.set_xdata(x4)
            line4.set_ydata(y4)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
            cant += 1
    except KeyboardInterrupt:
        break

ser.close()
