from django.shortcuts import render

# Create your views her
def calc(requests):
    field1=requests.GET['field1']
    field2=requests.GET['field2']
    operation=requests.GET['optradio']
    result=0
    if operation =='+':
        result=int(field1)+int(field2)
    elif operation =='-':
        result=int(field1)-int(field2)
    elif operation =='*':
        result=int(field1)*int(field2)
    else:
        result=int(field1)/int(field2)
    return render(requests,'calculator/calc.html',{'result':result})
def home(requests):
    return render(requests,'calculator/home.html')