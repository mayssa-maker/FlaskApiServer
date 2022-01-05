import pandas as pd
from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_mail import Mail ,Message
from datetime import date, datetime, timedelta


sheet_id='16G7cgOCFTpdXNbIDapPeIt6ApjlOcguFMwsosA0UzGQ'
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
#print(df)
records=df.to_dict(orient='records')
#print(records[0])


#Instanciate new flask application object
app = Flask(__name__)
#initialize api object for the flask application
api =Api(app)

#Flask Mail config 
app.config['DEBUG']= True
app.config['MAIL_SERVER' ]='smtp.gmail.com'
app.config['Testing']=False
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL']= False
#app.config['MAIL_DEBUG']= True
app.config['MAIL_USERNAME'] = 'mattelimayssa@gmail.com'
app.config['MAIL_PASSWORD'] = 'mayssaing3@'
app.config['MAIL_DEFAULT_SENDER'] = 'mattelimayssa@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND']=False
app.config['MAIL_ASCII_ATTACHMENTS']=False

mail = Mail(app)


#routes
@app.route('/')
def index():
    """
   ** this byte of code was for testing the mail sending and it was successful**
    msg = Message('Hey There', recipients=['mayssa.mettali@sesame.com.tn'])
    mail.send(msg)"""
    return render_template('index.html')
 
#api requests
"""class All(Resource):
    def get(self):
        return records
"""
class Tasks(Resource):
    def get(self):
        
    
     #1
      for n in records :

          if (n['status']=='Applied'):

              msg = Message('Thank u for applying', recipients=[n['email']])
              mail.send(msg)
              n['status']='Online Test sent'
              n['mail_sent'] = date.today()
     #2
       
          elif ((n['status']=='Online Test Sent') and (n['mail_sent'] == ((datetime.now() - timedelta(days=7)).date())) and (n['Test_score']==' ')):

              msg = Message('you haven''t submitted your test.Every thing is okay ?', recipients=[n['email']])
              mail.send(msg)
              n['status']='Reminder Sent'
              n['mail_sent'] = date.today()
#3
     
          elif ((n['status']=='Submitted Test') and n['Test_score']<=0.5):
              
              msg = Message('We are sorry to tell you that you did not pass the test', recipients=[n['email']])
              mail.send(msg)
              n['status']='Refusal Mail Sent'
              n['mail_sent'] = date.today()
#4 
      
          elif ((n['status']=='Submitted Test')  and n['Test_score']>=0.5):
              
              msg = Message('Congratulations for passing the test. You’ll have an interview with _____', recipients=[n['email']])
              mail.send(msg)
              n['status']='Interview Mail Sent'
              n['mail_sent'] = date.today()
              return  records 
#register api resources
api.add_resource(Tasks,'/api/')

#api.add_resource(Email,'/api/email/<string:value>')

if __name__=="__main__":
    app.run(debug=True,port=9000)


