from django.shortcuts import render, redirect, reverse,get_object_or_404 # 追加
from django.http import HttpResponseBadRequest # 追加
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic import View
from .models import Product
from django.core import serializers

class ProductListView(View):
    def get(self,request):
        
        # Productデータを全件取得する。
        # TemplatesではproductListでアクセス可能
        productModel = {'products':Product.objects.all()} 

        return render(request, "register_food/product_list.html", productModel)

#-----新規登録処理を追加(20230801) From-------#
class ProductCreateView(View):
    def get(self, request):
        return render(request, 'register_food/product_form.html', {})
       
    def post(self, request):
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        place = request.POST.get('place')
        payment_date = request.POST.get('payment_date')
        meal_format = request.POST.get('meal_format')
        category = request.POST.get('category')
        degree_regret = request.POST.get('degree_regret')

		# 変数のバリデーション
        if product_name and price and place and payment_date and meal_format and category and degree_regret:

			# データベースへの保存項目
            product = Product(
                product_name=product_name, 
                price=price, 
                place=place, 
                payment_date=payment_date,
                meal_format=meal_format,
                category=category,
                degree_regret=degree_regret,
                )

			# データベースへの保存
            product.save()

			# 登録後トップページに遷移
            return redirect('/register_food/')
        else:
			# バリデーションエラーの場合、バッドリクエストを表示する。
            return HttpResponseBadRequest("All fields are required")

#-----新規登録処理を追加(20230801) To -------#

#-----削除処理を追加(20230805) From -------#
# class ProductDeleteView(View):
#     def post(self, request):
#         selected_product_ids = request.POST.getlist('selected_products')
#         # __in演算子で指定されたリスト内の値に一致するものを取得する。
#         selected_products = Product.objects.filter(id__in=selected_product_ids)
#         if request.POST.get('confirm_delete'):
#             # 商品一覧画面で削除ボタン押下時に、セッションデータを設定する。
#             request.session['selected_products'] = selected_product_ids
#             return redirect(reverse('register_food:delete_confirmation'))

#         return render(request, 'register_food/product_delete.html', {'selected_products': selected_products})

# # 削除確認クラス
# # 削除確認画面から対象データを削除する。
# class DeleteConfirmationView(View):
#     def get(self, request):
#         # 選択された商品データ(プロダクトID)のセッション取得処理
#         selected_product_ids = request.session.get('selected_products')
#         selected_products = Product.objects.filter(id__in=selected_product_ids)
#         return render(request, 'register_food/product_delete.html', {'selected_products': selected_products})
    
#     def post(self, request):
#         # 選択された商品データ(プロダクトID)のセッション取得処理
#         selected_product_ids = request.session.get('selected_products')
#         selected_products = Product.objects.filter(id__in=selected_product_ids)

#         if request.POST.get('confirm_delete'):
#             # チェックされたデータの削除処理
#             selected_products.delete()
#             # セッションデータの削除
#             del request.session['selected_products']
#             # 商品一覧画面にリダイレクト
#             return redirect(reverse('register_food:product_list'))
#         return redirect(reverse('register_food:product_list'))
        
#-----削除処理を追加(20230805) To -------#


#-----削除と更新処理を追加(20230813) From -------#
class ProductUpdateView(View):
    # 更新処理の開始。確認画面を表示するためのビュー。
    # (POSTメソッドでデータが送信されたときの処理を記述)
    def post(self,request):
        #  チェックボックスで選択されたデータを取得
        selected_product_ids = request.POST.getlist('selected_products')
        # アクションタイプの取得
        action_type = request.POST.get('action_type')
        # チェックされたデータでフィルタリング
        selected_products = Product.objects.filter(id__in=selected_product_ids)
        
        if action_type == "update":
            # 商品一覧画面で更新ボタン押下時に、セッションデータを設定する。
            request.session['selected_products'] = selected_product_ids
            return redirect(reverse('register_food:update_confirmation'))

        return render(request, 'register_food/product_update.html', {'selected_products': selected_products})

class ProductUpdateExcuteView(View): 
    # 確認画面からデータを受け取り、商品情報を更新するためのビュー。
    def get(self, request):
        # 選択された商品データ(プロダクトID)のセッション取得処理
        selected_product_ids = request.session.get('selected_products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)
        return render(request, 'register_food/product_update.html', {'selected_products': selected_products})
    
    def post(self, request):
        # 選択された商品データ(プロダクトID)のセッション取得処理
        selected_product_ids = request.session.get('selected_products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)

        if request.POST.get('confirm_update'):
            # フォームデータを受け取り、商品情報を更新
            for product in selected_products:
                product.product_name = request.POST.get('product_name')
                product.price = request.POST.get('price')
                product.place = request.POST.get('place')
                product.payment_date = request.POST.get('payment_date')
                print(product.meal_format)
                print(request.POST.get('meal_format'))
                product.meal_format = request.POST.get('meal_format')
                
                product.category = request.POST.get('category')
                product.degree_regret = request.POST.get('degree_regret')
                # 他のフィールドも同様に更新
                product.save()
            # セッションデータの削除
            del request.session['selected_products']
            # 商品一覧画面にリダイレクト
            return redirect(reverse('register_food:product_list'))
        return redirect(reverse('register_food:product_list'))

class ProductDeleteView(View):
    def post(self,request):
        # チェックボックスで選択されたデータを取得
        selected_product_ids = request.POST.getlist('selected_products')
        # アクションタイプの取得
        action_type = request.POST.get('action_type')
        # selected_product_ids = request.POST.get('selected_products')

        # 削除処理の場合
        if action_type == "delete":
            # チェックされたデータでフィルタリング
            selected_products = Product.objects.filter(id__in=selected_product_ids)
            # 削除処理実行
            selected_products.delete()
            # 商品一覧画面にリダイレクト
            return redirect(reverse('register_food:product_list'))
        return redirect(reverse('register_food:product_list'))



#-----削除と更新処理を追加(20230813) To -------#