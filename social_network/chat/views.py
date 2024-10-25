from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .forms import MyModelForm
# # Create your views here.



def chat_view(request):
    # return redirect('apps:main_view')
    return HttpResponse("None")


def chat_room(request):
    context={}
    # return render(request,'chat/chat.html',context)
    return HttpResponse("None")





# def form_view(request):
#     form=MyModelForm()
#     if request.method=="POST":
#         form=MyModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("apps:main_view")
#         else:
#             return HttpResponse("Error")
#     form=MyModelForm()
#     context={'form':form}
#     return render(request,"chat/form.html",context)