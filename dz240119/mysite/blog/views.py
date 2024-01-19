# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Post


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    template = loader.get_template("blog/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    post = Post.object.get(pk=object_id)
    output = post.text
    return HttpResponse
    # return render(request, "polls/detail.html", {"question": question})