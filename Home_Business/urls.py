"""LikHanap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,
PortfolioDetailView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView, PortfolioListView, 
ProjectListView, LogoArtistListView, TarpArtistListView, AdArtistListView, InviArtistListView,  InteriorArtistListView,
LogoProjectListView, TarpProjectListView, AdProjectListView, InviProjectListView,  InteriorProjectListView,
BidCreateView, BidsListView, BidDetailView, BidUpdateView, BidDeleteView,
ApplyCreateView, ApplyListView, ApplyDetailView, ApplyUpdateView, ApplyDeleteView,
AcceptDetailView, AcceptListView, AcceptCreateView, AcceptUpdateView, AcceptDeleteView,
EmployListView, EmployDetailView, EmployCreateView, EmployUpdateView, EmployDeleteView)
 
from . import views


urlpatterns = [
    path('posts/', PostListView.as_view(), name = 'LikHanap-Business'),

    path('projects/', ProjectListView.as_view(), name = 'LikHanap-Projects'),

    path('logoartist/', LogoArtistListView.as_view(), name = 'Logo-Artist'),

    path('logoproject/', LogoProjectListView.as_view(), name = 'Logo-Project'),

    path('tarpartist/', TarpArtistListView.as_view(), name = 'Tarpaulin-Artist'),

    path('tarpproject/', TarpProjectListView.as_view(), name = 'Tarpaulin-Project'),

    path('adartist/', AdArtistListView.as_view(), name = 'Ad-Artist'),

    path('adproject/', AdProjectListView.as_view(), name = 'Ad-Project'),

    path('inviartist/', InviArtistListView.as_view(), name = 'Invi-Artist'),

    path('inviproject/', InviProjectListView.as_view(), name = 'Invi-Project'),

    path('interiorartist/', InteriorArtistListView.as_view(), name = 'Interior-Artist'),

    path('interiorproject/', InteriorProjectListView.as_view(), name = 'Interior-Project'),

    path('portfolios/', PortfolioListView.as_view(), name = 'LikHanap-Freelance'),
        
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'Post-Detail'),
    
    #
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name = 'Portfolio-Detail'),
    #
    
    path('post/new/', PostCreateView.as_view(), name = 'Post-Create'),
    
    #
    path('portfolios/new/', PortfolioCreateView.as_view(), name = 'Portfolio-Create'),
    #
    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'Post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'Post-Delete'),
    
    #
    path('portfolios/<int:pk>/update/', PortfolioUpdateView.as_view(), name = 'Portfolio-Update'),
    path('portfolios/<int:pk>/delete/', PortfolioDeleteView.as_view(), name = 'Portfolio-Delete'),
    #
    path('bid/new/', BidCreateView.as_view(), name = 'Bid-Create'),

    path('bids/', BidsListView.as_view(), name = 'LikHanap-Bids'),

    path('bid/<int:pk>/', BidDetailView.as_view(), name = 'Bid-Detail'),

    path('bid/<int:pk>/update/', BidUpdateView.as_view(), name = 'Bid-Update'),
    path('bid/<int:pk>/delete/', BidDeleteView.as_view(), name = 'Bid-Delete'),
    #
    path('apply/new/', ApplyCreateView.as_view(), name = 'Apply-Create'),

    path('applies/', ApplyListView.as_view(), name = 'LikHanap-Apply'),

    path('apply/<int:pk>/', ApplyDetailView.as_view(), name = 'Apply-Detail'),

    path('apply/<int:pk>/update/', ApplyUpdateView.as_view(), name = 'Apply-Update'),
    path('apply/<int:pk>/delete/', ApplyDeleteView.as_view(), name = 'Apply-Delete'),
   
    #
    path('accepts/', AcceptListView.as_view(), name = 'Accept'),
    path('accepts/<int:pk>/', AcceptDetailView.as_view(), name = 'Accept-Detail'),
    path('accepts/new/', AcceptCreateView.as_view(), name = 'Accept-Create'),
    path('accept/<int:pk>/update/', AcceptUpdateView.as_view(), name = 'Accept-Update'),
    path('accept/<int:pk>/delete/', AcceptDeleteView.as_view(), name = 'Accept-Delete'),
    #

    path('employs/', EmployListView.as_view(), name = 'Employ'),
    path('employs/<int:pk>/', EmployDetailView.as_view(), name = 'Employ-Detail'),
    path('employs/new/', EmployCreateView.as_view(), name = 'Employ-Create'),
    path('employ/<int:pk>/update/', EmployUpdateView.as_view(), name = 'Employ-Update'),
    path('employ/<int:pk>/delete/', EmployDeleteView.as_view(), name = 'Employ-Delete'),

    

    path('about/', views.about, name = 'LikHanap-About'),
    path('terms/', views.terms, name = 'LikHanap-Terms'),
    path('homestatus/', views.homestatus, name = 'LikHanap-HomeStatus'),
    path('', views.prehome, name='prehome'),
]
