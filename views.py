from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
	return render(request,"home.html")

def result(request):
	cls=joblib.load('finalized_model.sav')

	lis=[]
	lis.append(request.POST.get('TAU1',False))
	lis.append(request.POST.get('TAU2',False))
	lis.append(request.POST.get('TAU3',False))
	lis.append(request.POST.get('TAU4',False))
	lis.append(request.POST.get('P1',False))
	lis.append(request.POST.get('P2',False))
	lis.append(request.POST.get('P3',False))
	lis.append(request.POST.get('P4',False))
	lis.append(request.POST.get('G1',False))
	lis.append(request.POST.get('G2',False))
	lis.append(request.POST.get('G3',False))
	lis.append(request.POST.get('G4',False))
	# lis.append(request.GET('STAB',False))

	ans=cls.predict([lis])



	return render(request,"result.html",{'ans':ans})
