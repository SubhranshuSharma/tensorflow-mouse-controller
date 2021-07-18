# tensorflow-mouse-controller
This project uses tensorflow lite for microcontrollers  to control mouse using eyes or hands. it's made using teachable machine website.

Camera used- ov7670

Board used- Arduino 33 ble sense

Getting Started:

1. Use the wiring imformation below to make connections.
2. Upload arduino code of choice to arduino 33 ble sense.
3. Make sure all other serial ports are free and connect arduino to pc.
4. Room should not be dark more the light better it works.
5. Run the mouse.exe file.
6. Although mouse only moves 15 pixels every 3 seconds, slam the curser in right corner to stop mouse.exe if mouse goes crazy don't do it otherwise.
7. Use task manager to close mouse.exe when you are done.

ov7670 Camera Pin Name ->	Arduino pin name

3.3v	    ->  3.3v

GND	    ->    GND (either pin marked GND is fine)

SCL/SIOC  -> A5

SDA/SIOD  ->   A4

VS/VSYNC  ->     D8

HS/HREF   ->       A1

PCLK	    ->      A0

MCLK/XCLK ->      D9

D7	       ->       D4

D6	       ->         D6

D5	       ->       D5

D4	       ->         D3

D3	       ->         D2

D2	       ->         D0 / RX

D1	       ->         D1 / TX

D0	       ->         D10 

How to move mouse:

1. Look into dataset folder in arduino code folder to see what it should look like to the camera)
2. The background should be a out of focus white wall(any colour other than black should work but not great) You should not be in the background.
3. Make the camera focus on near objects by rotating lens clockwise.
4. It jumps 15 pixels every 3 second to change it go to model_settings.cpp and add your required number of pixels at end of up, down, right, left, hold and dclick like shown below
   
const char* kCategoryLabels[kCategoryCount] = {
    "up 30","down 30","right 30","left 30","hold 30","dclick 30",
};

Troubleshooting:
1. If you are having trouble using mouse.exe file, its just bootable version of mouse.py file to use mouse.py file download python and all imported liberaries and comment out all the lines(from port select section) other than line consisting of your board's port number.
   mouse.py file will also print all the serial port devices if there are more than one than remove other devices
