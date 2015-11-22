from scapy.all import* # Imports scapy to Python file
icmp = ICMP() # Creates an ICMP header

icmp.type = 8 # The type value of ICMP header is set as 8 for ICMP request

icmp.code = 0 # The code value is set as 0

dst = raw_input('\n Enter the destinaton IP address : ') # Takes the destination address from the user

ip.dst = dst # Maps the destination IP address in the IP header as 

count = 0 # initializes a variable count as 0

i = 0 # initializes a variable i as 0

no = input('\n Enter the number of packets to be sent :') # Takes the input from the user for packets to be set

print '\n' # Prints a new line

# Creates a for loop , increments the counter, sends the packet using sr1 command , and analyzes packet sent and prints the lost packets.

for x in range ( 0 , no ) :

	i = i + 1

	print '\n Sending packet',i,'......',\

	reply = sr1( ip/icmp , timeout = 1 , verbose = 0 )

	if reply :

		print 'Packet Sent.'

    	continue

else :

    	print 'Packet Lost.'

    	count = count + 1

print '\n Packets sent :',no, 'Packets lost :',count, '\n'

