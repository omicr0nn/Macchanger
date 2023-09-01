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
	    
system("cls||clear")
os.system("figlet MAC Degistirme")
print("""
MAC Adres Değiştirme Programına Hoş Geldiniz / omicr0n 

1) MAC Adresi Random Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orijinale Döndür
""")

islemno = input("İşlem No Girin: ")

if(islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Random Belirlendi.")


elif(islemno=="2"):
	macadres = input("Yeni MAC Adres Girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Elle Belirlendi.")

elif(islemno=="3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adresi Orijinale Döndürüldü.")

else:
	print("Hata! Kali linux kullansana kardeşim")
