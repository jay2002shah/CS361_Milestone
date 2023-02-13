import time
import json
import codecs

while True:

        f = open('getjson.txt', 'r')
        input = f.readline()
        f.close()


        if input == 'recieved':
                w = open('getjson.txt', 'w')
                w.write('Request recieved')
                w.close()
                
