
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
'''class Tweet():
    
    def __init__(self,post,timestamp):
        self.post=post
        self.timestamp=timestamp
        self.score=TextBlob(post).sentiment.polarity'''



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
'''@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    twitter_data = get_data()
    xs = twitter_data["timestamps"]
    ys = twitter_data["scores"]
    axis.plot(xs, ys)
    return fig'''

app.run(debug=True)

'''@app.route('/')
def hello_world():
    return render_template("user-form.html")
@app.route('/graph')
def get_graph():
    handle=request.args.get("handle")
    print(handle)
    return render_template('graph.html',geocode=[1,5,6,7,8])
(debug=True)'''
