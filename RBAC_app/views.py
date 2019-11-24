from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import User,Resources,Role_id
from django.template import loader

def index(request):
    try:
        all_users  = User.objects.all()
        template =  loader.get_template('RBAC_app/index.html')
        context = {
            'all_users' :all_users,
        }
    except:
        raise Http404("nothing exist")
    
    return HttpResponse(template.render(context,request))
        

def userEntry(request, username):
    try:
        username = User.objects.get(username = username)
        
        template =  loader.get_template('RBAC_app/userEntry.html')
        context = {
            'username' : username,
        }
    except:
        raise Http404("nothing exist")

   
    return HttpResponse(template.render(context,request))
    #return HttpResponse("<h1> This is the Users page "+str(username.username)+" </h1>")



def userID(request,username):
    try:
        username = User.objects.get(username = username)
        user_id = username.user_id
        accessLevel = Role_id.objects.get(user_id=user_id)
        
        
        resources = Resources.objects.all().filter(accessLevel = accessLevel.accessLevel)
        template =  loader.get_template('RBAC_app/resources.html')
        context = {

            'resources' : resources,
        }
    except:
        raise Http404("nothing exist")
    return HttpResponse(template.render(context,request))

    #return HttpResponse("<h1> This is the Users page "+str(resources.accessLevel)+" </h1>")

    