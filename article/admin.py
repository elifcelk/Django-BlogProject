from django.contrib import admin

# Register your models here.
from .models import Article
@admin.register(Article) #decoratör
class ArticleAdmin(admin.ModelAdmin):  #admin panelini özelleştirmek için
    
    list_display =["title","author","created_date"] #bu kısımlar da gözüksün
    list_display_links =["title","created_date"] #bu kısımlarda link özelliği
    search_fields = ["title"] #buna göre  arama özelliği
    list_filter = ["created_date"] #bu özelliğe göre filtreleme
    class Meta:
        model = Article #articleadmin classı ile article ı birleştirmiş oluyoruz.
