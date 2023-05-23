from flask import Flask,render_template,request
app=Flask(__name__)
from model import mal_function
@app.route('/')
def hello_world():
    return render_template("mal.html")

@app.route('/result',methods=["GET","POST"])
def results_pages():
    if request.method=="POST":
        Dev_Prs=int(request.form["Dev_Prs"])
        Dev_Temp=int(request.form["Dev_Temp"])
        Dev_Cap=int(request.form["Dev_Cap"])
        Day=int(request.form["Day"])
        Month=int(request.form["Month"])
        Year=int(request.form["Year"])
        Location=request.form["Location"]
        dates=mal_function(Dev_Cap,Dev_Prs,Dev_Temp,Location,Day,Month,Year)
        return render_template("results.html",Mal_Function_Date=str(dates[0]),Service_Date=str(dates[1]))

    
app.run(debug=True)    

