from app.urls import urlpatterns

urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]