from flask import Flask,render_template,request
# import Fakenews as fk
# from joblib import load
import joblib
app = Flask(__name__)
# model = load('./model.joblib')
model = joblib.load('fakenewsmodel.pkl')
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('page.html')
    else:
        cleandata = request.form['news'].rstrip()
    # print(cleandata)
        # res = fk.prednews(cleandata)
        res = model.predict([cleandata])
        return render_template('page.html',result=res[0].replace('[','').replace(']',''))

if   __name__==  '__main__':
    app.run()