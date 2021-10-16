from flask import Flask,render_template,request
import Fakenews as fk
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    cleandata = request.form['news'].rstrip()
    # print(cleandata)
    res = fk.prednews(cleandata)
    return render_template('page.html',result=res)

app.run(debug=True)