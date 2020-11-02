from django.urls import path
from pagoomi import views

urlpatterns = [
    path('',views.index,name='index'),
    path('curiosidad/<int:pk>',views.CuriosidadDetailView.as_view(),name='curiosidad_detail'),
    path('curiosidad/create/',views.CuriosidadCreate.as_view(),name="curiosidad_create"),
    path('curiosidad/<int:pk>/update/',views.CuriosidadUpdate.as_view(),name="curiosidad_update"),
    path('curiosidad/<int:pk>/delete/',views.CuriosidadDelete.as_view(),name="curiosidad_delete"),
]
