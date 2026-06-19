from django.urls import path
from ManageCash.views import *
urlpatterns = [
    path('',register_page,name = 'register_page'),
    path('login-page/',login_page,name = 'login_page'),
    path('logout-page/',logout_page, name='logout_page'),
    path('dashboard-page/',dashboard_page, name='dashboard_page'),
    path('cash-list/',cash_list, name='cash_list'),
    path('addcash-page/',addcash_page, name='addcash_page'),
    path('updatecash-page/<int:id>/',updatecash_page, name='updatecash_page'),
    path('delete-cash/<int:id>/',delete_cash, name='delete_cash'),
    path('expense-list/',expense_list, name='expense_list'),
    path('addexpense-page/',addexpense_page, name='addexpense_page'),
    path('updateexpnese_page/<int:id>/',updateexpnese_page, name='updateexpnese_page'),
    path('delete-expense/<int:id>/',delete_expense, name='delete_expense'),
]