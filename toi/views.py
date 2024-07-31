from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def home(request):
    try:
        print("inside home view")
        show_section=False
        courses_obj = Course.objects.all().values()[:6]
        context = {
            "courses": list(courses_obj),
            "show_section": show_section,
        }
        return render(request, "toi/index.html", context)
    except Exception as e:
        print(e)


def about(request):
    try:
        print("inside about view")
        return render(request, "toi/about.html")
    except Exception as e:
        print(e)


def contact(request):
    try:
        print("inside contact view")
        return render(request, "toi/contact.html")
    except Exception as e:
        print(e)


def course_single(request):
    try:
        print("inside course_single view")
        return render(request, "toi/course-single.html")
    except Exception as e:
        print(e)


def courses(request):
    try:
        print("inside courses view")
        courses_obj = Course.objects.all().values()
        context ={
            "courses":list(courses_obj)
        }
        for obj in courses_obj:
            print(courses_obj.__dict__)
        return render(request, "toi/courses.html",context)
    except Exception as e:
        print(e)


def notice_single(request):
    try:
        print("inside notice_single view")
        return render(request, "toi/notice-single.html")
    except Exception as e:
        print(e)


def notice(request):
    try:
        print("inside notice view")
        return render(request, "toi/notice.html")
    except Exception as e:
        print(e)


def teacher_single(request):
    try:
        print("inside teacher_single view")
        return render(request, "toi/teacher-single.html")
    except Exception as e:
        print(e)


def teacher(request):
    try:
        print("inside teacher view")
        return render(request, "toi/teacher.html")
    except Exception as e:
        print(e)


def admin_signin(request):
    try:
        print("inside admin_signin view")
        return render(request, "toi/admin_panel.html")
    except Exception as e:
        print(e)


@csrf_exempt
def apply_course(request):
    try:
        print("inside apply_course view")
        if request.method == "POST":
            mobile = request.POST.get("mobile")
            name = request.POST.get("loginName")
            course_id = request.POST.get("courseId")
            email = request.POST.get("email")
            message=''
            status = False
            
            print(f"mobile:{mobile},name:{name},course_id:{course_id},email:{email}")

            if mobile and name  and course_id:
                course = Course.objects.get(id=course_id)

                if Student.objects.filter(enrolled_course=course,full_name=name,mobile=mobile,email=email).exists():
                    message = "You are already registered for this course."
                    status = False

                elif Student.objects.filter(
                    enrolled_course=course,mobile=mobile, email=email
                ).exists():
                    message = "This email or mobile already used."
                    status = False

                else:
                    Student.objects.create(
                        mobile=mobile, full_name=name, enrolled_course=course,email=email
                    )

                    # Set the success message
                    message = "Your registration for the course is successful!"
                    status=True

            else:
                message = "All fields are required."

            print("message:",message)

        # Render the same template with the success or error message
        # return render(
        #     request,
        #     "toi/courses.html",
        #     {
        #         "status": True,
        #         "courses": Course.objects.all(),
        #         "show_footer": False,
        #         "message": message,
        #     },
        # )
        return JsonResponse({"status": status, "message": message,"show_footer": False})
    except Exception as e:
        print(e)
        # return render(
        #         request,
        #         "toi/courses.html",
        #         {
        #             "status": False,
        #             "courses": Course.objects.all(),
        #             "show_footer": False,
        #             "message": message,
        #         },
        #     )
        return JsonResponse(
            {"status": status, "message": message, "show_footer": False}
        )
