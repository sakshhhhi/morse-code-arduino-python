"""Morse Code Sender - Tkinter GUI that sends dots/dashes to an Arduino over serial.

Usage:
    python morse_gui.py                # uses default port
    python morse_gui.py COM5           # Windows
    python morse_gui.py /dev/ttyACM0   # Linux/Mac
"""
import sys
import time
import tkinter as tk
import serial

PORT = sys.argv[1] if len(sys.argv) > 1 else "COM3"
BAUD = 9600

# Opening the port resets the Arduino, so wait for it to boot
arduino = serial.Serial(PORT, BAUD)
time.sleep(2)

morse_buffer = ""  # current pattern, e.g. ".-"

MORSE_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
}


def send_dot():
    global morse_buffer
    arduino.write(b".")
    morse_buffer += "."
    print("Dot (.) clicked")
    print("Current Buffer:", morse_buffer)


def send_dash():
    global morse_buffer
    arduino.write(b"-")
    morse_buffer += "-"
    print("Dash (-) clicked")
    print("Current Buffer:", morse_buffer)


def decode_letter():
    global morse_buffer
    letter = MORSE_DICT.get(morse_buffer, "?")
    print("Decoded Letter:", letter)
    morse_buffer = ""  # reset for next letter


def quit_app():
    print("Closing application...")
    arduino.close()
    root.destroy()


root = tk.Tk()
root.title("Morse Code Sender")

tk.Button(root, text="Dot (.)", width=20, command=send_dot).pack(pady=10)
tk.Button(root, text="Dash (-)", width=20, command=send_dash).pack(pady=10)
tk.Button(root, text="Decode Letter", width=20, command=decode_letter).pack(pady=10)
tk.Button(root, text="Quit", width=20, fg="red", command=quit_app).pack(pady=20)

root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
