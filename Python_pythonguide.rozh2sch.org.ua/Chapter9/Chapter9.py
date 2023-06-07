#import os
#print(os.getcwd())
#os.chdir('C:\\Windows\\Temp')
#print(os.getcwd())

#print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#print(os.listdir('C:\\Windows\\System32'))

#total = 0
#for filename in os.listdir('C:\\Merck'):
#    total = total + os.path.getsize(os.path.join('C:\\Merck', filename))
#    print(filename)
#print(total)

#print(os.path.exists('C:\\Windows'))
#print(os.path.exists('C:\\some_made_up_folder'))
#print(os.path.isdir('C:\\Windows\\System32'))
#print(os.path.isfile('C:\\Windows\\System32'))
#print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
#print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))

#import glob
#os.chdir('c:\\')
#print(glob.glob('o*'))
#print(glob.glob('???'))
#print(glob.glob('c*db'))
#print(glob.glob('[kmr]*'))

#import calendar
#print(calendar.isleap(1900))
#print(calendar.isleap(2000))
#print(calendar.isleap(2019))

#import time
#starttime = time.time()
#for i in range(1000, 0, -1):
#    print(i)
#endtime = time.time()
#print('The program has been running:', str(endtime - starttime), 'seconds.')

import time
row_format = "It's %A, %B %d, %Y, local time %H:%M:%S"
t = time.localtime()
print(t)
print(time.strftime(row_format, t))

#import locale, datetime
#names = locale.locale_alias.keys()
##print(names)
#good_names = [name for name in names if len(name) == 5 and name[2] == '_']
#print(good_names)

import os
#print(os.getcwd())
#for file in os.listdir(os.getcwd()):
#    #print(file)
#    print(os.path.getsize(file))