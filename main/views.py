from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from .models import City,State, Place
#from .forms import PlaceForm



# homepage view, it will show all the states

def homepage(request):
    return render(request, 'main/home.html', context=None)


def explore(request):
    all_states = State.objects.all()
    return render(request, 'main/index.html', {'all_states': all_states})


# 'city':state.cities.all, is a related name, in which all the city associated with that single state is queried out ,
# ie state with pk =1 , and all CITIES 'related_name' associated to that particular state

def state_detail(request, state_id):
    state = State.objects.get(pk=state_id)
    city = state.cities.all()
    return render(request, 'main/state_detail.html', {'city': city})

# def city_detail(request,state_id):
#     all_city = City.objects.filter(state__pk=state_id)
#     for m in all_city:
#         all_places = Place.objects.filter(city__city_title=m.city_title)
#
#         return render(request,'main/city_detail.html', {'all_places': all_places})

def sign_up(request):

    if request.method == 'POST':

        # fetching data from user
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # checking if both passwords matches or not
        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")

            else:
                # Django ORM
                user = User.objects.create_user(username=username, password=password2)

                # adding user data to the database
                user.save()
                messages.info(request, "User created")
                return redirect('main:homepage')

        else:
            messages.info(request, "Password didn't match")
            return redirect('main:sign_up')

    else:

        # this will be called whether its a get or post request
        return render(request, 'main/signup.html')

# after creating user if login, then a session id is generated along with the backend authenticated are saved in a
# user's session

def log_in(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        # after authentication with authentication backend, it returns a User object & is stored in user variable
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:homepage')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('main:login')

    else:
        return render(request, 'main/login.html')

# clears out the session data
def log_out(request):
    logout(request)
    return redirect('main:login')

# new-form

# def add_place(request):
#     if request.method == "POST":
#         place_title = request.POST['place_title']
#         place_about = request.POST['place_about']
#         city = request.POST['city']
#
#         place = Place.objects.create(place_title=place_title, place_about=place_about, city=city)
#         place.save()
#         return redirect('main:homepage')
#
#     else:
#         return render(request, 'main/new_place.html')

# def add_place(request):
#
#     if request.method == "POST":
#         form = PlaceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main:homepage')
#
#         else:
#             messages.info(request, 'invalid form')
#             return redirect('main:add-place')
#     else:
#
#         form = PlaceForm()
#         return render(request, 'main/new_place.html', {'form': form})
