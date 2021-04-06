from flask import Flask,flash, redirect, url_for, request,render_template
from flask import session
import MySQLdb
app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/')
def success():
   return render_template('landing.html')

@app.route('/home')
def home():
   return render_template('index.html') 

@app.route('/login',methods = ['POST', 'GET'])
def login():
   msg = ''
   if request.method == 'POST':
      user = request.form['username']
      password = request.form['password']
      conn = MySQLdb.connect( host="localhost",
                            user="root",
                            passwd="Srujana@0705",
                            db="geekfolks",
                            port=3306)
      curs = conn.cursor()
      nrows=curs.execute("select * from users where username = %s and password = %s" ,(user,password,))
      
      if nrows == 1:
         msg = 'You have logged in successfully !'
         return render_template('chooseui.html', msg = msg) 
      else: 
         msg = 'Incorrect username / password !'
         return render_template('index.html',msg =  msg) 

@app.route('/register',methods = ['POST','GET'])
def register():
   msg = ''
   if request.method == 'POST':
      user = request.form['username']
      email_id = request.form['email_id']
      password = request.form['password']
      conn = MySQLdb.connect( host="localhost",
                            user="root",
                            passwd="Srujana@0705",
                            db="geekfolks",
                            port=3306)
      curs = conn.cursor()
      try:
         curs.execute("INSERT INTO users(username, emailid, password) VALUES (%s, %s, %s)", (user, email_id, password))
         print("Hello")
         # input()
         conn.commit()
         curs.close()
         return render_template('chooseui.html',user=user,email = email_id)
      except Exception as e:
         msg = "This username already exists"
         #return render_template('r_sign_up.html',msg =  msg, id = id)
         return render_template('sign_up.html',msg = msg)

@app.route('/Nutrition_Landing',methods = ['POST','GET'])
def land_func():
   return render_template('nutrition_landing.html') 

@app.route('/options',methods = ['POST','GET'])
def option_func():
   return render_template('boxes.html')    


@app.route('/Mental_Landing',methods = ['POST','GET'])
def mental_func():
   return render_template('mental_landing.html')   

@app.route('/workout_landing',methods = ['POST','GET'])
def workout_func():
   return render_template('workout_landing.html')      

@app.route('/Articles',methods = ['POST','GET'])
def articles():
   return render_template('Articles.html') 

@app.route('/mindfulness',methods = ['POST','GET'])
def mindfulness():
   return render_template('mindfullness.html')    

@app.route('/meditation',methods = ['POST','GET'])
def meditation():
   return render_template('meditation.html') 


@app.route('/sleep',methods = ['POST','GET'])
def sleep():
   return render_template('sleep.html')    

@app.route('/exercise',methods = ['POST','GET'])
def exercise():
   return render_template('exercise.html')    

@app.route('/todo',methods = ['POST','GET'])
def todo():
   return render_template('to-do.html')      


@app.route('/stress_relief',methods = ['POST','GET'])
def stress():
   return render_template('stress.html') 

@app.route('/BMI',methods = ['POST','GET'])
def bmi_func():
   return render_template('calculator.html')    

@app.route('/health_chat',methods = ['POST','GET'])
def health_chat():
   return render_template('health_chat.html') 

@app.route('/nutrition_chat',methods = ['POST','GET'])
def nutrition_chat():
   return render_template('nutrition_chat.html') 



# @app.route('/Mental Health',methods = ['POST','GET'])
# def mental_func():
#    return render_template('mental_health.html')   

@app.route('/diet_plan',methods = ['POST','GET'])
def diet():
   if request.method == 'POST':
      val1 = int(request.form['height'])
      val2 = int(request.form['weight'])
      result = round(val2/(val1/100*val1/100),2)
      if result<18.5:
         return render_template('underweight .html',result = result)
      elif result>=18.5 and result<25:
          return render_template('normalweight.html',result = result)
      elif result>=25 and result<30:
         return render_template('overweight.html',result = result)  
      else:
         return render_template('obesity.html',result = result)

if __name__ == '__main__':
   app.run(debug = True)