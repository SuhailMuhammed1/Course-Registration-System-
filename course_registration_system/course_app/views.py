from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

def add_course(request):  # function to create a course
    if request.method == 'POST':
        form = CourseForm(request.POST) # to validate form input
        if form.is_valid(): # checks if form is valid
            form.save() # saves form
            messages.success(request, "Course added successfully!") # success message
            return redirect('/add_course/')  # Redirect to the same page to show message
        else:
            messages.warning(request, "Failed to add course. Please check the form.") # warning message
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form}) # passes form to the page


def course_list(request):  # function to fetch and display all courses from db
    courses = Course.objects.all() # fetch course data from db
    return render(request, 'course_list.html', {'courses': courses}) # passes course data to the page

def register_course(request): # function for students course registration form
    available_courses = Course.objects.all() # Fetch all available courses from the database

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST) # to validate form input

        if form.is_valid(): # checks if form is valid
            name = form.cleaned_data['name'] # validates and sanitizes name, email, course 
            email = form.cleaned_data['email']
            course = form.cleaned_data['course']

            # if Student.objects.filter(email=email).exists(): # Check if the email already exists in the database
            #     messages.warning(request, "This email is already registered.")
            #     return redirect('/register/')  # Redirect to the same page to show message

            student, created = Student.objects.get_or_create(name=name, email=email) # check if name and email are already there or create new

            if course in student.enrolled_courses.all(): # Check if the student is already registered for the selected course
                messages.warning(request, "You are already registered for this course.")
            else:
                if course.current_enrolled < course.maximum_capacity: # Check if the course is not full 
                    student.enrolled_courses.add(course)
                    course.current_enrolled += 1
                    course.save()
                    messages.success(request, "Registration successful!") # success message
                else:
                    messages.warning(request, "This course is already full.") # warning message

            return redirect('/register/')  # Redirect to the same page to display the message

    else:
        form = CourseRegistrationForm()

    return render(request, 'register_course.html', {'form': form, 'available_courses': available_courses}) # passes form, available_courses to the page
