#!/usr/bin/python3
import time
import serial

print("UART testing, press q and enter to quit")

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,	#8N1 Protocol
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a simple header
    serial_port.write("UART testing\r\n".encode())

    serial_port.flushInput()
    while True:

        if serial_port.inWaiting() > 0:
            data = serial_port.readline()	# readline is used so input can be whole sentences or words
            print(data.decode('utf-8'))
            serial_port.write(data)
            # if we get a carriage return, add a line feed too
            # \r is a carriage return; \n is a line feed
            # This is to help the tty program on the other end 
            # Windows is \r\n for carriage return, line feed
            # Macintosh and Linux use \n

            if data == "\r".encode():
                # For Windows boxen on the other end
                serial_port.write("\n".encode())
                
            if data == "q\n".encode():	# if incoming input is q + enter(\n), 
               serial_port.close()	# close serial ports 
               break			# exit program



except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
