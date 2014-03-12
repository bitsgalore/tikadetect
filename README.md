## About
Simple demo script to demonstrate how the [Apache Tika](https://tika.apache.org/) API can be called from Python for doing mime type detection. Access to the Java API is done using [PyJnius](http://pyjnius.readthedocs.org/en/latest/).

Adapted from: 

[http://www.hackzine.org/using-apache-tika-from-python-with-jnius.html](http://www.hackzine.org/using-apache-tika-from-python-with-jnius.html )

Note that this not intended as a production-ready tool! My main reason for writing this was to get more familiar with *PyJnius* and the *Tika* API. So far I've only managed to test this using Python 2.7 running under Linux Mint. Other platforms may work ... or maybe not!


##Installation of PyJnius and its dependencies
This script uses [PyJnius](http://pyjnius.readthedocs.org/en/latest/) for accessing the Tika Java classes. I found several guides on the installation of PyJnius and its dependencies, and none of them quite worked for me (*python-dev* in particular isn't explicitly mentioned anywhere). After some experimentation the following did the trick for me under Linux Mint (haven tried under Windows yet): 

###Step 1: install Cython

    sudo apt-get install cython
    
###Step 2: install python-dev

    sudo apt-get install python-dev

###Step 3: clone & install pyjnius

    git clone https://github.com/kivy/pyjnius.git
    cd pyjnius
    sudo python setup.py install

###Step 4: download & install Apache Tika
Download the latest runnable jar from:

[https://tika.apache.org/download.html](https://tika.apache.org/download.html)

Then save it wherever you prefer.

Done!

##Configuration
Open *config.py* in a text editor and update *tikaJar* to the location of the *Tika* JAR on your system (see above).


##Command line use

###Usage

    python tikadetect.py [-h] [--magiconly] directory

This will result in a *recursive* scan of *directory* and all its subdirectories. Output is written to *stdout*, using the following format dfor each analysed file:

    /path/to/file.ext: mimetype

###Positional arguments

`directory`: directory that will be analysed

###Optional arguments

`-h, --help`:   show help message and exit
`--magiconly`:  establish mimetype from magic bytes only (ignoring filename extension)

Note that by default mimetype detection is done using a combination of magic bytes and filename extensions (the latter can be disabled using the *--magiconly* switch).

##Documentation of Tika methods
See this link (describes Tika 1.5), and have a look at the *detect* methods (which are called in the script):

[https://tika.apache.org/1.5/api/org/apache/tika/Tika.html](https://tika.apache.org/1.5/api/org/apache/tika/Tika.html)
