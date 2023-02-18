from django.urls import path
from stack import views

urlpatterns=[
    path("register/",views.Signupview.as_view(),name="register"),
    path("login",views.Signinview.as_view(),name="signin"),
    path("home",views.Indexview.as_view(),name="index"),
    path("questions/<int:id>/ansewrs/add",views.AddAnswerView.as_view(),name="add-answer"),
    path("answers/<int:id>/upvote/add",views.UpvoteView.as_view(),name="upvote")

]