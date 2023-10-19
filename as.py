import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)  # Update the COM port accordingly

# Initialize the figure for plotting
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 3000)
    return ln,

def update(frame):
    data = ser.readline().decode().strip()
    if 'Touch' in data:
        yvalue = 2000  # You can adjust this value based on your setup
    else:
        yvalue = 0
    xdata.append(frame)
    ydata.append(yvalue)
    if len(xdata) > 50:
        xdata.pop(0)
        ydata.pop(0)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True)
plt.show()

