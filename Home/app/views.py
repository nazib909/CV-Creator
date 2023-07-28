from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
import os
# Create your views here.


@login_required
def cv(request):
    profile = Profile.objects.filter(
        user=request.user
    ).last()
    return render(request, 'cv.html', {
        'profile': profile
    })


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('createProf')
        else:
            messages.success(request, 'Login failed')
            return redirect(login)

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User arleady exist")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email arleady used")
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.set_password(password1)
                user.save()
                messages.success(request, "Profile successfully created")
                return redirect('login')
    return render(request, 'registration.html')


@login_required
def createCV(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        carrier_profile = request.POST['carrier_profile']
        # education
        degree1 = request.POST['degree1']
        institute1 = request.POST['institute1']
        passingyear1 = request.POST['passingyear1']
        degree2 = request.POST['degree2']
        institute2 = request.POST['institute2']
        passingyear2 = request.POST['passingyear2']

        edus = Edu.objects.bulk_create(
            [Edu(degree=degree1, institution=institute1, passingyear=passingyear1),
             Edu(degree=degree2, institution=institute2, passingyear=passingyear2)]
        )
        # skill
        skill1 = request.POST['skill1']
        proficiency1 = request.POST['proficiency1']
        skill2 = request.POST['skill2']
        proficiency2 = request.POST['proficiency2']
        skill3 = request.POST['skill3']
        proficiency3 = request.POST['proficiency3']
        skill4 = request.POST['skill4']
        proficiency4 = request.POST['proficiency4']
        skill5 = request.POST['skill5']
        proficiency5 = request.POST['proficiency5']
        skill6 = request.POST['skill6']
        proficiency6 = request.POST['proficiency6']

        skills = Skill.objects.bulk_create(
            [Skill(s_name=skill1, proficiency=proficiency1),
             Skill(s_name=skill2, proficiency=proficiency2),
             Skill(s_name=skill3, proficiency=proficiency3),
             Skill(s_name=skill4, proficiency=proficiency4),
             Skill(s_name=skill5, proficiency=proficiency5),
             Skill(s_name=skill6, proficiency=proficiency6)]
        )
        # project
        projectname1 = request.POST['projectname1']
        pdetails1 = request.POST['pdetails1']
        projectname2 = request.POST['projectname2']
        pdetails2 = request.POST['pdetails2']
        projectname3 = request.POST['projectname3']
        pdetails3 = request.POST['pdetails3']
        projectname4 = request.POST['projectname4']
        pdetails4 = request.POST['pdetails4']
        projects = Project.objects.bulk_create(
            [Project(p_name=projectname1, des=pdetails1),
             Project(p_name=projectname2, des=pdetails2),
             Project(p_name=projectname3, des=pdetails3),
             Project(p_name=projectname4, des=pdetails4)]
        )
        # experience
        title1 = request.POST['title1']
        companyname1 = request.POST['companyname1']
        duration1 = request.POST['duration1']
        details1 = request.POST['details1']
        title2 = request.POST['title2']
        companyname2 = request.POST['companyname2']
        duration2 = request.POST['duration2']
        details2 = request.POST['details2']
        experiences = Experience.objects.bulk_create(
            [Experience(j_title=title1, c_name=companyname1,
                        duration=duration1, des=details1,),
             Experience(j_title=title2, c_name=companyname2,
                        duration=duration2, des=details2)]
        )
        # language
        language1 = request.POST['language1']
        fluency1 = request.POST['fluency1']
        language2 = request.POST['language2']
        fluency2 = request.POST['fluency2']
        language3 = request.POST['language3']
        fluency3 = request.POST['fluency3']
        languages = Language.objects.bulk_create(
            [Language(l_name=language1, fluency=fluency1),
             Language(l_name=language2, fluency=fluency2),
             Language(l_name=language3, fluency=fluency3)]
        )
        # interest
        interest1 = request.POST['interest1']
        interest2 = request.POST['interest2']
        interest3 = request.POST['interest3']
        interests = Interest.objects.bulk_create(
            [Interest(i_name=interest1),
             Interest(i_name=interest2),
             Interest(i_name=interest3)]
        )
        # contact
        email = request.POST['email']
        phone = request.POST['phone']
        portfolio = request.POST['portfolio']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        twitter = request.POST['twitter']
        contacts = Contact.objects.create(
            email=email, phone=phone, portfolio=portfolio, linkedin=linkedin, github=github, twitter=twitter)

        user = request.user
        profile = Profile.objects.create(
            name=name, image=image, carrier_profile=carrier_profile, user=user, contacts=contacts)
        profile.edus.set(edus)
        profile.skills.set(skills)
        profile.projects.set(projects)
        profile.experiences.set(experiences)
        profile.languages.set(languages)
        profile.interests.set(interests)

    return redirect('cv')


# def updateCV(request):
#     profile = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         profile.name = request.POST['name']
#         profile.email = request.POST['email']

#         if request.FILES.get('image'):
#             if profile.image:
#                 os.remove(profile.image.path)
#             profile.image = request.FILES['image']

#         profile.phone = request.POST['phone']
#         profile.protfolio = request.POST['portfolio']
#         profile.carrier_profile = request.POST.get('carrier_profile')

#         profile.save()

#         return redirect('cv')
    
#     return render(request, 'cv_update.html',{'profile':profile})

def updateCV(request):
    profile = Profile.objects.get(user=request.user)
    languages = profile.languages.all()

    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.email = request.POST['email']

        if request.FILES.get('image'):
            if profile.image:
                os.remove(profile.image.path)
            profile.image = request.FILES['image']

        profile.phone = request.POST['phone']
        profile.portfolio = request.POST['portfolio']
        profile.carrier_profile = request.POST.get('carrier_profile')

        # Save profile changes
        profile.save()

        # Update language section
        for i, language in enumerate(languages):
            language_name = request.POST.get('language_name[]')[i]
            fluency_level = request.POST.get('fluency[]')[i]

            language.l_name = language_name
            language.fluency = fluency_level
            language.save()

        return redirect('cv')
    
    return render(request, 'cv_update.html', {'profile': profile, 'languages': languages})




def createProf(request):
    profile = Profile.objects.filter(
        user=request.user
    ).last()
    return render(request, 'cv_create.html', {
        'profile': profile
    })


def setting(request):
    return render(request, 'setting.html')


def forgot(request):
    return render(request, 'forgot.html')


def changePassword(request):
    user = User.objects.get(id=request.user.id)
    if user.check_password(request.POST['current_password']) and request.POST['password1'] == request.POST['password2']:
        newPassword = make_password(request.POST['password1'])
        user.password = newPassword
        user.save()
        messages.success(request, 'Password Changed Successfully')
    return redirect('login')


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('login')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect(login)
