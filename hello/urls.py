from django.urls import path
from .views import hello_world, GreetingView, HelloView, GoodbyeView

urlpatterns = [
	path('', hello_world),										 # 関数「hello_world」を実行
    path('greet/', GreetingView.as_view(), name='greet-home'),	 #「 GreetingView」を関数化して実行
	path('hello/', HelloView.as_view(), name='hello-home'),		 #「 HelloView」 　を関数化して実行
	path('goodbye/', GoodbyeView.as_view(), name='goodby-home'), #「 GoodbyeView」 を関数化して実行
]


