from django.shortcuts import redirect, render
from .models import School, Course, Application
from .forms import CourseApplicationForm, ApplicationForm
from django.contrib import messages
from django.core.mail import EmailMessage
from students import settings
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'base/index.html')


def about(request):
    return render(request, 'base/about.html')

def course(request):
    courses = Course.objects.all()
    schools = School.objects.all()
    context = {'courses': courses, 'schools': schools}
    return render(request, 'base/courses.html', context)


@login_required(login_url='login')
def apply_for_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.course = course
            application.name = request.user
            application.save()
            # messages.success(request, f"Your Application was successfull!.")

            # return redirect('home')
    else:
        form = ApplicationForm()
    context = {'form': form, 'course': course}
    return render(request, 'base/application.html', context)


def on_success(request):
    template = render_to_string('base/email_template.html', {'name': request.user.username})
    email = EmailMessage(
        'Thank you for choosing to work with us.',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],

    )
    email.fail_silently = False
    email.send()
    #
    # my_course = Course.objects.all()
    # context = {'my_course': my_course}

    return render(request, 'base/success.html')


def search(request):
    q = request.GET.get('query') if request.GET.get('query') is not None else ''
    my_courses = Course.objects.filter(Q(schools__name__icontains=q) |
                                       Q(name__icontains=q)
                                       )
    context = {'my_courses': my_courses, 'q': q}

    return render(request, 'base/search_results.html', context)
