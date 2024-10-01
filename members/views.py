from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
#def members(request):
#    template = loader.get_template('myfirst.html')
#    return HttpResponse(template.render())

# Import the model (member.py) so that we can use it in our view

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))