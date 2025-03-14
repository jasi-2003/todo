from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import Userform,Taskform,Login_form

from django.contrib.auth import authenticate,login,logout

from myapp.models import User,Taskmodel

from django.utils.decorators import method_decorator


def is_user(fn):

    def wrapper(request,**kwargs):

        id = kwargs.get("pk")

        obj = Taskmodel.objects.get(id = id)

        if obj.user_id == request.user  :

            return fn(request,**kwargs)

        else :
            
            return redirect("login")

    return wrapper




class Registrationview(View):

    def get(self,request):

        form = Userform

        return render(request, 'register.html',{'form':form})



    def post(self,request):

        form = Userform(request.POST)

        if form.is_valid():

           User.objects.create_user(**form.cleaned_data)

           form = Userform

           return redirect("login")





class Login(View):

    def get(self,request):

        form = Login_form

        return render(request,'login.html',{'form':form})

    def post(self,request):

        form = Login_form(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            u_name = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user =  authenticate( request, username = u_name,password = pwd)

            if user:

                login(request,user)

                return redirect("create")

            else:

                return render(request,"home.html",{"form":form})


class TaskAdd(View):

    def get(self,request):

        form = Taskform

        data = Taskmodel.objects.filter(user_id = request.user)

        return render(request,"task.html",{"form":form})




    def post(self,request):

       form = Taskform(request.POST)

       if form.is_valid():

         Taskmodel.objects.create(**form.cleaned_data,user_id=request.user)

         data = Taskmodel.objects.filter(user_id = request.user)


         form = Taskform

         return render(request,"task.html",{"form":form, "data":data})


      
class TaskAll(View):

    def get(self,request):

        data = Taskmodel.objects.filter(user_id = request.user ).order_by("is_completed","created_date")

        return render(request,"alltask.html",{"data":data})


@method_decorator(decorator = is_user,name = 'dispatch')    
class TaskDelete(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        data =  Taskmodel.objects.get(id=id)

        if data.user_id == request.user:

            
            data.delete()

            return redirect("all")
        else :

            print("get out")

            return redirect("all")

@method_decorator(decorator=is_user,name='dispatch')    
class TaksUpdate(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        data = Taskmodel.objects.get(id=id)

        form = Taskform(instance=data)

        return  render(request,"update.html",{'form':form})


    def post(self,request,**kwargs):

        id = kwargs.get('pk')

        data = Taskmodel.objects.get(id=id)

        form = Taskform(request.POST,instance=data)

        if form.is_valid:

            form.save()

        return  redirect("all")


@method_decorator(decorator=is_user,name='dispatch')
class TaskDetail(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        data = Taskmodel.objects.get( id = id )

        return render (request,"detail.html",{'data':data})



# http://127.0.0.1:8000/taskedit/<int:pk>/


@method_decorator(decorator=is_user,name='dispatch')
class Taskedit(View):

    def get(self,request,**kwargs):

        id  = kwargs.get('pk')

        data = Taskmodel.objects.get( id = id)

        print(data)

        if data.is_completed == False:

            data.is_completed = True

            data.save()

        return redirect("all")


class singout(View):

    def get(self,request):

        logout(request)

        return redirect("login")


class CompletedView(View):

    def get(self,request):

        data = Taskmodel.objects.filter(user_id= request.user,is_completed=True)

        return render(request,"complete.html",{"data":data})


class Userdetails(View):

    def get(self,request):

        data = Taskmodel.objects.filter(user_id = request.user )

        total = Taskmodel.objects.filter(user_id = request.user).count()

        incompleted = Taskmodel.objects.filter(user_id = request.user,is_completed = False ).count()

        completed = total - incompleted

        return render(request,"userdetails.html",{"total":total,"incompleted":incompleted,"completed" : completed,"data":data})


    