import RPi.GPIO as GPIO
import time
import random

ir_l = 7
ir_m = 22 
ir_r = 24
mr_r1 = 15
mr_r2 = 16
mr_l1 = 18
mr_l2 = 22

GPIO.setmode( GPIO.BOARD )

GPIO.setup( mr_r1, GPIO.OUT )
GPIO.setup( mr_r2, GPIO.OUT )
GPIO.setup( mr_l1, GPIO.OUT )
GPIO.setup( mr_l2, GPIO.OUT )
GPIO.setup( ir_l, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( ir_m, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( ir_r, GPIO.IN, pull_up_down=GPIO.PUD_UP )

def motor_r_forward():
	
	GPIO.output( mr_r1, 0 )
	GPIO.output( mr_r2, 1 )

def motor_r_reverse():
	
	GPIO.output( mr_r1, 1 )
	GPIO.output( mr_r2, 0 )

def motor_l_forward():
	
	GPIO.output( mr_l1, 1 )
	GPIO.output( mr_l2, 0 )

def motor_l_reverse():
	
	GPIO.output( mr_l1, 0 )
	GPIO.output( mr_l2, 1 )

def move_forward():

	motor_r_forward()
	motor_l_forward()

def move_back():

	motor_r_reverse()
	motor_l_reverse()

def turn_right():

	motor_r_reverse()
	motor_l_forward()

def turn_left():

	motor_r_forward()
	motor_l_reverse()

def stop():

	GPIO.output( mr_r1, 0 )
	GPIO.output( mr_r2, 0 )
	GPIO.output( mr_l1, 0 )
	GPIO.output( mr_l2, 0 )

judgement = { 1 : turn_left , 2 : turn_right }

try:

	while True:

		ir_lin = GPIO.input( ir_l )
		ir_min = GPIO.input( ir_m )
		ir_rin = GPIO.input( ir_r )

		if ir_lin == 0 and ir_min == 1 and ir_rin == 0:

			move_forward()

		elif ir_lin == 1 and ir_min == 0 and ir_rin == 0:

			turn_left()

		elif ir_lin == 0 and ir_min == 0 and ir_rin == 1:

			turn_right()

		elif ir_lin == 1 and ir_min == 1 and ir_rin == 0:
		
			turn_left()

		elif ir_lin == 0 and ir_min == 1 and ir_rin == 1:

			turn_right()

		elif ir_lin == 1 and ir_min == 1 and ir_lin == 1:
		        
			move_random = random.choice( [ 1, 2 ] )
			judgement[ move_random ]()	
			time.sleep( 0.3 )
		
		else:
			
			stop()


except KeyboardInterrupt:

	GPIO.cleanup()
		
