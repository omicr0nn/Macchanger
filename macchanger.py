#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding by omicr0n
import os
import sys
import time
from os import system

system("cls||clear")
def rainbow_text(text, delay=0.1):
    colors = [
    "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m",
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")
	
if __name__ == "__main__":
    rainbow_text("Coding by Omicron")
	    
print("""
\033[35mMAC Adres Değiştirme Programına Hoş Geldiniz / omicr0n \033[0m

\033[32m 1) MAC Adresi Random Belirle\033[0m
\033[31m 2) MAC Adresi Elle Belirle\033[0m
\033[94m 3) MAC Adresi Orijinale Döndür\033[0m
""")

islemno = input("İşlem No Girin: ")

if(islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[32m Yeni MAC Adresi Random Belirlendi. \033[0m")


elif(islemno=="2"):
	macadres = input("\033[31m Yeni MAC Adres Girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[31m Yeni MAC Adresi Elle Belirlendi. \033[0m")

elif(islemno=="3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[94m MAC Adresi Orijinale Döndürüldü. \033[0m")

else:
	print("Hata! Kali linux kullansana kardeşim")
