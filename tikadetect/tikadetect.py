#! /usr/bin/env python
#
# Simple script that demonstrates how Apache Tika API can be called
# from Python for doing mime type detection. Uses PyJnius.
# Adapted from:
# 
# http://www.hackzine.org/using-apache-tika-from-python-with-jnius.html 
#
## If you put the jar in a non-standard location, you need to
## prepare the CLASSPATH **before** importing jnius

import os
import sys
import codecs
import argparse
import config
os.environ['CLASSPATH'] = config.tikaJar
from jnius import autoclass

## Import the Java classes we are going to need
Tika = autoclass('org.apache.tika.Tika')
Metadata = autoclass('org.apache.tika.metadata.Metadata')
FileInputStream = autoclass('java.io.FileInputStream')
tika = Tika()
meta = Metadata()

# Create command-line parser
parser = argparse.ArgumentParser(description="Mimetype detector based on Apache Tika")

def detectMagicOnly(filename):

    # Detect mimetype based on byte signature only

    stream = FileInputStream(filename)
    mimeType = tika.detect(stream, meta)
    stream.close()

    return(mimeType)

def detectMagicAndName(filename):

    # Detect mimetype based on byte signature and file name

    stream = FileInputStream(filename)
    mimeType = tika.detect(stream, filename)
    stream.close()

    return(mimeType)

def getFilesFromTree(rootDir):
    # Recurse into directory tree and return list of all files
    # NOTE: directory names are disabled here!!

    filesList=[]
    for dirname, dirnames, filenames in os.walk(rootDir):
        #Suppress directory names
        for subdirname in dirnames:
            thisDirectory=os.path.join(dirname, subdirname)

        for filename in filenames:
            thisFile=os.path.join(dirname, filename)
            filesList.append(thisFile)
    return filesList

def parseCommandLine():
    # Add arguments
    parser.add_argument('--magiconly', 
        action = "store_true", 
        dest = "magicOnlyFlag", 
        default = False, 
        help = "establish mimetype from magic bytes only (ignoring filename extension)")

    parser.add_argument('directory', 
        action = "store", 
        type = str, 
        help = "directory that will be analysed")

    # Parse arguments
    args=parser.parse_args()

    return(args)


def main():

    # Get input from command line
    args=parseCommandLine()    
    directory = args.directory
    magicOnlyFlag = args.magicOnlyFlag

    # Set encoding of the terminal to UTF-8
    if sys.version.startswith("2"):
        out = codecs.getwriter("UTF-8") (sys.stdout)
    elif sys.version.startswith("3"):
        out = codecs.getwriter("UTF-8") (sys.stdout.buffer)

    files = getFilesFromTree(directory)

    for f in files:
        # Decode filename to utf-8
        fName = f.decode("utf-8","strict")

        # Detect mime type with Tika
        if magicOnlyFlag == True:
            mimeType = detectMagicOnly(fName)
        else:
            mimeType = detectMagicAndName(fName)

        # Results to stdout
        out.write(fName + ": " +  mimeType + "\n")

main()

