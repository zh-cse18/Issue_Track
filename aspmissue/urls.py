from django.contrib import admin
from django.urls import path

from aspmissue import views

app_name = "aspmissue"
urlpatterns = [
    path('', views.index, name='index'),
    path('model_detail/<int:id>', views.modelDetail, name='modelDetail'),
    path('market_issue/', views.marketIssue, name='marketIssue'),
    path('xcel_view/<int:id>', views.xcel_view, name='xcel_view'),
    path('weekly_report/', views.weekly_report, name="Weekly_report"),
    path('after_sales/', views.after_sales_issue, name="after_sales"),
    path('field_test/', views.field_test_report, name="field_test"),
    path('weekly_report_excel/', views.weekly_report_xcel_view, name='weekly_report_xcel_view'),
    path('all_model/', views.xcel_view_all_model, name='xcel_view_all_model'),

]
