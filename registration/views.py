from django.contrib import messages
from django.shortcuts import render, redirect
from registration.models import *
from taxfiling.models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def regis(request,slug1,slug2):
    try:
        reg = RegistrationSubMenu.objects.get(title__slug=slug1,slug=slug2)

    except RegistrationSubMenu.DoesNotExist:
        return redirect('index')
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        pin = request.POST['pin']
        contacts(reg_title = reg,name=name,email=email,mobile=contact,pincode=pin).save()
        messages.success(request,"Hurrey! Thanks For Contacting With us, We will Get Back To You Soon.")
        return redirect(request.get_full_path())
    res = {}
        # return render(request,'pvt-ltd-reg.html')
    res['top'] = SubRegistrationContent.objects.filter(reg_title__slug=slug2)
    res['absm'] = AboutRegistraionSubMenu.objects.filter(reg_title__slug=slug2)
    res['pi'] = PackageIncluded.objects.filter(reg_title__slug=slug2)
    res['mm'] = Memorandum.objects.filter(reg_title__slug=slug2)
    res['dr'] = DocumentRequired.objects.filter(reg_title__slug=slug2)
    res['sn'] = Sainification.objects.filter(reg_title__slug=slug2)
    res['cr'] = CompanyRegisterRequirements.objects.filter(reg_title__slug=slug2)
    res['pr'] = Procedure.objects.filter(reg_title__slug=slug2)
    res['faq'] = FAQ.objects.filter(reg_title__slug=slug2)    
    res['client'] = ourclients.objects.filter(reg_title__slug=slug2)
    res['reg'] = reg
    res["title"] = reg.submenu
    return render(request,'privateltdreg.html',res)

    
    # if type(slug1)==str:
    #     slug1 = slug1.replace('__','/')
    #     try:
    #         slug1 =  Registration.objects.get(title = slug1.replace('_',' ')).id
	# 	except Exception as a:
	# 		return redirect('home')
	# if type(slug2)==str:
	# 	slug2 = slug2.replace('__','/')
	# 	try:
	# 		slug2 =  RegistrationSubMenu.objects.get(submenu = slug2.replace('_',' ')).id
	# 	except Exception as a:
    #         return redirect('home')
    # id = slug2
    # reg = SubRegistrationContent.objects.get(pk=id)
    # return render(request,'privateltdreg.html',{'reg':reg})