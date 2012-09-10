polargraph-py-com
=================

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
	* the communication protocol is dawn simple and build upon the usb/serial of the arduino
	* the polargraph controler can export the serial commands in a file
	* this project is a very simple script that will open the serial communcation, read the commannd file and send it to the polargraph without the need of a gui

	* the second version will be used to 

The tools :
-----------
	* a pivotal tracker roadmap is availlable here : https://www.pivotaltracker.com/projects/638973
	* a pivotal to github bridge is set so please add the id of the related story in pivotal in the comment of the commit ( [#000000] to link to a story and [fix #0000000] to mark it as fixed ) if you submit code to this project. You'll find more info in the API help section of pivotal tracker.