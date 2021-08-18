from django.contrib import admin

# Register your models here.
from .models import Article
@admin.register(Article) #decoratör
class ArticleAdmin(admin.ModelAdmin):  #admin panelini özelleştirmesi
    
    list_display =["title","author","created_date"] 
    list_display_links =["title","created_date"] 
    search_fields = ["title"] 
    list_filter = ["created_date"] 
    class Meta:
        model = Article #articleadmin classı ile article ı birleştirir
