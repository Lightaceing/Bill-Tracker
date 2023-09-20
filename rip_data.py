#read all files from a dir and write the info to a csv file
import os
import csv

dir = "D:\\Bill payment\\Electricity Bill"
names_list = os.listdir(dir)
new_csv = dir + "\\compre.csv"
ff = []

for name in names_list:
    x = ''
    g = name.rsplit('.pdf')[0].rsplit('-')[1:5]
    for each in g:
        x += g
    ff.append(g)

f = open(new_csv, 'w')
writer = csv.writer(f)
writer.writerow(ff)
f.close()

print(ff)