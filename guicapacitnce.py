import serial
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import threading

# Path to the audio file
audio_file = "/home/prajwal/Desktop/plant_capacitive_sensing/qw.mp3"

# Path to the image file
image_file = "/home/prajwal/Desktop/plant_capacitive_sensing/qw.jpg"

# Serial port setup
ser = serial.Serial('/dev/ttyACM0', 9600)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Touch App")
        self.master.geometry("500x500")

        # Load and display the image
        self.img = Image.open(image_file)  # Use Pillow to open the image file
        self.tk_img = ImageTk.PhotoImage(self.img)  # Convert to Tkinter format
        self.panel = tk.Label(master, image=self.tk_img)
        self.panel.pack()

        # Hide the window initially
        self.master.withdraw()

    def show(self):
        self.master.deiconify()
        self.play_audio()

    def hide(self):
        self.master.withdraw()

    def play_audio(self):
        threading.Thread(target=playsound, args=(audio_file,)).start()

def main():
    root = tk.Tk()
    app = App(root)

    while True:
        data = ser.readline().decode().strip()
        print(f"Received data from serial port: {data}")

        if "touch" in data.lower():
            app.show()
        else:
            app.hide()

        root.update()

if __name__ == "__main__":
    main()

