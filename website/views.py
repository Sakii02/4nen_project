import csv
import cgi
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import TSVUploadForm
from .models import Post
from tkinter import messagebox

# 変換後のデータを格納するリスト
trans_list = []

class PostIndex(generic.ListView):
    model = Post


class PostImport(generic.FormView):
    template_name = 'website/import.html'
    success_url = reverse_lazy('website:index')
    form_class = TSVUploadForm

    def form_valid(self, form):
        form.save()
        return redirect('website:index')
  


def post_export(request):
    response = HttpResponse(content_type='text/tsv')
    response['Content-Disposition'] = 'attachment; filename="translatedList.tsv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response, delimiter='\t')
    for post in trans_list:
        writer.writerow([post[0], post[1]])
    return response


def translate(request):
    # response = HttpResponse(content_type='text/tsv')
    # response['Content-Disposition'] = 'attachment; filename="posts.tsv"'
    
    # writer = csv.writer(response, delimiter='\t')

    # file = open('review_list.tsv', 'w')
    # writer = csv.writer(file, delimiter='\t')

    trans_list.clear()


    # 文字列の置換(ここにレビューの変換アルゴリズム書く)
    for post in Post.objects.all():
        if 'こんにちは' in post.title:
            trans_list.append([post.pk, post.title.replace('こんにちは', 'Hello')])
        else:
            trans_list.append([post.pk, post.title])

    params = {
        'trans_list' : trans_list,
        'post_list' : Post.objects.all()
    }

    return render(request, 'website/post_list.html', params)