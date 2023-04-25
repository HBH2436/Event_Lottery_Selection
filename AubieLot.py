import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

#input Contestants
contest = pd.read_excel(r'C:\Users\Henry\OneDrive\Desktop\Work\AubieLottery\AubieLottery\Up.xlsx')
contestants=contest.to_numpy()
contestant=[]

#input timeslots, timeslot size, and number of timeslots
print('Please enter the number of winners per timeslot.')
#num_winners = int(input())
num_winners = 20

print('Please enter the timeslots in the form **/**/****|*-*PM')
#timeslot_picks_string = str(input())
timeslot_picks_string='11/10/2022|4-8PM,11/11/2022|8-6PM,11/13/2022|8-6PM,11/17/2022|4-8PM,11/11/2022|2-8PM,11/20/2022|8-6PM'
timeslot_a = timeslot_picks_string.split(',')
num_timeslots = len(timeslot_a)
for x in timeslot_a:
    timeslot_winners = []
    while len(timeslot_winners) != num_winners:
        #select random contestant
        rand_int = random.randint(0,len(contestants))
        contestant = contestants[rand_int-1]
        timeslot_picks_string = contestant[9]
        timeslot_picks = timeslot_picks_string.split('.,')
        timeslot_winners.append(contestant)
    df = pd.DataFrame(timeslot_winners).T
    df.to_excel(excel_writer = "C:/Users/Henry/OneDrive/Desktop/Work/AubieLottery/AubieLottery/Out.xlsx")
