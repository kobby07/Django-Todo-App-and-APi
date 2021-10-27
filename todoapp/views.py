from django.shortcuts import redirect, render

from todoapp.serializer import todoserializer, ListTodoSerializer
from .models import mytodo
from .forms import todoform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def home(request):
    task= list(reversed(mytodo.objects.all()))
    form = todoform()
    if request.method == 'POST':
        form = todoform(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'todoapp/home.html', {'task':task, 'form':form})


# API - create
class CreateTask(APIView):
    def post(self, request):
        form = todoserializer(data=request.data)
        form.is_valid(raise_exception=True)

        if len(form.data['task']) > 5:
            form.save()
        

            return Response({
            "message":"You just created a task"  
            })
        else:
            return Response({
            "message":"Your task is too short"  
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    # def get(self, request):
    #     tasks = mytodo.objects.all()

    #     tasks = ListTodoSerializer(tasks, many=True)

    #     return Response(
    #         {
    #             "tasks":tasks.data
    #         }
    #     )


class RetrieveTasks(APIView):
    def get(self, request):
        tasks = mytodo.objects.all()

        tasks = ListTodoSerializer(tasks, many=True)

        return Response(
            {
                "tasks":tasks.data
            }
        )


class UpdateTodo(APIView):
    def put(self, request, id):

        data_sent = todoserializer(data=request.data)
        data_sent.is_valid(raise_exception=True)


        task_text = data_sent.data['task']

        task = mytodo.objects.get(id=id)

        task.task=task_text

        task.save()
    
        return Response({
        "message":"You just updated a task"  
        })





def delete(request, pk):
    task= mytodo.objects.get(id =pk)
    task.delete()
    return redirect('home')


class Delete(APIView):
    def delete(self, request, id):
        task = mytodo.objects.get(id=id)
        task.delete()
        return Response(
            {
                "message":"deleted "
            }
        )


def edit(request, pk):
    task= mytodo.objects.get(id = pk)
    editform = todoform(instance= task)
    if request.method == 'POST':
        editform = todoform(request.POST, instance=task)
        if editform.is_valid():
            editform.save()
            return redirect('home')
    return render(request, 'todoapp/edit.html', {'task':task, 'editform':editform})

