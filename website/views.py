from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from .models import User
from . import db
import json
import sqlite3
from sqlalchemy.sql import func
import datetime

views = Blueprint('views', __name__)
conn = sqlite3.Connection('instance/database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()


aaa = -1

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)




@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        note = request.form.get('note')
        admin2= request.form.get('admin2')
        department2= request.form.get('department2')
        unit2= request.form.get('unit2')
        date2= request.form.get('date')
        print(date2)
        


        if len(note) < 1:
            flash('! امر العمل قصير جدا ', category='error')
        elif len(admin2) < 1:
            flash('اختر وجهة امر العمل .', category='error')
        elif (len(department2) < 1 ):
            flash('.ادخل الشعبة المنفذة', category='error')
        elif (len(unit2) < 1 and admin2=="وحدة"):
            flash('.ادخل الوحدة المنفذة', category='error')
        elif (current_user.department == department2 and admin2=="شعبة" ):
            flash('.لا يمكن ارسال امر عمل الى نفس شعبة المستخدم', category='error')
        elif (current_user.unit == unit2 and admin2=="وحدة"):
            flash('.لا يمكن ارسال امر عمل الى نفس وحدة المستخدم', category='error')
            
        else:
            new_note = Note(data=note, user_id=current_user.id, admin2=admin2, department2=department2, unit2=unit2, date2=date2)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("create.html", user=current_user)

@views.route('/check', methods=['GET', 'POST'])
@login_required
def check():
    conn = sqlite3.Connection('instance/database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = ("""SELECT * from Note  """)
    cur.execute(sql)
    results = cur.fetchall()
    conn2 = sqlite3.Connection('instance/database.db')
    conn2.row_factory = sqlite3.Row
    cur2 = conn2.cursor()
    sql2 = ("""SELECT * from User  """)
    cur2.execute(sql2)
    results2 = cur2.fetchall()
    return render_template("check.html", user=current_user, results=results, results2=results2)


@views.route('/check2', methods=['GET', 'POST'])
@login_required
def check2():
    conn = sqlite3.Connection('instance/database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = ("""SELECT * from Note  """)
    cur.execute(sql)
    results = cur.fetchall()
    conn2 = sqlite3.Connection('instance/database.db')
    conn2.row_factory = sqlite3.Row
    cur2 = conn2.cursor()
    sql2 = ("""SELECT * from User  """)
    cur2.execute(sql2)
    results2 = cur2.fetchall()
    return render_template("check2.html", user=current_user, results=results, results2=results2)




@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    print(noteId)
    return jsonify({})





@views.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    conn = sqlite3.Connection('instance/database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    
    sql = ("""SELECT * from Note WHERE id == {};""").format(aaa)
    cur.execute(sql)
    results = cur.fetchone()
    
    sql2 = ("""SELECT * from User """)
    cur3.execute(sql2)
    results2 = cur3.fetchall()



  
   
    #if request.form.get('sign1') != "":
    if request.method == 'POST':
      
        note22 = request.form.get('note')
        note33 = request.form.get('note2')
        state22 = state33 = ""
        state11 = request.form.get('state1')
        state22 = request.form.get('state2')
        state33 = request.form.get('state3')
        print(state22)
        print(state33)
        date5= request.form.get('date5')
        username = current_user.first_name
        username2 = current_user.first_name
        username3 = current_user.first_name
        time = datetime.datetime.now()
        time2 = datetime.datetime.now()
        if current_user.admin == "مدير قسم" :
         cur2.execute("""UPDATE Note SET data2 = :data2 , state1 = :state1, sign1 = :sign1 ,  date3 = :date3  WHERE id == :id;""",{'data2':note22 ,'state1' :state11 ,'sign1':username , 'date3':time  ,'id':aaa })
         conn.commit()
         db.session.commit()
        if current_user.admin ==  "مسؤول وجبة":
            
        
          if state22 :
           cur2.execute("""UPDATE Note SET data3 = :data3 , state2 = :state2 , sign2 = :sign2, date4 = :date4  WHERE id == :id;""",{'data3':note33 ,'state2' :state22 ,'sign2':username2 ,'date4':time2 ,'id':aaa })
           conn.commit()
           db.session.commit()
           print("one")
           
          if state33 :
           cur2.execute("""UPDATE Note SET state3 = :state3 , sign3 = :sign3 , date5 = :date5 WHERE id == :id;""",{'state3' :state33 , 'sign3':username3, 'date5':date5 ,'id':aaa })
           conn.commit()
           db.session.commit()
           print("two")
        return redirect(url_for('views.update'))
    return  render_template("update.html",aaa=aaa, user=current_user, results=results,results2=results2)
    
    



@views.route('/update2', methods=['GET', 'POST'])
@login_required
def update2():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    request.method = "GET"
    global aaa 
    aaa = noteId
    return  jsonify({})
