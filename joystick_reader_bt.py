import pygame
import time
# ==== CONFIGURATION ====
BLUETOOTH_PORT = "COM10"
BAUD_RATE = 38400
try:
    bt = serial.Serial(BLUETOOTH_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {BLUETOOTH_PORT}")
    time.sleep(2)  # allow connection to stabilize
except Exception as e:
    print(f"Bluetooth connection failed: {e}")
    exit()
# ==== PYGAME SETUP ====
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bluetooth Joystick Sprite Controller")
clock = pygame.time.Clock()
# Sprite setup
sprite = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
color = (0, 200, 255)
# Motion control sensitivity
SPEED = 5
# ==== MAIN LOOP ====
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Read Bluetooth data
    try:
        if bt.in_waiting > 0:
            line = bt.readline().decode().strip()
            if line:
                # Expected: x,y,joyBtn,jump,wave,dance
                parts = line.split(",")
                if len(parts) == 6:
                    x, y = int(parts[0]), int(parts[1])
                    joyBtn = int(parts[2])
                    jump = int(parts[3])
                    wave = int(parts[4])
                    dance = int(parts[5])
                    # Map joystick movement (0–1023) to -1..1 range
                    x_offset = (x - 512) / 512
                    y_offset = (y - 512) / 512
                    # Move sprite
                    sprite.x += int(x_offset * SPEED)
                    sprite.y += int(y_offset * SPEED)
                    # Button actions
                    if jump:
                        color = (255, 0, 0)
                    elif wave:
                        color = (0, 255, 0)
                    elif dance:
                        color = (255, 255, 0)
                    else:
                        color = (0, 200, 255)
                    # Keep sprite on screen
                    sprite.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
    except Exception as e:
        print("Read error:", e)
    # Draw everything
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, color, sprite)
    pygame.display.flip()
    clock.tick(30)
bt.close()
pygame.quit()