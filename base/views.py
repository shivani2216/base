from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return HttpResponse('This is page')

def about(request):
	str1="""
			This tutorial will not magically turn you into 
			a programmer. If you want to be good at it,
			you need months or even years of learning
			and practice. But we want to show you that 
			programming or creating websites is not as complicated
			as it seems. We will try to explain different bits and
			pieces as well as we can,so you will not feel intimidated
			by technology.
		"""
	wordlist = str1.split(' ')
	worddict = {}
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
		return render(request,'list.html')


# Create your views here.
