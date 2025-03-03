from django.shortcuts import render, redirect
from .models import Feedback, Government
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests, json
from django.contrib.auth.models import User
from django.conf import settings

# Different API Keys used thoughtout the application
API_KEY = settings.API_KEY
NEPAL_API = settings.NEPAL_API
KHALTI_API = settings.KHALTI_API


def home(request):
    """
    Renders the home page with national news fetched from an external API.

    Fetches the latest 8 national news articles from the specified API and passes them to the 'home.html' template.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'home.html' template and national news data.
    """
    national = f'https://newsdata.io/api/1/news?country=np&apikey={NEPAL_API}&domain=onlinekhabar,Nagarik News,The Himalayan Times'
    national_news = requests.get(national).json()['results'][:8]
    return render(request, 'home.html', {'national_news': national_news})


def register(request):
    """
    Handles user registration.

    Processes the registration form submission, validates the input, and creates a new user if the data is valid.
    Displays appropriate error messages if the username or email already exists or if passwords do not match.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'auth/register.html' template or a redirect to the login page.
    """
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = data['password']
        password1 = data['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                messages.success(request, 'Registered successfully!')
                return redirect('log_in')
        else:
            messages.error(request, "Password doesn't match")
            return redirect('register')

    return render(request, 'auth/register.html')


def log_in(request):
    """
    Handles user login.

    Authenticates the user with the provided username and password. If successful, logs the user in and redirects to the home page.
    Displays an error message if authentication fails.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'auth/login.html' template or a redirect to the home page.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome")
            return redirect('home')
        else:
            messages.error(request, "Try again!")
            return redirect('log_in')
    return render(request, 'auth/login.html')


def log_out(request):
    """
    Handles user logout.

    Logs out the currently authenticated user and redirects to the login page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with a redirect to the login page.
    """
    logout(request)
    return redirect('log_in')


def feedback(request):
    """
    Handles user feedback submission and display.

    Processes feedback form submissions, saves the feedback to the database, and displays all feedback entries.
    Supports file uploads for feedback images.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'feedback.html' template and feedback data.
    """
    if request.method == 'POST' and request.FILES:
        data = request.POST
        name = data['name']
        email = data['email']
        desc = data['desc']
        image = request.FILES['image']
        ob = Feedback(name=name, email=email, desc=desc, image=image)
        ob.save()
        messages.success(request, "Successfully added!")
        return redirect('feedback')

    data = Feedback.objects.all()
    return render(request, 'feedback.html', {'data': data})


def news(request):
    """
    Renders the news page with various categories of news.

    Fetches international, national, financial, and sports news from external APIs and passes them to the 'news.html' template.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'news.html' template and news data.
    """
    url = f'https://newsapi.org/v2/everything?domains=bbc.co.uk&apiKey={API_KEY}'
    articles = requests.get(url).json()['articles']
    international_news = articles[:8]

    national = f'https://newsdata.io/api/1/news?country=np&apikey={NEPAL_API}&domain=onlinekhabar,Nagarik News'
    national_news = requests.get(national).json()['results'][:8]
    latest_news = national_news[:1]
    trending_news = national_news[2:5]

    finance1 = f'https://newsdata.io/api/1/news?apikey={NEPAL_API}&country=np&category=business'
    financial_news = requests.get(finance1).json()['results'][:8]

    sports1 = f'https://newsdata.io/api/1/news?apikey={NEPAL_API}&q=sports&country=np&category=sports'
    sports_news = requests.get(sports1).json()['results'][:8]

    return render(request, 'news.html', {
        'articles': articles,
        'latest_news': latest_news,
        'national_news': national_news,
        'financial_news': financial_news,
        'sports_news': sports_news,
        'international_news': international_news,
        'trending_news': trending_news,
    })


def about(request):
    """
    Renders the about page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'about.html' template.
    """
    return render(request, 'about.html')


def government(request):
    """
    Renders the government page with a list of government sites.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'government.html' template and government data.
    """
    data = Government.objects.all()
    return render(request, 'government.html', {'data': data})


def searchGov(request):
    """
    Handles searching for government sites.

    Processes the search query and filters government sites based on the title.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'searchGov.html' template and search results.
    """
    if request.method == 'POST':
        searched = request.POST['searched']
        finds = Government.objects.filter(title__contains=searched)
        return render(request, 'searchGov.html', {'finds': finds})


def notices(request):
    """
    Renders the notices page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered 'notices.html' template.
    """
    return render(request, 'notices.html')


def initkhalti(request):
    """
    Initiates a Khalti payment.

    Processes payment initiation by sending a request to the Khalti API with the provided payment details.
    Redirects the user to the Khalti payment URL.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with a redirect to the Khalti payment URL.
    """
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = request.POST.get('return_url')
    website_url = request.POST.get('return_url')
    amount = 1000
    purchase_order_id = request.POST.get('purchase_order_id')
    purchase_order_name = request.POST.get('purchase_order_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')

    payload = json.dumps({
        "return_url": return_url,
        "website_url": return_url,
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": purchase_order_name,
        "customer_info": {
            "name": username,
            "email": email,
            "phone": phone,
        }
    })

    headers = {
        'Authorization': f'Key {KHALTI_API}',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    new_res = json.loads(response.text)
    return redirect(new_res['payment_url'])
