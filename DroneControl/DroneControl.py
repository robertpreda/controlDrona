#!/usr/bin/python

import smbus
import math
import time 
import pygame
import libardrone
import RPi.GPIO as GPIO

#<<<<< Reading data from accelerometer >>>>>

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z, dist(x,y))
    return math.degrees(radians)

bus = smbus.SMBus(1) 

# Initial values

accel_xout = read_word_2c(0x3b)
accel_yout = read_word_2c(0x3d)
accel_zout = read_word_2c(0x3f)

accel_xout_scaled = accel_xout / 16384.0
accel_yout_scaled = accel_yout / 16384.0
accel_zout_scaled = accel_zout / 16384.0

xInit = math.floor(get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
yInit = math.floor(get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
zInit = math.floor(get_z_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	


#<<<<< Data processing and sending >>>>>
def main():
    pygame.init()
    W, H = 320, 240
    screen = pygame.display.set_mode((W, H))
    drone = libardrone.ARDrone()
    clock = pygame.time.Clock()
    running = True
    while running:
        
        if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYUP:
                drone.hover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    drone.reset()
                    running = False
                # takeoff / land
                elif accel_xout > 10000:
                    drone.takeoff()
                elif accel_xout < -10000:
                    drone.land()
                # emergency
                elif event.key == pygame.K_BACKSPACE:
                    drone.reset()
                # forward / backward
                elif x > xInit:
				    if x > xInit && x < xInit+8.5
					drone.speed = 0.1
					elif x > xInit+8.5 && x < xInit+17
					drone.speed = 0.2
					elif x > xInit+17 && x < xInit+25.5
					drone.speed = 0.3
					elif x > xInit+25.5 && x < xInit+34
					drone.speed = 0.4
					elif x > xInit+34 && x < xInit+42.5
					drone.speed = 0.5
					elif x > xInit+42.5 && x < xInit+51
					drone.speed = 0.6
					elif x > xInit+51 && x < xInit+59.5
					drone.speed = 0.7
					elif x > xInit+59.5 && x < xInit+68
					drone.speed = 0.8
					elif x > xInit+68 && x < xInit+76.5
					drone.speed = 0.9
					elif x > xInit+76.5 && x < xInit+85
					drone.speed = 1.0
					
                    drone.move_forward()
					
                elif x < xInit:
				    if x < xInit && x > xInit-8.5
					drone.speed = 0.1
					elif x < xInit-8.5 && x > xInit-17
					drone.speed = 0.2
					elif x < xInit-17 && x > xInit-25.5
					drone.speed = 0.3
					elif x < xInit-25.5 && x > xInit-34
					drone.speed = 0.4
					elif x < xInit-34 && x > xInit-42.5
					drone.speed = 0.5
					elif x < xInit-42.5 && x > xInit-51
					drone.speed = 0.6
					elif x < xInit-51 && x > xInit-59.5
					drone.speed = 0.7
					elif x < xInit-59.5 && x > xInit-68
					drone.speed = 0.8
					elif x < xInit-68 && x > xInit-76.5
					drone.speed = 0.9
					elif x < xInit-76.5 && x > xInit-85
					drone.speed = 1.0
					
                    drone.move_backward()
					
                # left / right
                elif y > yInit:
				    if y > yInit && y < yInit+8.5
					drone.speed = 0.1
					elif y > yInit+8.5 && y < yInit+17
					drone.speed = 0.2
					elif y > yInit+17 && y < yInit+25.5
					drone.speed = 0.3
					elif y > yInit+25.5 && y < yInit+34
					drone.speed = 0.4
					elif y > yInit+34 && y < yInit+42.5
					drone.speed = 0.5
					elif y > yInit+42.5 && y < yInit+51
					drone.speed = 0.6
					elif y > yInit+51 && y < yInit+59.5
					drone.speed = 0.7
					elif y > yInit+59.5 && y < yInit+68
					drone.speed = 0.8
					elif y > yInit+68 && y < yInit+76.5
					drone.speed = 0.9
					elif y > yInit+76.5 && y < yInit+85
					drone.speed = 1.0
					
                    drone.move_left()
					
                elif y < yInit:
				    if y < yInit && y > yInit-8.5
					drone.speed = 0.1
					elif y < yInit-8.5 && y > yInit-17
					drone.speed = 0.2
					elif y < yInit-17 && y > yInit-25.5
					drone.speed = 0.3
					elif y < yInit-25.5 && y > yInit-34
					drone.speed = 0.4
					elif y < yInit-34 && y > yInit-42.5
					drone.speed = 0.5
					elif y < yInit-42.5 && y > yInit-51
					drone.speed = 0.6
					elif y < yInit-51 && y > yInit-59.5
					drone.speed = 0.7
					elif y < yInit-59.5 && y > yInit-68
					drone.speed = 0.8
					elif y < yInit-68 && y > yInit-76.5
					drone.speed = 0.9
					elif y < yInit-76.5 && y > yInit-85
					drone.speed = 1.0
					
                    drone.move_right()
					
                # up / down
                elif event.key == pygame.K_UP:
                    drone.move_up()
                elif event.key == pygame.K_DOWN:
                    drone.move_down()
                # turn left / turn right
                elif z > zInit:
				    if z > zInit && z < zInit+8.5
					drone.speed = 0.1
					elif z > zInit+8.5 && z < zInit+17
					drone.speed = 0.2
					elif z > zInit+17 && z < zInit+25.5
					drone.speed = 0.3
					elif z > zInit+25.5 && z < zInit+34
					drone.speed = 0.4
					elif z > zInit+34 && z < zInit+42.5
					drone.speed = 0.5
					elif z > zInit+42.5 && z < zInit+51
					drone.speed = 0.6
					elif z > zInit+51 && z < zInit+59.5
					drone.speed = 0.7
					elif z > zInit+59.5 && z < zInit+68
					drone.speed = 0.8
					elif z > zInit+68 && z < zInit+76.5
					drone.speed = 0.9
					elif z > zInit+76.5 && z < zInit+85
					drone.speed = 1.0
					
                    drone.turn_left()
					
                 elif z < zInit:
				    if z < zInit && z > zInit-8.5
					drone.speed = 0.1
					elif z < zInit-8.5 && z > zInit-17
					drone.speed = 0.2
					elif z < zInit-17 && z > zInit-25.5
					drone.speed = 0.3
					elif z < zInit-25.5 && z > zInit-34
					drone.speed = 0.4
					elif z < zInit-34 && z > zInit-42.5
					drone.speed = 0.5
					elif z < zInit-42.5 && z > zInit-51
					drone.speed = 0.6
					elif z < zInit-51 && z > zInit-59.5
					drone.speed = 0.7
					elif z < zInit-59.5 && z > zInit-68
					drone.speed = 0.8
					elif z < zInit-68 && z > zInit-76.5
					drone.speed = 0.9
					elif z < zInit-76.5 && z > zInit-85
					drone.speed = 1.0
					
                    drone.turn_right()
                

        try:
            surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
            # battery status
            hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
            bat = drone.navdata.get(0, dict()).get('battery', 0)
            f = pygame.font.Font(None, 20)
            hud = f.render('Battery: %i%%' % bat, True, hud_color)
            screen.blit(surface, (0, 0))
            screen.blit(hud, (10, 10))
        except:
            pass

        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

    print "Shutting down...",
    drone.halt()
    print "Ok."

if __name__ == '__main__':
    main()

