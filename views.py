from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from pure_pagination.mixins import PaginationMixin

import os

from .models import App01

# Create your views here.

class App01ListView(PaginationMixin,ListView):
    model = App01
    template_name ='app01/app01_list.html'
    paginate_by = 3
    #絞り込みボタンをクリックした時の表示
    def get_queryset(self):

        QuerySet = self.model.objects.all()
        q_company = self.request.GET.get('company_ID')

        #indexの初期表示以外のとき
        if q_company is not None:
            #null以外のとき

            if q_company != "":
                #検索を繰り返す時に全件から絞り込みを行う
                #単純条件の場合の書き方
                #QuerySet = QuerySet.filter(company_ID__contains=q_company)
                
                #複合条件の場合
                #QuerySet = QuerySet.filter(Q(title__icontains=q_company) | Q(content__icontains=q_company))
                
                #複数モデルで複合条件の場合
                QuerySet = QuerySet.filter(Q(title__icontains=q_company) | Q(company_ID__name__icontains=q_company))

        return QuerySet

 

class App01DetailView(DetailView):
    model = App01


class App01CreateView(CreateView):
     model = App01
     fields = [ "title","content","company_ID" ]
     success_url = reverse_lazy("index")

class App01UpdateView(UpdateView):
    model = App01
    fields = [ "title","content","company_ID" ]
 #   form_class = App01Form

    def get_success_url(self):
        model_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": model_pk})
        return url


     
