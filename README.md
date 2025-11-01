🎮 Wireless 2D/3D Sprite Control Using Arduino & Python (Pygame)
🧩 Project Overview

This project demonstrates real-time wireless control of a game sprite using an Arduino UNO and a joystick module, connected via an HC-05 Bluetooth module.
Joystick readings from the Arduino — representing directional and button inputs — are transmitted wirelessly to a Python application built with Pygame, which updates the sprite’s position, rotation, and color dynamically.

⚙️ Key Features

Real-time sprite movement and rotation using joystick input

Wireless Bluetooth communication through HC-05

Joystick integration for analog directional control and button press detection

Dynamic color and speed adjustments based on joystick values

Modular Python–Arduino architecture using Pygame for visualization

Safe serial communication handling to prevent port connection errors

🧠 Technologies Used

Arduino UNO

Joystick Module (2-axis + button)

HC-05 Bluetooth Module

Python 3.13

Pygame Library

PySerial for Bluetooth communication

🔄 How It Works

The Arduino reads analog values from the joystick’s X and Y axes and the digital button pin.

These values are transmitted wirelessly via the HC-05 Bluetooth module to the PC.

A Python (Pygame) script reads the data over the serial port.

The sprite’s movement, rotation, and color in the Pygame window respond in real time to joystick input.

💡 Use Cases

Wireless game control prototypes

Educational demonstrations for serial and Bluetooth communication

Interactive robotics and visualization projects

Real-time control experiments

🚀 Getting Started

Pair the HC-05 Bluetooth module with your computer.

Upload the provided Arduino sketch that reads joystick data.

Run the Python (Pygame) script to visualize the sprite’s motion.

Move the joystick — watch the sprite move, rotate, and change color wirelessly in real time!
