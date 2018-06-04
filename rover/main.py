import time
from controls import Rover
from arguments import Arguments
from connections import Connections

'''
This code runs the JPL Open Source Rover. It accepts a few command line arguments for different functionality
   -t : Testing mode - allows you to test commands to send to the rover emulating a signals from a controller
   -s : Attempts to connect to a Unix socket for controlling the LED screen. The screen.py script must be running
   			previous to this in order to work. It lives at ../led/screen.py
   -c : Controller flag, letting this program know what type of controller you wish to run with
   		b : Bluetooth app (default)
   		x : XBox controller (requires USB reciever)

An example line running this script to run the LED screen and with an Xbox controller
	sudo python main.py -s -c x
'''
args = Arguments()
conn = Connections()
rover = Rover()

def listener():
	'''
	Based on command line args decides which controller and sockets to open
	'''

	if args.socket:
		print "starting LED socket client"
		conn.unixSockConnect()
	elif args.connect == 'x' or args.connect == 'b':
		conn.connect(args.connect)
	else:
		conn.connect('b')

def main():
	listener()
	try:
		while True:
			v,r = conn.getDriveVals()
			rover.drive(v,r)

			if args.socket:
				try:
					conn.sendUnixData()
				except Exception:   # Don't use bare except clause, as that catches keyboard interrupts as well
					pass

	except BaseException as e:  # Use BaseException, not Exception, as the latter will not catch keyboard interrupts
		rover.killMotors()
		conn.closeConnections()
		raise

if __name__ == '__main__':
	main()
