from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate
from .models import UserProfile, Influencer,Like, Post
from .forms import UserForm, ProfileAccountTypeForm,ProfilePictureForm,ProfileLifeForm,ProfileWayForm, EditUserForm, EditProfileForm, NoteForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse


def notes(request, user):
    user = get_object_or_404 (User, username=user)
    influencers = 0
    if request.user.username == user.username:
        owner = True
        user_profile = request.user.userprofile
    else:
        owner = False
        user_profile = user.userprofile
    post_list=[]
    like_list =[]
    searched_user = 0
    if request.method == 'POST':
        if 'usersearch' in request.POST:
            username = request.POST.get("usersearch")
            searched_user = get_object_or_404 (User, username=username)
            user = request.user.userprofile
        if 'text' in request.POST:
            post_text = request.POST.get("text")
            num_post = user_profile.post_set.count()
            count_post=num_post+1
            current_post = user_profile.post_set.create(text=post_text, post_id=count_post)
            #current_post.save()
            current_like = current_post.like_set.create()
            #current_like.save()
    post_list = user_profile.post_set.all()

    #for index, l in enumerate (post_list):
    #    #it is only one like object per post object, but need to get it this way
    #    like_object = post_list[index].like_set.all()
    #    for i, li in enumerate (like_object):
    #        like_list.append(like_object[i].likecount)



    #note_form = NoteForm()
    #return render (request, 'carte/notes.html',
    #               {'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'note_form': note_form,'post_list': post_list})

    context = {'request': request, 'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'note_form': note_form,'post_list': post_list}
    return JsonResponse(context)


def influencers(request, user):
    user = get_object_or_404 (User, username=user)
    influencers = 0
    if request.user.username == user.username:
        owner = True
        user_profile = request.user.userprofile
        # check his influencers
        influencer_object, created = Influencer.objects.get_or_create (current_user=request.user.userprofile)
        influencers = [friend for friend in influencer_object.influencers.all () if friend != request.user.userprofile]
    else:
        owner = False
        user_profile = user.userprofile

    searched_user = 0
    if request.method == 'POST':
        if 'usersearch' in request.POST:
            username = request.POST.get ("usersearch")
            searched_user = get_object_or_404 (User, username=username)
            user = request.user.userprofile

    #return render (request, 'carte/myinfluencers.html',
    #               {'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers})
    context = {'request': request,'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers}
    return JsonResponse (context)

def consultations(request, user):
    user = get_object_or_404 (User, username=user)
    influencers = 0
    if request.user.username == user.username:
        owner = True
        user_profile = request.user.userprofile
        # check his influencers
        influencer_object, created = Influencer.objects.get_or_create (current_user=request.user.userprofile)
        influencers = [friend for friend in influencer_object.influencers.all () if friend != request.user.userprofile]
    else:
        owner = False
        user_profile = user.userprofile

    searched_user = 0
    if request.method == 'POST':
        if 'usersearch' in request.POST:
            username = request.POST.get ("usersearch")
            searched_user = get_object_or_404 (User, username=username)
            user = request.user.userprofile

    #if request.method == 'POST':
    #    if 'newpost' in request.POST:
    #return render (request, 'carte/myconsultations.html',
    #               {'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers})
    context = {'request': request,'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers}
    return JsonResponse (context)


def way(request, user):
    user = get_object_or_404 (User, username=user)
    influencers = 0
    if request.user.username == user.username:
        owner = True
        user_profile = request.user.userprofile
        # check his influencers
        influencer_object, created = Influencer.objects.get_or_create (current_user=request.user.userprofile)
        influencers = [friend for friend in influencer_object.influencers.all () if friend != request.user.userprofile]
    else:
        owner = False
        user_profile = user.userprofile

    searched_user = 0
    if request.method == 'POST':
        if 'usersearch' in request.POST:
            username = request.POST.get ("usersearch")
            searched_user = get_object_or_404 (User, username=username)
            user = request.user.userprofile

    #return render(request, 'carte/myway.html',
    #               {'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers})
    context = {'request': request,'user': user_profile, 'owner': owner, 'searched_user': searched_user, 'influencers': influencers}
    return JsonResponse(context)


def userpage(request, searched_user_profile):
    user = get_object_or_404 (User, username=searched_user_profile)
    influencers = 0
    if request.user.username == searched_user_profile:
        owner = True
        user_profile = request.user.userprofile
        #check his influencers
        influencer_object, created = Influencer.objects.get_or_create (current_user=request.user.userprofile)
        influencers = [friend for friend in influencer_object.influencers.all () if friend != request.user.userprofile]
    else:
        owner = False
        user_profile = user.userprofile

    searched_user = 0
    if request.method == 'POST':
        if 'usersearch' in request.POST:
            username = request.POST.get("usersearch")
            searched_user = get_object_or_404(User, username=username)
            user = request.user.userprofile

    #if request.method == 'POST':
    #    if 'newpost' in request.POST:
    #return render(request, 'carte/mylife.html',
    #               {'user': user_profile, 'owner': owner,  'searched_user': searched_user, 'influencers': influencers})
    context={'request': request,'user': user_profile, 'owner': owner,  'searched_user': searched_user, 'influencers': influencers}
    return JsonResponse (context)


def subscribe(request, name):
    infl = get_object_or_404(User, username=name)
    Influencer.add_influencer(request.user.userprofile, infl.userprofile)
    #return render(request, 'carte/userpage.html', {'user': request.user.userprofile, 'owner': owner})
    return redirect('/carte/' + 'account/' + request.user.username )

def likepost(request, user, post_id):
    user = get_object_or_404(User, username=user)
    userprofile = user.userprofile
    post = userprofile.post_set.get(post_id= post_id)
    print("here")
    print(post)
    like = post.like_set.all()
    print(like)
    for index,l in enumerate(like):
        if post.likecount == None:
            us_liked = [friend for friend in like[index].users_liked.all()]
            print(us_liked)
            add_like = True
            for i, u in enumerate (us_liked):
                if us_liked[i]== request.user.userprofile:
                    add_like = False
            if add_like == True:
                like[index].users_liked.add(request.user.userprofile)
                print("here1")
                post.likecount = 1
                post.save()


        else:
            us_liked = [friend for friend in like[index].users_liked.all ()]
            print (us_liked)
            add_like = True
            for i, u in enumerate (us_liked):
                if us_liked[i] == request.user.userprofile:
                    add_like = False
            if add_like == True:
                like[index].users_liked.add(request.user.userprofile)
                print("here2")
                post.likecount = post.likecount + 1
                post.save()
                #like[index].save()
        #print(like[index].likecount)
        print (like[index].users_liked.all())
    return redirect ('/carte/' + 'account/' + user.username + '/notes')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = auth_authenticate(request, username=username, password=password)
        users = User.objects.all()
        if user is not None:
            auth_login(request, user)
            user = request.user.userprofile
            owner = True
            searched_user_profile = 0
            return redirect ('/carte/' + 'account/'+ request.user.username)
            #userpage(request, request.POST.get('username'))
            #return render(request, 'carte/userpage.html', {'user': user, 'owner': owner})
            context = {'request': request,'loggedin_userprofile': user, 'owner': owner}
            return JsonResponse (context)
        else:
            username = request.POST.get("usersearch")
            searched_user = get_object_or_404(User, username=username)
            owner = True
            user = request.user.userprofile
            #return render(request, 'carte/mylife.html', {'user': user, 'owner': owner, 'searched_user': searched_user})
            context = {'request': request,'loggedin_userprofile': user, 'owner': owner, 'searched_user': searched_user}
            return JsonResponse(context)
    else:
        user_form = UserForm()
        #return render(request, 'carte/login.html',
        #           {'user_form': user_form})
        context = {'user_form': user_form }
        return JsonResponse (context)


def register(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            uform = UserForm(data=request.POST)
            if uform.is_valid():
                user = uform.save ()
                # form brings back a plain text string, not an encrypted password
                pw = user.password
                # thus we need to use set password to encrypt the password string
                user.set_password (pw)
                user.save()
                #login
                username = request.POST.get ('username')
                password = request.POST.get ('password')
                print (username)
                print (password)
                user = auth_authenticate(request, username=username, password=password)
                auth_login (request, user)
            pform = ProfileAccountTypeForm(data=request.POST)
            if pform.is_valid():
                profile = pform.save(commit=False)
                profile.user = user
                profile.save()
                #forms staff
                user_form = 0
                profile_form = ProfilePictureForm()
        if 'profile_pic' in request.FILES:
            pform = ProfilePictureForm(data=request.POST, instance=request.user.userprofile, files=request.FILES)
            if pform.is_valid ():
                profile = pform.save()
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                # forms staff
                user_form = 0
                profile_form = ProfileLifeForm()
        if 'life_desc' in request.POST:
            pform = ProfileLifeForm(data=request.POST, instance=request.user.userprofile)
            if pform.is_valid():
                profile = pform.save()
                profile.save()
                #forms staff
                user_form = 0
                profile_form = ProfileWayForm()
        if 'way_desc' in request.POST:
            pform = ProfileWayForm(data=request.POST, instance=request.user.userprofile)
            if pform.is_valid ():
                profile = pform.save()
                profile.save ()
                return redirect('/carte/' + 'account/' + request.user.username )

    else:
        user_form= UserForm()
        profile_form = ProfileAccountTypeForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return JsonResponse(context)
    #return render (request, 'carte/register.html', context)

def edit(request, user):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        userprofile_form = EditProfileForm(request.POST, instance=request.user.userprofile, files=request.FILES)

        if form.is_valid and userprofile_form.is_valid:
            form.save()
            profile = userprofile_form.save(commit=False)
            #profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                print ('here')
            profile.save()
            return redirect ('/carte/' + 'account/' + request.user.username)

    else:
        user_form = EditUserForm(instance=request.user)
        userprofile_form = EditProfileForm(instance=request.user.userprofile)
        #return render(request, 'carte/edit.html',
        #           {'user_form': user_form, 'userprofile_form': userprofile_form})
        context = {'request': request, 'user_form': user_form, 'userprofile_form': userprofile_form}
        return JsonResponse(context)

def index(request):
    return render(request, 'carte/index.html')

