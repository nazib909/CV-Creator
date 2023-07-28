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
    profile = Profile.objects.filter(user=request.user).last()
    return render(request, "cv.html", {"profile": profile})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("createProf")
        else:
            messages.success(request, "Login failed")
            return redirect(login)

    return render(request, "login.html")


def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User arleady exist")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email arleady used")
                return redirect("registration")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email
                )
                user.set_password(password1)
                user.save()
                messages.success(request, "Profile successfully created")
                return redirect("login")
    return render(request, "registration.html")


@login_required
def createCV(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES

        contacts = Contact.objects.create(
            email=data["email"],
            phone=data["phone"],
            portfolio=data["portfolio"],
            linkedin=data["linkedin"],
            github=data["github"],
            twitter=data["twitter"],
        )

        edus = []
        for i in range(1, 3):
            degree = data.get(f"degree{i}")
            institution = data.get(f"institute{i}")
            passing_year = data.get(f"passingyear{i}")
            if degree and institution and passing_year:
                edus.append(
                    Edu(
                        degree=degree, institution=institution, passingyear=passing_year
                    )
                )

        Edu.objects.bulk_create(edus)

        skills = []
        for i in range(1, 7):
            skill_name = data.get(f"skill{i}")
            proficiency = data.get(f"proficiency{i}")
            if skill_name and proficiency:
                skills.append(Skill(s_name=skill_name, proficiency=proficiency))

        Skill.objects.bulk_create(skills)

        projects = []
        for i in range(1, 5):
            project_name = data.get(f"projectname{i}")
            project_details = data.get(f"pdetails{i}")
            if project_name and project_details:
                projects.append(Project(p_name=project_name, des=project_details))

        Project.objects.bulk_create(projects)

        experiences = []
        for i in range(1, 3):
            title = data.get(f"title{i}")
            company_name = data.get(f"companyname{i}")
            duration = data.get(f"duration{i}")
            details = data.get(f"details{i}")
            if title and company_name and duration and details:
                experiences.append(
                    Experience(
                        j_title=title,
                        c_name=company_name,
                        duration=duration,
                        des=details,
                    )
                )

        Experience.objects.bulk_create(experiences)

        languages = []
        for i in range(1, 4):
            language_name = data.get(f"language{i}")
            fluency = data.get(f"fluency{i}")
            if language_name and fluency:
                languages.append(Language(l_name=language_name, fluency=fluency))

        Language.objects.bulk_create(languages)

        interests = []
        for i in range(1, 4):
            interest_name = data.get(f"interest{i}")
            if interest_name:
                interests.append(Interest(i_name=interest_name))

        Interest.objects.bulk_create(interests)

        name = data["name"]
        image = files["image"]
        carrier_profile = data["carrier_profile"]
        user = request.user
        profile = Profile.objects.create(
            name=name,
            image=image,
            carrier_profile=carrier_profile,
            user=user,
            contacts=contacts,
        )

        profile.edus.set(edus)
        profile.skills.set(skills)
        profile.projects.set(projects)
        profile.experiences.set(experiences)
        profile.languages.set(languages)
        profile.interests.set(interests)

    return redirect("cv")


def updateCV(request):
    profile = Profile.objects.get(user=request.user)
    languages = profile.languages.all()

    if request.method == "POST":
        profile.name = request.POST["name"]
        profile.email = request.POST["email"]

        if request.FILES.get("image"):
            if profile.image:
                os.remove(profile.image.path)
            profile.image = request.FILES["image"]

        profile.phone = request.POST["phone"]
        profile.portfolio = request.POST["portfolio"]
        profile.carrier_profile = request.POST.get("carrier_profile")

        profile.save()

        # Update language section
        for i, language in enumerate(languages):
            language_name = request.POST.get(f"language{i + 1}")

            fluency_level = request.POST.get(f"fluency{i + 1}")

            language.l_name = language_name
            language.fluency = fluency_level
            language.save()

        return redirect("cv")

    language_data = [
        {"language": lang.l_name, "fluency": lang.fluency} for lang in languages
    ]

    while len(language_data) < 3:
        language_data.append({"language": "", "fluency": ""})

    return render(
        request, "cv_update.html", {"profile": profile, "languages": language_data}
    )


def createProf(request):
    profile = Profile.objects.filter(user=request.user).last()
    return render(request, "cv_create.html", {"profile": profile})


def setting(request):
    return render(request, "setting.html")


def forgot(request):
    return render(request, "forgot.html")


def changePassword(request):
    user = User.objects.get(id=request.user.id)
    if (
        user.check_password(request.POST["current_password"])
        and request.POST["password1"] == request.POST["password2"]
    ):
        newPassword = make_password(request.POST["password1"])
        user.password = newPassword
        user.save()
        messages.success(request, "Password Changed Successfully")
    return redirect("login")


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("login")


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(login)
