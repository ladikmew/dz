from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post
from comments.forms import CommentForm
from django.http import HttpResponseRedirect
from comments.models import Comment
from django.urls import reverse


def main_views(request):
    latest_post_list = Post.objects.order_by("-datetime")
    # output = ", ".join([q.title for q in latest_post_list])
    # return HttpResponse(output)

    # template = loader.get_template("blog/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    print(context)
    # return HttpResponse(template.render(context, request))
    return render(request, "blog/index.html", context)


# def detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(pk=post_id)
#     # except Post.DoesNotExist:
#     #     raise Http404("Такого поста нет")
#     post = get_object_or_404(Post, pk=post_id)
#     # template = loader.get_template("blog/post.html")
#     context = {
#         "post": post,
#         "post_id": post_id,
#     }
#     #  return HttpResponse(template.render(context, request))
#     return render(request, "blog/post.html", context)

def detail(request, post_id):
    #form = CommentForm()

    latest_post_list = Post.objects.order_by("-datetime")
    post = get_object_or_404(Post, pk=post_id)
    comment_list = Comment.objects.filter(post=post).order_by("datetime")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            text = form.cleaned_data['text']
            comment = Comment.object.create(post=post, username=username, text=text)
            comment.save()
            form.save()
            return HttpResponseRedirect(reverse('detail',args=(post_id,)))

    else:
        form = CommentForm(initial={"post": post.id})

    form.fields["post"].widget.attrs['disabled'] = True
    context = {
        "comments":comment_list,
        "post": post,
        "form": form,
        "latest_post_list": latest_post_list,
    }
    return render(request, "blog/post.html", context)
