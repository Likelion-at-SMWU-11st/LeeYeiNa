from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostBasedfForm, PostCreatedForm, PostDetailForm


def index(request):
    post_list = Post.objects.all().order_by("-created_at")  # Post 객체를 최신순으로 정렬
    context = {  # 딕셔너리 형태
        'post_list': post_list,
    }
    return render(request, 'index.html', context)


def post_list_view(request):
    post_list = Post.objects.all()  # Post 모델에 있는 객체 전부 불러오기
    # .filter(writer=request.user) 현재 로그인한 작성자만 필터링
    content = {  # Post 객체를 리스트 형태로 담기
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', content)


def post_detail_view(request, id):
    try:  # 없는 Post일 경우 에러 처리
        post = Post.objects.get(id=id)  # 하나의 데이터만 불러오기
    except Post.DoesNotExist:  # 존재하지 않는 게시글을 조회할 경우
        return redirect('index')  # index.html로 리다이렉트
    post = Post.objects.get(id=id)
    context = {
        'post': post,
        'form': PostDetailForm(),
    }
    return render(request, 'posts/post_detail.html', context)


# 로그인 시에만 처리 가능한 함수
@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        # 데이터 받기
        image = request.FILES.get('image')
        content = request.POST.get('content')
        # Post모델에 전달받은 데이터 저장
        Post.objects.create(image=image, content=content, writer=request.user)
        return redirect('index')


@login_required
def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreatedForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreatedForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user,
            )
        else:  # 잘못된 형식이면 다시 입력
            return redirect('post:post-create')
        return redirect('index')
        '''
        # 데이터 받기
        image = request.FILES.get('image')
        content = request.POST.get('content')
        # Post모델에 전달받은 데이터 저장
        Post.objects.create(image=image, content=content, writer=request.user)
        '''


@login_required
def post_update_view(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)  # Post가 없을 경우 404페이지로 이동시켜줌
    if request.method == 'GET':
        context = {'post': post}
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        # print(image)
        # print(content)
        # 수정된 내용으로 저장된 내용 변경
        if new_image:  # 사진이 변경되었을 경우
            post.image.delete()  # 기존의 이미지 삭제
            post.image = new_image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)


@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.writer:
        return Http404("잘못된 접근입니다.")

    if request.method == "GET":
        context = {'post': post}
        return render(request, 'posts/post_confirm_delete.html', context)
    elif request.method == "POST":
        post.delete()  # 삭제하기
        return redirect('index')


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
