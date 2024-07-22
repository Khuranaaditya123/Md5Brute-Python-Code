#!/usr/bin/python
import hashlib
from termcolor import colored

def tryOpen(wordList):
        global pass_file
        try:
                pass_file = open(wordlist,"r")
        except:
                print("[!!]No such file at that path")
                quit()

pass_hash = input("[*] Enter value of md5 hash : ")
wordlist = input("[*] Enter path to the password file : ")
tryOpen(wordlist)

for word in pass_file:
        print(colored("[-]Trying : "+ word.strip("\n"),'red'))
        enc_word = word.encode('utf-8')
        md5digest = hashlib.md5(enc_word.strip()).hexdigest()

        if md5digest == pass_hash:
                print(colored("[+]Password matched :"+ word,'green'))

print("Password not in the list!!!!")
