#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from accounts.views import (
    login, 
    logout, 
    create,
    update,
    delete,
    account,
    accounts
)

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('', accounts, name="accounts"),
    path('<int:id>/', account, name="account"),
    path('<int:id>/create/', create, name="account_create"),
    path('<int:id>/update/', update, name="account_update"),
    path('<int:id>/delete/', delete, name="account_delete"),
]
