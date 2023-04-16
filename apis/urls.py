from django.urls import path
from . import views
urlpatterns = [
    
    # Sessions Related Apis start
    path('insert_session/', views.insert_session,name="insert_session"),
    path('get_sessions/', views.get_sessions,name="get_sessions"),
    path('get_session_by_id/', views.get_session_by_id,name="get_session_by_id"),
    path('delete_session_by_id/', views.delete_session_by_id,name="delete_session_by_id"),
    path('update_session/', views.update_session,name="update_session"),
    
    # Sessions Related Apis end

    # User Related Apis start

    path('signup_user/', views.signup_user,name="signup_user"),
    path('signin_user/', views.signin_user,name="signin_user"),
    path('get_user_by_id/', views.get_user_by_id,name="get_user_by_id"),

    path('update_user/', views.update_user,name="update_user"),

]
