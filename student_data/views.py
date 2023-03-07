from django.shortcuts import render
from .models import Coursedata, Studentdata
from django.contrib import messages
from django.db.models import Q


def qset(request):
    # data_s = Studentdata.objects.all().values()
    # data_c = Coursedata.objects.all().values()
    # context = {'students': data_s, 'courses': data_c}

    data1 = Studentdata.objects.all().values('sid')
    # Three ways of writing queries to filter both
    # data2 = Studentdata.objects.filter(sid='S001', course_id='C001').values()
    data2 = Studentdata.objects.filter(Q(sid='S001') | Q(course_id='C001')).values()
    data3 = Studentdata.objects.filter(sid='S001').values() | Studentdata.objects.filter(course_id='C001').values()

    # Use select_related with object key and then define the object foreign values
    data4 = Studentdata.objects.filter(Q(name='john') | Q(name='rose')).select_related('course').values_list(
        "sid", "name", "course__course_name").all()
    data5 = Studentdata.objects.filter(name__startswith='r').values()

    context = {'d1': data1, 'd2': data2, 'd3': data3, 'd4': data4, 'd5': data5}
    return context


# Create your views here.
def student_info(request):
    course1 = Coursedata(course_id='C001', course_name='python', duration=30)
    course1.save()
    course1 = Coursedata(course_id='C002', course_name='django', duration=30)
    course1.save()
    Coursedata.objects.update_or_create(course_id='C003', course_name='SQL', duration=20)
    Coursedata.objects.update_or_create(course_id='C004', course_name='JAVA', duration=20)
    course_id = Coursedata.objects.get(course_id='C001')
    student1 = Studentdata(sid='S001', name='john', course=course_id)
    student1.save()
    course_id = Coursedata.objects.get(course_id='C002')
    student2 = Studentdata(sid='S002', name='rose', course=course_id)
    student2.save()

    print('Data added...')
    messages.info(request, 'Course and Student added.')
    fetch1 = Studentdata.objects.get(name='john')
    # Don't need to do a get object of the course.  With the latest django,
    # once you have a primary key, it can automatically bring in the attribute of the foreign key data.
    # Coursedata.objects.get(course_name=fetch1.course)
    fetch_name = fetch1.course.course_name
    m1 = f'The course that John is taking is {fetch_name}'
    print(m1)
    messages.info(request, m1)

    # print('Deleting Rose...')
    # Studentdata.objects.filter(name='rose').delete()
    # messages.info(request, 'Removing Rose')
    #
    # print('Deleting Course 1...')
    # Coursedata.objects.filter(course_id='C001').delete()
    # messages.info(request, 'Removing python course.')

    context = qset(request)
    return render(request, 'student.html', context)
