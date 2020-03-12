from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    show_created_todo_item = Todo.objects.all().order_by("-date_added")
    return render(request, 'main/index.html', {"show_created_todo_item": show_created_todo_item})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    show_content = request.POST['content']
    create_obj_and_count = Todo.objects.create(date_added=current_date, text=show_content)
    # count_created_obj_and_show = Todo.objects.all().count()
    # print(count_created_obj_and_show)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

