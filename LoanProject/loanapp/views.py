from django.shortcuts import render
from joblib import load
#model=load('../savedModels/model.joblib')
path="C:/Users/user/Desktop/LoanPrediction/savedModels/model.joblib"
model=load(path)
path_scalar=r"C:\Users\user\Desktop\LoanPrediction\savedModels\standardScalar.joblib"
scalar=load(path_scalar)

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
        transformed_asset=scalar.fit_transform([[asset]]).reshape(-1)
        inputs = [
            graduate,
            employed,
            income,
            loan,
            term,
            cibil,
            transformed_asset[0]
        ]


        y_pred=model.predict([inputs])
        if y_pred[0]==0:
            y_pred='Accepted'
        else:
            y_pred='Rejected'
        print(y_pred)

        return render(request,'main.html',{'result':y_pred})

    return render(request,'main.html')

