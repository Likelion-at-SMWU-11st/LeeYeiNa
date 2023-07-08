from django.contrib import admin
from .models import Post  # models.py import
from .models import Comment
from .models import MyPage

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'


@admin.register(Post)  # admin 페이지 커스터마이징
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'content',
                    'created_at', 'view_count', 'writer']  # admin 페이지에서 보여질 list
    list_editable = ['content', 'writer']  # 콘텐츠와 작성자 편집 가능
    list_filter = ['created_at']  # 생성일에 따라 필터 가능
    search_fields = ('id', 'writer__username')  # id와 글 작성자 검색 가능
    search_help_text = "게시판 번호, 작성자 검색이 가능합니다."
    readonly_fields = ['view_count', 'created_at']
    inlines = [CommentInline, ]

    actions = ['make_published']  # 게시판 액션 추가하기

    def make_published(modeladmin, request, queryset):  # 게시판 액션 함수
        for item in queryset:
            item.content = '운영규칙 위반으로 인한 게시글 삭제 처리'
            item.save()

# admin.site.register(Post)  # Admin 사이트에 Post 모델 추가
# admin.site.register(MyPage)  # MyPage 모델 추가
