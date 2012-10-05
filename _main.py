#########################################################
# Polargraph python Controler                           #
#########################################################
# Version 0.1 alpha                                     #
#########################################################
# Writen by Edwin Joassart < edwin AT aethernet DOT eu  #
# 05/10/2012 http://aethernet.eu                        #
#########################################################
# Use it at your own risks !                            #
#########################################################
# This is distributed under the terms                   #
# of the MIT licence as stated on :                     #
# http://opensource.org/licenses/MIT                    #
#########################################################

import Serial                                           # Don't forget you need to install pySerial
from time import sleep

#-------------------------------------------------------# VARS - You need to change those to your needs

forceLiftPen = True                                     # do you want to force a pen lift at the end of the process ?

port = "/dev/tty.usbserial-A400fYTT"                    # here is your polagraph serial connection
polarfile = 'polarfile.pg'                              # here is your exported queue file

#-------------------------------------------------------# You shouldn't need to change things after this point

debug = False                                           # pass it in verbose mode

speed = 57600                                           # serial speed

#-------------------------------------------------------#

f = open(polarfile, 'r')

ser = serial.Serial(port, speed, timeout=0)

if (debug == True): # debug stuffs
    count = 0 

while True:
    data = ser.readline(9999)
    if len(data) > 0:
        if (data.startswith('READY')):                  # wait for READY
            comment = True
            while (comment == True):                    #check if it's not a commented line
                out = f.readline()

                if (debug == True):
                    count = count + 1                   # count it anyway

                if (not out.startswith('#')):
                    comment = False

            if (debug == True):                         # echo info on screen
                print data
                print count 
                print out

            if (not out):                               # if EOF stop the loop and disconnect
                if (forceLiftPen == True):              # for security send a lift pen at the end
                    ser.write('C14,END')
                    sleep(0.2)
                    ser.write('EXEC')
                break

            ser.write(out);

        else:
            if(debug == True):
                print data

            if(data.startswith('ACK')):                 # check if the message is an ACK
                end = data.find('END');

                if (data.startswith(out[:end-4], 4, end)):  # it is so check if it's the message we sent
                    ser.write('EXEC')                   # tell the pg to exec the command 
                    if(debug == True):  
                        print 'EXEC'
                else:
                    if(debug == True):
                        print 'WTF !?'
                        print 'end'
                        print end
                        print 'out'
                        print out[:end]
                        print 'data'
                        print data[4:]
                        sleep(10)

    if (debug == True):
        sleep(0.5)

ser.close                                           # close connection