from django.shortcuts import render,HttpResponseRedirect
import random
from .models import users,posts,number
# Create your views here.

# sign up ( add a new user to the database )  
def signup(request):
    if request.method == "POST": # get the form
        #get inputs
        firstname = request.POST.get('first')
        lastname = request.POST.get('sur1')
        email = request.POST.get('mobile1')
        password = request.POST.get('new1')
        #add the user
        users.objects.create(firstname=firstname,lastname=lastname,email=email,password=password)
    return render(request, 'signup.html', {})

#login (search for the user in the database)
def login(request):
    if request.method == 'POST':
        # get user email & password
        email = request.POST.get('email')
        password = request.POST.get('pass')
        db =  users.objects
        # try every user in the database 100 times and if it match the user email & password you are done
        for i in range(100):
            try:
                if email == db.get(id = i).email and password == db.get(id = i).password:
                    db = posts.objects
                    num = int(number.objects.get(id=1).no)
                    # get all titles in the database
                    title = [db.get(id=j).title for j in range(1,num+1)]
                    # get all minds in the database
                    mind = [db.get(id=j).mind for j in range (1,num+1)]
                    # get all images in the database
                    img = [db.get(id=j).img for j in range (1,num+1)]
                    # match the first title with first mind with first img and so on
                    #eg: [ [title1,mind1,img1] , [title2,mind2,img2] ] 
                    kol = zip(title,mind,img)
                    # put it in the html
                    con = {
                        'posts':kol
                    }
                    #open facebook
                    return render(request,'facebook.html', con)
            except: print('no')
    return render(request, 'tests.html', {})


# add a new post to the database
def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        mind = request.POST.get('mind')
        img = request.POST.get('img')
        number.objects.get(id=1).no = int(number.objects.get(id=1).no) + 1
        posts.objects.create(title=title,mind=mind,img=img)
    return render(request, 'post.html', {})



         


 
    

         
        
































      
 
    
        
      
 




