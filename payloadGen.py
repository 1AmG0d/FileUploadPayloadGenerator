#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import configparser
import logging
import os
import shutil
import ast

__config__ = './cfg/payloadGen.cfg'
__sections__ = [
    'PayloadDirectory',
    '_XSSName',
    '_FileTypeBypass',
    'FileBypassChars'
    ]

__author__ = 'IΛMGӨÐ'
__date__ = '2019-05-01'
__version__ = '9.9.9'
__description__ = '''Given A File, This Will Produce Various Files
                    That Can Be Used During Web Penetration Testing Engagements.
                  '''

def printMessage(level, message):
    if level == "DEBUG":
        logging.debug(message)
    elif level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "CRITICAL":
        logging.critical(message)

def createDir(directory):
    if args.verbose:
        printMessage("DEBUG", "Checking If " + '"' + directory + '"' + " Directory Exists" )
    if not os.path.exists(directory):
        if args.verbose:
            printMessage("DEBUG", '"' + directory + '"' + " Does Not Exist. Creating Directory")
        try:
            os.makedirs(directory)
            if args.verbose:
                printMessage("DEBUG", '"' + directory + '"' + " Directory Created")
        except Exception as e:
            printMessage("CRITICAL", "Exception Occurred:\n" + str(e))
            exit()
    else:
        if args.verbose:
            printMessage("DEBUG", '"' + directory + '"' + " Directory Already Exists")

def createXSSNamePayload(dir, file, payload, ext):
    if args.verbose:
        printMessage("DEBUG", "Attempting To Copy: " + file + " --> " + dir + '/' + payload + ext)
    try:
        shutil.copy(file, dir + '/' + payload + ext)
    except Exception as e:
            printMessage("CRITICAL", "Exception Occurred:\n" + str(e))
            exit()

def createExtBypassPayload(dir, file, payload, bChar, base):
    if args.verbose:
        printMessage("DEBUG", "Attempting To Copy: " + file + " --> " + dir + '/' + base + bChar + payload)
    try:
        shutil.copy(file, dir + '/' + base + bChar + payload)
    except Exception as e:
            printMessage("CRITICAL", "Exception Occurred:\n" + str(e))
            exit()

def main():
    printMessage("INFO", "Program Starting")

    for file in args.file:
        if args.verbose:
            printMessage("DEBUG", "Grabbing Base File Name From: " + file)
            printMessage("DEBUG", "Grabbing File Extension From: " + file)
        base = os.path.basename(file)
        fExt = os.path.splitext(base)[1]
        fExtDir = fExt.replace(".", "_").upper()

        if args.verbose:
            printMessage("DEBUG", "File BaseName: " + base)
            printMessage("DEBUG", "File Extension: " + fExt)

        createDir(fExtDir)

        printMessage("INFO", "Reading Payload Directories From Config File")
        section_0 = config.sections()[0]
        keys = ast.literal_eval(config.get(section_0, config.options(section_0)[0]))

        for key in keys:
            if (args.all or args.xss) and key == "_XSSName":
                printMessage("INFO", "Reading XSS Payload From Config File")
                section_1 = config.sections()[1]
                dir = fExtDir + "/" + key
                createDir(dir)
                payloads = ast.literal_eval(config.get(section_1, config.options(section_1)[0]))
                for payload in payloads:
                    createXSSNamePayload(dir, file, payload, fExt)

            elif (args.all or args.ext) and key == "_FileTypeBypass":
                printMessage("INFO", "Reading File Extension Payloads From Config File")
                section_2 = config.sections()[2]
                section_3 = config.sections()[3]
                dir = fExtDir + "/" + key
                createDir(dir)
                payloads = ast.literal_eval(config.get(section_2, config.options(section_2)[0]))
                bChars = ast.literal_eval(config.get(section_3, config.options(section_3)[0]))
                for payload in payloads:
                    for bChar in bChars:
                        pass
                        createExtBypassPayload(dir, file, payload, bChar, base)
            else:
                printMessage("ERROR", '"' + key + '"'  + " Does Not Exist In Config File")

            printMessage("INFO", "Program Complete!")

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    parser = argparse.ArgumentParser(description=__description__, add_help=False)
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-f", "--file",
                        help="files to create payloads from",
                        nargs='+',
                        required=True)
    optional.add_argument("-a", "--all",
                        action='store_true',
                        help="create xss file payloads and file extension bypass payloads (Default)")
    optional.add_argument("-e", "--ext",
                        action='store_true',
                        help="create file extension bypass payloads")
    optional.add_argument("-x", "--xss",
                        action='store_true',
                        help="create xss file payloads")
    optional.add_argument("-h", "--help",
                        action='help',
                        help="show this help message and exit")
    optional.add_argument("-v", "--verbose",
                        action="store_true",
                        help="display information verbosely")

    args = parser.parse_args()
    config = configparser.ConfigParser()

    print("Payload Generator: XSS in filename & Extension bypass")
    print("By: " + __author__)

    printMessage("INFO", "Loading Config File")
    config.read(__config__)
    for section in __sections__:
        if section not in config:
            printMessage("ERROR", '"' + section + '"'  + " Section Does Not Exist In Config File")
            exit()

    if not args.ext and not args.xss:
        args.all = True

    main()
