
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MinMax , name="minmax"),
    path('lastmonth', views.lastMonth , name="lastmonth"),
    path('last2weeks', views.last2Weeks , name="last2weeks"),
    path('lastweek', views.lastWeek , name="lastweek"),
    path('today', views.Today , name="today"),
    path('getMinMax', views.getMinMax , name="getMinMax"),
    path('getLastMonth', views.getLastMonth , name="getLastMonth"),
    path('getLast2Weeks', views.getLast2Weeks , name="getLast2Weeks"),
    path('getLastWeek', views.getLastWeek , name="getLastWeek"),
    path('getToday', views.getToday , name="getToday"),
    path('LastMonthHours', views.LastMonthHours , name="LastMonthHours"),
    path('Last2WeeksHours', views.Last2WeeksHours , name="Last2WeeksHours"),
    path('LastWeekHours', views.LastWeekHours , name="LastWeekHours"),
    path('TodayHours', views.TodayHours , name="TodayHours"),
]
