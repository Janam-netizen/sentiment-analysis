
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


from flask import Flask,render_template,request
from flask import Flask
from textblob import TextBlob
from  matplotlib import pyplot as plt
app = Flask(__name__)




#def get_data():
    # currenty uses harcoded data, but will use real data when access is acquired 
  
    
@app.route('/')
def start():
    return render_template("user-form.html")
@app.route('/get_score',methods=["post","get"])
def get_score():

    text=request.args.get("text")
    print(text)
    score=TextBlob(text).sentiment.polarity
    return str(score)
'

app.run(debug=True)


