import random
import sys
import webbrowser
import zipfile
import os
import subprocess
import time

#List links
dlist1 = 'https://docs.google.com/document/d/1NjxjMzkAmOZKGObvknOH4HIQO4-CCwn8-IVabGl_woY/edit'
dlist2 = ''
dlist3 = ''
dlist4 = ''
dlist5 = ''
dlist6 = ''
dlist7 = ''
dlist8 = ''
dlist9 = ''
nlist1 = 'https://docs.google.com/document/d/1ToJJCWXyZ3bBQhvzu202QYFzLu5zWNHlxHf7nxiScWQ/edit'
nlist2 = 'https://docs.google.com/document/d/1DZ5Q-D2nwpJ4GDWjLEehUJVggpDa_Tfr8zn2KtRKKnI/edit'

#List definitions
rhlist = [dlist1, nlist1, nlist2]
newrhlist = []

#Open two random RHEL lists
for i in range(3):
 r = random.choice(rhlist)
 if r not in newrhlist:
  newrhlist.append(r)
webbrowser.open_new(newrhlist[0])
webbrowser.open_new(newrhlist[1])

time.sleep(5)

#Figure out if timer exists, if no, install timer
exists = os.path.isfile('C:\Users\Nick\Desktop\RHCSAHelp\LiveSplit_1.7.6\LiveSplit.exe')

if exists:
 subprocess.call('C:\Users\Nick\Desktop\RHCSAHelp\LiveSplit_1.7.6\LiveSplit.exe')
else:
 print 'poop'
 #need these things https://gitpython.readthedocs.io/en/stable/intro.html

time.sleep(5)

#Timer setup

time.sleep(5)

#unzip start
archive = zipfile.ZipFile('C:\Users\Nick\Desktop\RHCSAHelp\dpkg.zip', 'r')

archive.extractall('C:\Users\Nick\Desktop\RHCSAHelp')

archive.close()


#open vm start
numlist = ['poop', 'skkrt', 'champ', 'poopers']
newlist = []
vmlist = ['poop', 'skkrt']

for i in range(3):
 r = random.choice(numlist)
 if r not in newlist:
  newlist.append(r)

print newlist[0]
print newlist[1]

if newlist[0] == 'poop':
    print 'Open poop vm!'
elif newlist[0] == 'skkrt':
    print 'Open skkrt vm!'
else:
    print 'Open ova'
if newlist[1] == 'poop':
    print 'Open poop vm!'
elif newlist[1] == 'skkrt':
    print 'Open skkrt vm!'
else:
    print 'Open ova'

time.sleep(5)
