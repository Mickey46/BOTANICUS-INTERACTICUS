import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Open serial port
ser = serial.Serial('/dev/ttyACM1', 9600)  # Update the COM port accordingly

# Initialize the figure for plotting
fig, ax = plt.subplots()
xdata, ydata1, ydata2 = [], [], []
ln1, = plt.plot([], [], 'r-', label='Sensor 1')
ln2, = plt.plot([], [], 'b-', label='Sensor 2')

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 1)
    return ln1, ln2

def update(frame):
    data = ser.readline().decode().strip().split(',')
    if len(data) == 2:
        try:
            sensorValue1 = int(data[0])
            sensorValue2 = int(data[1])
        except ValueError:
            sensorValue1 = 0
            sensorValue2 = 0
    else:
        sensorValue1 = 0
        sensorValue2 = 0

    xdata.append(frame)
    ydata1.append(sensorValue1)
    ydata2.append(sensorValue2)

    ln1.set_data(xdata, ydata1)
    ln2.set_data(xdata, ydata2)

    max_y = max(max(ydata1), max(ydata2), 1)
    ax.set_ylim(0, max_y)

    if frame >= 50:
        ax.set_xlim(frame - 50, frame)

    return ln1, ln2

ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True)
plt.legend()
plt.show()

