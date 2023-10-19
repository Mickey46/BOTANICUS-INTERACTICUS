import serial
import sounddevice as sd
import numpy as np

# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)  # Update the COM port accordingly

sample_rate = 44100
duration = 1.0  # seconds

# Initialize the reservoir state
reservoir_state = 0

def callback(outdata, frames, time, status):
    global reservoir_state
    if status:
        print(status)
    data = ser.readline().decode().strip()
    if data == "Touch":
        reservoir_state = np.random.randint(100, 1000)
    else:
        reservoir_state = int(reservoir_state * 0.99)  # Decay the reservoir state

    t = (np.arange(frames) + callback.counter) / sample_rate
    callback.counter += frames

    wave = 0.5 * np.sin(2 * np.pi * reservoir_state * t)
    outdata[:] = wave.reshape(-1, 1)

callback.counter = 0

# Start streaming
with sd.OutputStream(callback=callback, channels=1, samplerate=sample_rate, dtype='float32'):
    input("Press Enter to stop...")

