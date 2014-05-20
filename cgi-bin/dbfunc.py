from flask import Flask
from flask import request
from flask import render_template
import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wowdb import User
from wowdb import Guild
from wowdb import Item

app = Flask(__name__)

engine = create_engine('sqlite:///wow.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guilds.html')
def guilds():
    return render_template('guilds.html')

@app.route('/items.html')
def items():
    return render_template('items.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/guilds/get', methods=["POST"])
def getGuilds():
    
    trackedList = ""
    for guild, server in session.query(Guild.guild, Guild.server):
       trackedList = trackedList + ":" + guild + "," + server
    return str(trackedList)

@app.route('/guilds/delete', methods=["POST"])
def delGuilds():
    #engine = create_engine('sqlite:///wow.db', echo=True)
    #Session = sessionmaker(bind=engine)
    #session = Session()
    deletedGuild = Guild(request.json['user_name'],
                          request.json['guild'],
                          request.json['server'])
    try: 
        session.delete(deletedGuild) 
    except: 
        session.query(Guild.guild, Guild.server).filter(Guild.guild==request.json['guild']).delete()
        #session.expunge(deletedGuild)
    return str(request.json['guild'])

@app.route('/index/guild', methods=["POST"])
def trackGuild():
    if request.method == "POST":
        #engine = create_engine('sqlite:///wow.db', echo=True)

        # Create a Session
        #Session = sessionmaker(bind=engine)
        #session = Session()

        trackedGuild = Guild(request.json['user_name'],
                              request.json['guild'],
                              request.json['server'])

        # Add the record to the session object
        session.add(trackedGuild)
        session.commit()
        # commit the record the database
        #return str(request.json)
    return str(request.json['guild'])

app.debug = True
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
