from django.shortcuts import render
from joblib import load
#model=load('../savedModels/model.joblib')
path="C:/Users/user/Desktop/LoanPrediction/savedModels/model.joblib"
model=load(path)

# Create your views here.
def predictor(request):
    if request.method=='POST':
        graduate=request.POST['graduate']
        employed=request.POST['employed']
        income=request.POST['income']
        loan=request.POST['loan']
        term=request.POST['term']
        cibil=request.POST['cibil']
        asset=request.POST['asset']
        y_pred=model.predict([[graduate,employed,income,loan,term,cibil,asset]])
        if y_pred[0]==0:
            y_pred='Accepted'
        else:
            y_pred='Rejected'
        print(y_pred)

        return render(request,'main.html',{'result':y_pred})

    return render(request,'main.html')

