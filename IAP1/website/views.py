from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import register
# from .forms import *
from django.http import *
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from . forms import UserForm



# Create your views here.

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('website:index')

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/latest-news')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/index.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def base(request):

    return render(request, 'website/base.html')

def breaking(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/amazing')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/breaking.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def business(request):
    import requests
    import bs4
    res=requests.get('https://www.geo.tv/category/business')
    type(res)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    hi = soup.select('.list')

    res2 = requests.get('https://www.geo.tv/latest-news')
    type(res2)
    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    type(soup2)
    hj = soup.select('.list')
    # im=soup.select('.pic')
    # im=soup.find_all('img')
    # im2=str(im[1])
    # im3=im2.find_all('img')
    print(hi)
    # txt=hi[0].getText()
    # str1=','.join(hi)
    str1=str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hj[11])
    str12 = str(hj[1])
    str13 = str(hj[5])
    str14 = str(hj[10])
    str15 = str(hj[11])
    str16 = str(hj[9])
    str17 = str(hj[4])
    str18 = str(hj[0])
    str19 = str(hj[2])
    str20 = str(hj[8])
    # hi = soup.get_text('.menu')
    # print(str1)
    # print(hi)

    # for i in soup.select('.menu'):
    #  register.objects.create(name=i)
    #  print(i)
    #  print(i.text)
    # reg = register.objects.create(name=hi)
    # reg.save()
    #register.objects.create(name=hi)
    # return render(request, 'website/business.html',{'hi':str1,'im2':im2})
    return render(request, 'website/business.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})


def contact(request):
    return render(request, 'website/contact.html')

def entertainment(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/entertainment')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/entertainment.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def events(request):
    return render(request, 'website/events.html')

def lifestyle(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/health')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/lifestyle.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

# def loginform(request):
#     return render(request, 'website/index.html')

def political(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/pakistan')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/political.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def sports(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/sports')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/sports.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def technology(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/sci-tech')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    return render(request, 'website/technology.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def videos(request):
    return render(request, 'website/videos.html')

def health(request):
    import requests
    import bs4
    res = requests.get('https://www.geo.tv/category/health')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    type(soup)
    # hi=soup.select('.pigeon-item faux-block-link')
    # hi = soup.select('.new_storylising_contentwrap')
    hi = soup.select('.list')
    str1 = str(hi[0])
    str2 = str(hi[1])
    str3 = str(hi[2])
    str4 = str(hi[3])
    str5 = str(hi[4])
    str6 = str(hi[5])
    str7 = str(hi[6])
    str8 = str(hi[7])
    str9 = str(hi[8])
    str10 = str(hi[9])
    str11 = str(hi[11])
    str12 = str(hi[1])
    str13 = str(hi[5])
    str14 = str(hi[10])
    str15 = str(hi[11])
    str16 = str(hi[9])
    str17 = str(hi[4])
    str18 = str(hi[0])
    str19 = str(hi[2])
    str20 = str(hi[8])
    # str2 = str(hi[1])
    print(hi[0])


    return render(request, 'website/health.html',{'hi':str1,'hi2':str2,'hi3':str3,'hi4':str4,
                                                    'hi5':str5,'hi6':str6,'hi7':str7,'hi8':str8,
                                                    'hi9':str9,'hi10':str10,'hi11':str11,'hi12':str12,
                                                    'hi13':str13,'hi14':str14,'hi15':str15,'hi16':str16,
                                                    'hi17':str17,'hi18':str18,'hi19':str19,'hi20':str20})

def shortcodes(request):
    return render(request, 'website/shortcodes.html')

def single(request):
    return render(request, 'website/single.html')
def loginform(request):

    if request.method=='POST':

        # username2 = request.POST['username']
        # password2 = request.POST['password']
        #
        # register1=authenticate(name=username2, password=password2)
        #
        # # p=register.objects.filter(name=username2)
        #  # obj=register.objects.all()
        # # print (username2)
        #
        # if register1 is not None:
        #         auth.login(request, register)
        #         return render(request,'website/base.html')
        # else:
        #     return render(request, 'website/index.html')
        #
        #     messages.error(request,'username did not match ')



        username1=request.POST['usernamesignup']
        email=request.POST['emailsignup']
        password=request.POST['passwordsignup']
        print (username1)
        print (email)
        print (password)
        register.objects.create(name=username1,emailid=email,password=password)
        # reg=register.objects.create_user(name=username1,emailid=email,password=password)
        # reg.save()

        # disply data


        return HttpResponseRedirect('/loginform/')

    else:
        # return render(request, 'website/base.html')
        # obj = register.objects.all()

        return render(request, 'website/loginform.html')


def Admn(request):
    return render(request, 'Admn/index.html')

class UserFormView(View):
    form_class=UserForm
    template_name='website/registration_form.html'

    def get(self, request):
        form= self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})