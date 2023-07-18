from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post


def index(request):
    post_list = Post.objects.order_by("-created_at")  # Post 객체를 최신순으로 정렬
    content = {
        'post_list': post_list,
    }
    return render(request, 'index.html', content)


def post_list_view(request):
    post_list = Post.objects.all()  # Post 모델에 있는 객체 전부 불러오기
    # filter(writer=request.user) 작성자 필터링
    content = {  # Post 객체를 리스트 형태로 담기
        'post_list': post_list, }
    return render(request, 'posts/post_list.html', content)


def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:  # 존재하지 않는 게시글을 조회할 경우
        return redirect('index')  # index.html로 리다이렉트
    post = Post.objects.get(id=id)
    context = {'post': post, }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(image=image, content=content, writer=request.user)
        return redirect('index')


def post_update_view(request, id):
    return render(request, 'posts/post_update.html')


def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')


class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'


def url_view(request):
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_views</h1>')


def url_parameter_view(request, username):
    print(f'url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)


def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')
