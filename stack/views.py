from django.shortcuts import render,redirect
from stack.forms import Registrationform,LoginForm,QuestionForm
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from stack.models import Questions,Answers
# Create your views here.
class Signupview(CreateView):
    model=User
    form_class=Registrationform
    template_name="register.html"
    success_url=reverse_lazy("signin")


class Signinview(FormView):
    template_name="login.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})

class Indexview(CreateView,ListView):
    model=Questions
    form_class=QuestionForm
    template_name="home.html"
    success_url=reverse_lazy("index")
    context_object_name="questions"

    def form_valid(self, form):
        form.instance.user=self.request.user 
        return super().form_valid(form)

class AddAnswerView(View):
    def post(self,request,*args,**kwargs):
        qid=kwargs.get("id")
        ques=Questions.objects.get(id=qid)
        usr=request.user
        ans=request.POST.get("answer")
        Answers.objects.create(user=usr,questions=ques,answer=ans)
        return redirect("index")

class UpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        ans=Answers.objects.get(id=id)
        ans.upvote.add(request.user)
        ans.save()
        return redirect("index")



