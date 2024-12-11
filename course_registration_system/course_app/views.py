from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('/add_course/')  # Redirect to the same page to show message
        else:
            messages.warning(request, "Failed to add course. Please check the form.")
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def register_course(request):
    available_courses = Course.objects.all() # Fetch all available courses from the database

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            course = form.cleaned_data['course']

            # if Student.objects.filter(email=email).exists(): # Check if the email already exists in the database
            #     messages.warning(request, "This email is already registered.")
            #     return redirect('/register/')  # Redirect to the same page to show message

            # Create or get the student
            student, created = Student.objects.get_or_create(name=name, email=email)

            # Check if the student is already registered for the selected course
            if course in student.enrolled_courses.all():
                messages.warning(request, "You are already registered for this course.")
            else:
                # Check if the course is not full before allowing registration
                if course.current_enrolled < course.maximum_capacity:
                    student.enrolled_courses.add(course)
                    course.current_enrolled += 1
                    course.save()
                    messages.success(request, "Registration successful!")
                else:
                    messages.warning(request, "This course is already full.")

            return redirect('/register/')  # Redirect to the same page to display the message

    else:
        form = CourseRegistrationForm()

    return render(request, 'register_course.html', {'form': form, 'available_courses': available_courses})
