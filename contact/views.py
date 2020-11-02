from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = ContactForm(request.POST)
        form.first_name = request.POST.get("first_name")
        form.last_name = request.POST.get("last_name")
        form.email = request.POST.get("email")
        form.text = request.POST.get("text")

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            try:
                message = 'First_name: %s\nLast_name: %s\nEmail Address: %s\nMessage:\n      %s' % (form.first_name, form.last_name, form.email,form.text)
                send_mail('有人通过vtoo.pro联系你',message,'1360004212@qq.com',['1360004212@qq.com'],fail_silently=False)
            except BaseException:
                pass
            try:
                message_to_client = '\n    %s,你好!我是fuweifu-vtoo，已经收到了你的消息，我会尽快查看并回复邮件的～\n\n\n下面是你的信息和留言:\n\n%s' % (form.last_name,message) 
                send_mail('这是一封来自vtoo.pro的自动回复',message_to_client,'1360004212@qq.com',[form.email],fail_silently=False)
            except BaseException:
                pass
            contact = form.save(commit=False)

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            contact.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            form_empty = ContactForm()
            context = {'form': form_empty,
                       }
            return render(request, 'hydrogen/contact.html', context=context)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            context = {'form': form,
                       }
            return render(request, 'hydrogen/contact.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    form_empty = ContactForm()
    context = {'form': form_empty,
               }
    return render(request, 'hydrogen/contact.html', context=context)