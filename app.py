from flask import Flask, render_template

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('chart.html')

if __name__=="__main__":
    app.debug=True
    app.run()