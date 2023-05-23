import pickle
import warnings
warnings.filterwarnings("ignore")
import datetime
Predictor=pickle.load(open("Model.pkl","rb"))
Location=pickle.load(open("Location_encoder.pkl","rb"))
def mal_function(dc,dp,dt,cl,d,m,y):
    cl=Location.transform([cl])[0]
    days=Predictor.predict([[dc,dp,dt,cl]])[0]
    Failure_date=datetime.datetime(y,m,d)+datetime.timedelta(days=days)
    Service_date=datetime.datetime(y,m,d)+datetime.timedelta(days=days-30)
    return Failure_date,Service_date