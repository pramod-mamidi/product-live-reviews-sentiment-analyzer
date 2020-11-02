from django.shortcuts import render
from sin_final.forms import ConForm
from pjct.BMS_sentiment_analysis import main_part_pjct,summarize_t
def Organiser(request):
    dict={}
    if request.method == 'POST':
        form = ConForm(request.POST)
        if form.is_valid():
            dict["form"]=form
            lin=form.cleaned_data['link']
            x=main_part_pjct(lin)
            dict["con"]=x[0]
            dict["r_p"]=x[1]
            dict["r_neg"]=x[2]
            dict["r_neu"]=x[3]
            dict["a_p"]=x[4]
            dict["a_neg"]=x[5]
            dict["a_neu"]=x[6]
            dict["t_p"]=x[7]
            dict["t_neg"]=x[8]
            dict["t_neu"]=x[9]
            print(lin)
        return render(request,'ht.html',{"dict":dict})
    else:
        form=ConForm()
        dict["form"]=form
        return render(request,'ht.html',{"dict":dict})
def Summary(request):
    l=summarize_t()
    dict1={}
    dict1['f']=l[0]
    dict1['s']=l[1]
    dict1['t']=l[2]
    dict1['fo']=l[3]
    dict1['fi']=l[4]
    return render(request,'ht1.html',{"dict1":dict1})
