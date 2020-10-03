import numpy as np
import os
import pyttsx3
import calendar

software_dict = {('Paint', 'paint', 'PAINT'):'mspaint',
                 ('notepad', 'Notepad', 'NOTEPAD'):'notepad',
                 ('word', 'msword', 'Msword', 'Word', 'WORD'):'WINWORD',
                 ('PPT', 'Ppt', 'ppt', 'powerpoint', 'Powerpoint', 'POWERPOINT'):'POWERPNT',
                 ('VLC','vlc', 'vlc player', 'vlcplayer', 'VLC player'):'vlc',
                 ('win player', 'win media player', 'windows media player', 'Windows Media Player', 'WINDOWS MEDIA PLAYER', 'WIN PLAYER', 'wmplayer'):'wmplayer',
                 ('excel', 'sheet', 'msexcel', 'spreadsheet', 'EXCEL', 'SHEET', 'SPREADSHEET', 'MSECEL', 'Excel', 'Sheet', 'Spreadsheet', 'Msexcel'):'EXCEL',
                 ('edge', 'Edge', 'EDGE', 'browser', 'Browser', 'BROWSER'):'msedge',
                 ('calc','calcuator', 'CALC', 'CALCULATOR', 'Calc', 'Calculator'):'calc'}

run_key = ['run', 'Run', 'RUN', 'open', 'Open', 'OPEN', 'execute', 'Execute', 'EXECUTE']
st1 = ('Hello. What do you want to run?')
pyttsx3.speak(st1)
print(st1)
print('1.Paint')
print('2.Notepad')
print('3.Microsoft Word')
print('4.Microsoft PowerPoint')
print('5.VLC Player')
print('6.Windows Media Player')
print('7.Microsoft Excel')
print('8.Edge Browser')
print('9.Calculator')
print('10.Calender')

user_input = input()
sd = ['shut','Shut','SHUT','down','Down','DOWN','turn','Turn','TURN','Off','off','OFF']
res = ['RESTART', 'Restart', 'restart']
diff_key = 'Try a different keyword.'
#print(user_input)

software_keyword = []
for s in software_dict:
    software_keyword.append(s)
#print(software_keyword)

prog = []
for s in software_dict:
    prog.append(software_dict[s])
#print(prog)
sep_keywords = []

for i in range(len(software_keyword)):
    for keyword in software_keyword[i]:
        if keyword in user_input:
            prog_id = software_keyword.index(software_keyword[i])
            prog_ele = prog[prog_id]
            pyttsx3.speak(f'launching {keyword}')
            os.system(prog_ele)
        break

    if ('calender' or 'Calender' or 'CALENDER') in user_input:
        print('Enter the year for which you want to see the calender.')
        pyttsx3.speak('Enter the year for which you want to see the calender.')
        year = int(input())
        print(calendar.calendar(year))
    
    for i in range(len(sd)):
        if sd[i] in user_input:
            pyttsx3.speak('Shutting down')
            print('shutdown')
            #os.system('shutdown /s /t 1')
        break

    for i in range(len(res)):
        if res[i] in user_input:
            pyttsx3.speak('Restarting')
            print('r')
            #os.system('shutdown /r /t 1')
        break

    break