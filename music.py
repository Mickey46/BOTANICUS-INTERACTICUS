import serial
import wave
import numpy
import pyaudio

# Define tones
tones = {
    'Touch': 440  # Frequency for the tone (in Hz)
}

# Function to generate a tone
def generate_tone(frequency, duration):
    sample_rate = 44100
    samples = numpy.arange(duration * sample_rate)
    wave = 0.5 * numpy.sin(2 * numpy.pi * frequency * samples / sample_rate)
    return wave

# Function to play a tone
def play_tone(wave, duration):
    sample_rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    data = (wave * 32767).astype(numpy.int16).tobytes()
    stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)  # Update the COM port accordingly

while True:
    data = ser.readline().decode().strip()
    if data in tones:
        freq = tones[data]
        wave = generate_tone(freq, 1)  # Generate a 1-second tone
        play_tone(wave, 1)
