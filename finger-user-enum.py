#!/usr/bin/env python3

import argparse
import os
import time


START_MESSAGE = """
█████ █████ █   █  ████ █████ ████       █   █ █████ █████ ████          █████ █   █ █   █ █   █ 
█       █   ██  █ █     █     █   █      █   █ █     █     █   █         █     ██  █ █   █ ██ ██ 
████    █   █ █ █ █  ██ ████  ████       █   █ █████ ████  ████          ████  █ █ █ █   █ █ █ █ 
█       █   █  ██ █   █ █     █   █      █   █     █ █     █   █         █     █  ██ █   █ █   █ 
█     █████ █   █  ███  █████ █   █      █████ █████ █████ █   █         █████ █   █ █████ █   █ 
"""


def user_enum(wordlist, host, user='n!0t_user', delay='0.5'):
    print(START_MESSAGE)
    print("="*100)
    print(f"Using wordlist: {wordlist} on host: {host} with delay: {delay}")

    if user != None:
        print(f'Checking user: {user}')
        pc = os.popen(f'finger {user}@{host}').read()
        print(pc)
        if 'no such user' not in pc:
            print(f'Valid user: {user}')
    else:
        wordlist = open(wordlist, 'rb').readlines()

        for word in wordlist:
            word = word.strip()
            print(f'Checking user: {word}', end='\r')
            pc = os.popen(f'finger {word}@{host}').read()
            if 'no such user' not in pc:
                print(f'Valid user: {word}')
            time.sleep(float(delay))
    return


def main():
    parser = argparse.ArgumentParser(description="Finger User Enum")

    parser.add_argument("-w", "--wordlist",
                        help="Specify a wordlist file", default='/usr/share/wordlists/rockyou.txt')

    parser.add_argument("-p", "--port", type=int,
                        help="Specify a port number", default=79)

    parser.add_argument("--host", help="Specify a Host number")

    parser.add_argument(
        "-u", "--user", help="Specify a username")

    parser.add_argument("-H", "--custom_help", action="store_true",
                        help="Show this help message and exit")

    parser.add_argument(
        "-d", "--delay", help="Specify a delay time in seconds", default=0.5)

    try:
        args = parser.parse_args()
        if args.custom_help:
            parser.print_help()
        elif args.wordlist and args.port and args.host:
            user_enum(args.wordlist, args.host, args.user, args.delay)
        else:
            print("Usage: ./finger-user-enum.py -option ip")
            parser.print_help()
    except argparse.ArgumentError:
        parser.print_help()


if __name__ == "__main__":
    main()
