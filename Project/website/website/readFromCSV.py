#usage:
#In command line, write: python3 manage.py shell
#type the code below
'''
import csv


from theory.models import Key

with open('keyMap.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        k = Key(name = row['name'], type = row['type'], s_f = row['s_f'], component_pitches = row['pitches'])
        k.save()
'''
