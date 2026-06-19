from django.contrib import admin
from ManageCash.models import *

# Register your models here.

admin.site.register([
    User,
    AddCashModel,
    ExpenseModel,
])