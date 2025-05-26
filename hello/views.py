from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView	#クラスベースビューで使用する「HTML表示用の汎用ビュー」



# 関数ベースビュー（単純なテキストやバイナリデータを返す場合）-----------------------
def hello_world(request):				    	# 関数「hello_world」
	return HttpResponse("Hello, World!")    	# HttpResponseオブジェクトの生成



# 関数ベースビュー（htmlファイル を使用する場合）----------------------------------
def hello_world(request):						# 関数「hello_world」
	return render(request, 'hello.html', {'message': 'Hello World'}) #「hello.html」を表示テンプレートとして使用



# クラスベースビュー（汎用的な例）------------------------------------------------
class GreetingView(TemplateView):		    	# クラス「GreetingView」
	template_name = 'greeting.html'		        # テンプレートファイルの指定（※ TemplateViewの機能）
	message = 'ご挨拶申し上げます'

	def get_context_data(self, **kwargs):   	# htmlテンプレートへ動的にデータを渡す場合に記述
		context = super().get_context_data(**kwargs)  # 親クラスから基本的なコンテキストを取得
		context['message'] = self.message   	#「message」をコンテキストに追加　（※html側では {{ message }}で呼び出し）
		return context

class HelloView(GreetingView):		           	# クラス「GreetingView」を継承
	message = 'こんにちは！'		        	 # コンテキスト内「message」の値を変更

class GoodbyeView(GreetingView):		    	# クラス「GreetingView」を継承
	message = 'さようなら！'                     # コンテキスト内「message」の値を変更


