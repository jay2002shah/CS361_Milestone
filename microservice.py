import time
import json
import codecs
#import request

from json2html import *

while True:
        time.sleep(3)

        f = open('books.txt', 'r')
        line = f.readline()
        f.close()

        if line == 'request':

                time.sleep(5)
                with open ('request.json') as f:
                        d = json.load(f)
                        scanOutput = json2html.convert(json=d)
                        htmlReportFile = "results.html"



                with open(htmlReportFile, 'w') as htmlFile:
                        htmlFile.write(str(scanOutput))
                print("Json file is converted into html successfully")
                exit()
