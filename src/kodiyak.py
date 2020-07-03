#######################################
#      KodiYak Python Etiquette       #
#      Developed by Colby Pryor       #
#######################################

#Imports and other modules
import time
import os 
#Find file & convert into text file
path = input("Enter path to .py file for review:") #Gather path
filename = input("Enter filename:") #Gather path
print("Converting into .txt file for review...")
os.rename(path, filename+'.txt') #Conversion to .txt file
newfilename = input("Conversion complete, enter new path name to begin review:")

def review_for_comments():
    file = open(newfilename, 'r')
    count = 0
    for line in file:
        line = line.strip()
        if(len(line) > 0):
            if(len(line) > 20):
                print("{}".format(line))
review_for_comments()      
#add more validation below

