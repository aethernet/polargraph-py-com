polargraph-py-com
=================

Version 0.1 alpha

polargraph python communicator and driver

The polargraph project can be found at http://polargraph.co.uk and is a wonderfull project

The Problem :
-------------
The polargraph controler is build with the java framework processing, wich is an amazing tool for art and rapid prototyping.

But :
	* it require to have a computer attached to the arduino to drive the polargraph
	* the gui is so heavy that it turns my macbook pro into an hoven. (cpu 100%)
	* i want to use a wifi router with openwrt and a usb port to wirelessly pilot the polargraph

The Solution :
--------------
As :
	* the communication protocol is damn simple and build upon the usb/serial of the arduino
	* the polargraph controler can export the serial commands in a file
	
	I just wrote this small python script which :
		* open a serial communication with the polargraph
		* send one line of a file for each 'READY' message, check the ACK and then send a EXEC
		* send a pen lift message at the end of file to be sure security (optional)

The tools :
-----------
	* a pivotal tracker roadmap is availlable here : https://www.pivotaltracker.com/projects/638973
	* a pivotal to github bridge is set so please add the id of the related story in pivotal in the comment of the commit ( [#000000] to link to a story and [fix #0000000] to mark it as fixed ) if you submit code to this project. You'll find more info in the API help section of pivotal tracker.

How it works ?
--------------
	* Install Python (2.x) ( http://python.org/ )
	* Install pySerial ( http://pyserial.sourceforge.net/ )
	* Open the polargraph controler as you usually do, create your whole commands queue and export it to a file
	* Open the _main.py file
	* Set the variables to your needs ( especially the port and polarfile )
	* open a terminal and launch the script ( $ python _main.py )
	* enjoy ( if you didn't set the debug var to True the script is silent while working )

Licence :
---------
	* The whole shit is released without any guarantee and is put under MIT licence ( this version -> http://opensource.org/licenses/MIT )

	(c)2012 - Edwin Joassart < edwin AT aethernet DOT eu > - aethernet.eu