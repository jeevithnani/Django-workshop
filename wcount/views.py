from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'wcount/home.html')
def about(request):
    return render(request,'wcount/about.html')
def count(request):
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    word_count_list=[(w,word_dict[w]) for w in list(word_dict.keys())]
    return render(request,'wcount/count.html',{'fulltext':fulltext,'word_count':word_count,'word_dict':word_dict,'word_count_list':word_count_list})
