#### What is Arduino?
Strictly speaking, Arduino is the combination of:
* an Arduino Board: a microcontroller board. The most popular board is the Arduino Uno based on the ATmega328 microcontroller from Microchip's (formerly Atmel) AVR family but today it can be almost any microcontroller from any manufacturer;
* the Arduino IDE: a simplified and easy-to-use Integrated Development Environment (IDE) used to create small programs -- commonly referred to as Sketches. There exists an online IDE, Arduino Create, and a downloadable offline IDE;
* the Arduino API: a large library of functions (the Application Programming Interface or API) that can be used in user programs -- commonly referred to as the Arduino Language;
* the Arduino Bootloader: a special program pre-loaded into the Arduino Board and compatible with the Arduino IDE that allows uploading of programs to the board without requiring special tools; usually over USB.

#### Installation of the Arduino IDE
* Offline - The offline Arduino IDE must be installed on a computer. There are versions for Windows, Linux and Mac OS. For Windows it can be downloaded as a ZIP archive, an installer and even as a Windows App. For the other platforms only archives exist. Note that the Arduino IDE uses Java, so make sure you have that installed as well.
* Online - uses an Internet browser and requires the installation of a browser plug-in to allow the online IDE to load programs into the Arduino board.

#### How to setup the Arduino IDE for my Arduino Board?
* Connect the Arduino Board to the computer. Make sure it is recognized by the computer and that a port is created for it. If it isn't, you may have to install a driver for your board first.
* Start the Arduino IDE. From the menu choose 'Tools' -> 'Board:' and scroll through the list until you find your board. Select it.
* From the menu choose 'Tools' -> 'Port' and select the port that was created during step 1. If the port is not listed go back to step 1 and fix the problem.
