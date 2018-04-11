import time
from controls import Rover
from arguments import Arguments
from connections import Connections

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
	if args.test:
		print "starting test mode"
	elif args.connect == 'x' or args.connect == 'b':
		conn.connect(args.connect)
	else:
		conn.connect('b')

def main():
	listener()
	c = 0
	while True:
		try:
			v,r = conn.getDriveVals()
			rover.drive(v,r)

		except Exception as e:
			#print e
			rover.killMotors()
			conn.closeConnections()
			time.sleep(0.5)
			listener()

		if args.socket:
			try:
				conn.sendUnixData()
			except Exception as e:
				print e

if __name__ == '__main__':
	main()



