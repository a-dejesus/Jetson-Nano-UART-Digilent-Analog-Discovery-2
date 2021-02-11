
# UART Python GPIO output check program using Waveforms and Digilent Analog Discovery 2

simple python script using Jetson Nano UART GPIO header

Digilent Analog Discovery 2 as a protocol analyzer 

This is an easier to implement version of the original code that's on JetsonHacks, readline is used instead of read, "q" to exit program. Original code displays single character, this code is able to enter more letters and doesn't display "b" that original does.

Original Article on JetsonHacks:https://www.jetsonhacks.com/2019/10/10/jetson-nano-uart/

I made this to visually see what my Jetson nano was transmitting and receiving before I started to implement communication with another device

!! Before you start using UART with this serial port, make sure you've disabled the serial console nvgetty service. You can find why to do that in the original article. Commands are 

  $ systemctl stop nvgetty
  
  $ systemctl disable nvgetty
  
  $ udevadm trigger
  
  # You may want to reboot instead

The script requires py-serial. Command to install

  $ sudo apt-get install python3-serial

Command to run script is

  $ sudo python3 uart_mod.py
  
  
Analog Discovery 2
Before you start, you need to download Waveforms software to view Analog Discovery 2 output

Link to Waveforms download
https://mautic.digilentinc.com/waveforms-download  

Once you've downloaded the software, it will autodetect your device. At welcome screen, go to "Protocol" button. Set Rate to 115.2k and Ending to Line Feed.
  
This script 

Transmits input from waveforms on your computer to the Jetson nano and then is echoed back to the receive of waveforms. 

jetson to discovery pin connections

pin 8  TXD -> dio 1 RXD     
pin 10 RXD  ->  dio 0 TXD




