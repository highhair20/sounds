#!/usr/bin/python

from flask import Flask, jsonify, make_response, request     
from sys import argv
import urllib2
from gtts import gTTS
import os 

app = Flask(__name__)  

@app.route('/say', methods=['GET'])
def get_stations():
    re={'status': 'success'}

    tag = 'with an unkown tag'
    if (request.args.get('tag')):
        tag = 'Version ' + request.args.get('tag')
    product = 'An unknown product'
    if (request.args.get('product')):
        product = request.args.get('product')

    message = product + tag + ' has been released'
    # example message 'M2M Server Version 1.18.55 has been released.'
    tts = gTTS(text=message, lang='en')
    tts.save('sound.mp3')
    os.system('mplayer -ao alsa:device=hw=0,0 -really-quiet -speed 1.25 -af scaletempo -noconsolecontrols sound.mp3')    

    return jsonify(re)
    

# start the web server    
if __name__== '__main__':                                                      
    app.run(host='0.0.0.0',port=9000)
    



