from flask import Flask,request,render_template
import parking
from collections import OrderedDict

import logging
import os
import json
import time
from flask import jsonify

import unicodedata
app = Flask(__name__)

global slot_list
global dict_main

dict_main=OrderedDict()
slot_list=list()






def printdict(dict):
    try:
        os.remove('./datalog.txt')
    except:
        print("no file")
    with open('./datalog.txt', 'w') as f:
        f.write(json.dumps(dict,sort_keys=True))
        # unicodedata.normalize('NFKD', f).encode('ascii', 'ignore')
    f.close()
    print("Done writing to log file")


@app.route('/back')
def maini():
    return render_template('index.html')

@app.route('/')
def main():
    global dict_main

    try:
        alsod=OrderedDict()
        file = json.load(open('./datalog.txt', 'r'))

        for key in file.keys():
            x=file[key][0]
            y=file[key][1]
            alsod[int(key)]=[str(x),str(y)]

        li=(sorted(alsod.keys()))

        for key in li:

            dict_main[key]=alsod[key]

    except:
        print("No file")
    return render_template('index.html')


@app.route('/result.html',methods = ['POST', 'GET'])
def result():
    global slot_list
    global dict_main

    if request.method == 'POST':
        try:
            select = request.form.get('option')
            data = request.form['input']
            unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')

        except:
            print("error")
        # if select=='--choose--':
        #     return render_template('index.html')
        if select=='Create Lot':
            slot_list=parking.initalize(slot_list,int(data))
            temp_dict=dict()
            for k in range(0,len(slot_list)):
                temp_list=[slot_list[k],' ']
                temp_dict[k]=temp_list
            dict_main=temp_dict
            print(dict_main)
            printdict(dict_main)
            return render_template('createdlot.html', result = temp_dict)
        if select=='Add Car':
            text = data.split(" ")
            try:
                send_data=text[0]+" "+text[1]+" "+text[2]+" "+text[3]
                ans = dict()
                ans = dict_main
                ans = parking.entry(slot_list, str(send_data), str(text[-1]), dict_main)
                printdict(dict_main)
                if ans == 'Parking Full':
                    return render_template('result.html', result=ans)
                else:
                    return render_template('createdlot.html', result=dict_main)
            except:
                return render_template('result.html', result=' input syntax error')

        if select=='Leave Car':
            text = data.split(" ")
            try:
                send_data = text[0] + " " + text[1] + " " + text[2] + " " + text[3]
                parking.leave(slot_list, str(send_data), dict_main)
                printdict(dict_main)
                return render_template('createdlot.html', result=dict_main)
            except:
                return render_template('result.html', result=' input syntax error')

        if select=='Show Cars of same color':
            try:
                ans=parking.get_cars_with_color(data,dict_main)
                printdict(dict_main)
                return render_template('createdlot.html', result=ans)
            except:
                return render_template('result.html', result=' input syntax error')
        if select=='Show slot number of Car':
            text = data.split(" ")
            try:
                send_data = text[0] + " " + text[1] + " " + text[2] + " " + text[3]
                ans1=parking.get_slot_with_number(send_data,dict_main)
                printdict(dict_main)
                return render_template('createdlot.html', result=ans1)
            except:
                return render_template('result.html', result=' input syntax error')
        if select=='Show all Cars':

            print(dict_main)
            return render_template('createdlot.html', result=dict_main)
















if __name__ == '__main__':

    app.run()
