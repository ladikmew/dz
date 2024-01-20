# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
<<<<<<< HEAD

from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by("-datetime")
    # output = ", ".join([q.title for q in latest_post_list])
    # return HttpResponse(output)

=======
from .models import Post


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
>>>>>>> 591582992b91df85190d8a066deaadf44176e86c
    template = loader.get_template("blog/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
<<<<<<< HEAD
    post = Post.objects.get(pk=post_id)

    template = loader.get_template("blog/post.html")
    context = {
        "post": post,
        "post_id": post_id,
    }
    return HttpResponse(template.render(context, request))
=======
    post = Post.object.get(pk=object_id)
    output = post.text
    return HttpResponse
    # return render(request, "polls/detail.html", {"question": question})
>>>>>>> 591582992b91df85190d8a066deaadf44176e86c
