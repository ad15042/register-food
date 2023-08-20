from django.urls import path

from .views import *

app_name = "register_food"
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    # 新規登録
    path('entryform/', ProductCreateView.as_view(), name='entryform'),
    # 削除
    path('delete/', ProductDeleteView.as_view(), name='delete'),
    # 削除確認
    # path('delete_confirmation/', DeleteConfirmationView.as_view(), name='delete_confirmation'),
    # 更新
    path('update/', ProductUpdateView.as_view(), name='update'),
    # 更新処理実行確認
    path('update_confirmation/', ProductUpdateExcuteView.as_view(), name='update_confirmation'),
]