#Wireless 3D Sprite Control Using Arduino & Python

Project Overview:
This project demonstrates real-time wireless control of a 3D sprite using an Arduino UNO equipped with an MPU6050 motion sensor and an HC-05 Bluetooth module. Sensor readings from the Arduino — including accelerometer and gyroscope data — are transmitted wirelessly to a Python application running the Ursina 3D engine, which updates the sprite’s position, rotation, and color dynamically.

Key Features:

Real-time 3D sprite control via motion input

Wireless communication using HC-05 Bluetooth module

Accelerometer and gyroscope integration via MPU6050

Dynamic color changes and rotation based on tilt

Fully modular Python code using Ursina for 3D visualization

Safe serial handling to prevent port errors

Technologies Used:

Arduino UNO

MPU6050 Motion Sensor

HC-05 Bluetooth Module

Python 3.13

Ursina 3D Engine

PySerial

How It Works:

Arduino reads motion data from MPU6050.

Data is transmitted wirelessly via HC-05 to a paired PC.

Python script reads Bluetooth data and updates a 3D sprite in real-time.

Sprite movement, rotation, and color reflect the Arduino’s orientation.

Use Cases:

Educational demonstration of wireless sensor control

Motion-controlled gaming prototypes

Interactive visualization projects

Getting Started:

Pair HC-05 Bluetooth module with your PC.

Upload the Arduino sketch to your Arduino UNO.

Run the Python script to visualize and control the 3D sprite.
