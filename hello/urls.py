from django.urls import path
from .views import hello_world, GreetingView, HelloView, GoodbyeView

urlpatterns = [
	path('', hello_world),				    	# 関数「hello_world」を実行
    path('greet/', GreetingView.as_view()),		#「 GreetingView」を関数化して実行
	path('hello/', HelloView.as_view()),		#「 HelloView」 　を関数化して実行
	path('goodbye/', GoodbyeView.as_view()),	#「 GoodbyeView」 を関数化して実行
]


