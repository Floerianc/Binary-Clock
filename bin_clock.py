import time
from datetime import datetime
from colorama import Fore
import sys
import os

def display_time():
    time_now = datetime.now()
    sec = time_now.second
    minut = time_now.minute
    hour = time_now.hour
    day = time_now.day
    month = time_now.month
    year = time_now.year
    while True:
        bin_sec = bin(sec)
        bin_minut = bin(minut)
        bin_hour = bin(hour)
        bin_day = bin(day)
        bin_month = bin(month)
        bin_year = bin(year)
        prefix = ["Second", "Minute", "Hour", "Day", "Month", "Year"]
        bins = [bin_sec, bin_minut, bin_hour, bin_day, bin_month, bin_year]
        sec += 1
        if sec == 60:
            os.system("cls")
            sec = 00
            minut += 1
            if minut == 60:
                os.system("cls")
                minut = 00
                hour += 1
                if hour == 24:
                    os.system("cls")
                    hour = 00
                    
        os.system("cls")
        sys.stdout.write(Fore.RED + "\r %s.%s.%s / %s:%s:%s " % (time_now.day, time_now.month, time_now.year, hour, minut, sec))
        print("\n")
        for i in range(len(bins)):
            sys.stdout.write(Fore.YELLOW + f"\n{prefix[i]}: {bins[i]}")
        time.sleep(1)

display_time()