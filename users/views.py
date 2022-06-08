from email.mime import application
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import Application, Advice, Course
from .models import Profile
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def register_user(request):
    """
    If the request method is POST, then validate the form and save it. 
    If the form is valid, then get the username from the form, 
    create a success message, and redirect to the login page. 
    If the request method is not POST, then create an empty form. 
    Finally, render the register.html template with the form
    
    :param request: The request is an HttpRequest object
    :return: The render() function takes the request object as its first argument, a template name as
    its second argument and a dictionary as its optional third argument. It returns an HttpResponse
    object of the given template rendered with the given context.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f"Welcome '{username}'! Your Account was created successfully. You can now LogIn! ")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    """
    It renders the profile.html template with the context of all the applications and advices.
    
    :param request: The request is an HttpRequest object. It contains metadata about the request, such
    as the client’s IP address, the HTTP method, and the headers
    :return: The user is being returned.
    """
    applications = Application.objects.all()
    adivices = Advice.objects.all()

    context = {'applications': applications, 'advices': adivices}
    return render(request, 'users/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your Account was Updated successfully.")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/edit.html', context)


def pdf_report(request):
    """
    We are creating a function called pdf_report that takes a request as a parameter. 
    
    We are then creating three variables: applications, advices, and profiles. 
    
    We are then creating a variable called template_path and setting it equal to the path of the
    template we want to use. 
    
    We are then creating a variable called context and setting it equal to a dictionary with the keys
    applications, advices, and profiles and the values of the variables we created earlier. 
    
    We are then creating a variable called response and setting it equal to an HttpResponse object with
    the content type of application/pdf. 
    
    We are then setting the Content-Disposition header of the response to filename="student_report.pdf".
    
    
    We are then creating a variable called template and setting it equal to the template we want to use.
    
    
    We are then creating a variable called html and setting it equal to the rendered
    
    :param request: The request object
    :return: The pdf_report function is returning a response object.
    """
    applications = Application.objects.all()
    advices = Advice.objects.all()
    # profiles = Profile.objects.all()
    template_path = 'users/pdf_report.html'
    context = {'applications': applications, 'advices': advices,}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="student_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had an error <pre>' % html % '</pre>')
    return response
