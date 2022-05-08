from django.shortcuts import render,redirect

from users.models import Student

from .forms import EditProfile, EditProfiledes

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from quiz.models import Quiz
from module.models import Module
from users.models import Student, Module_results, Objective_result, Section_result, Chapter_result, Concept_result
from django.http import JsonResponse

def home(request):
    return render(request,'base.html')




def login(request):
    return render(request,'register-page.html')

@login_required
def profile(request):

    quiz_list=[]
    students = Student.objects.all()
    student = students.filter(owner=request.user)
    mod_name = []
    mod_count = []
    stu = Student.objects.get(owner=request.user)
    
    

    for i in student:
        name = i
        programme_name = i.programme
        modules_list = list(i.programme.modules.all())
        description = programme_name.description
        image = i.image
    
    for q in name.programme.modules.all():
        for quiz in q.quiz_set.all():
                quiz_list.append(quiz)
    
    for mod in name .programme.modules.all():
        mod_name.append(mod)
        mod_count.append(mod.count)
    for i in range(0,1):
        modules = []
        modules_score = []

        for mod in stu.get_modules():
            modules.append(mod)
            modules_score.append( Module_results.objects.get(student=stu,module=mod).score)
    print(modules_score,modules)

    
    return render(request,'profile-page.html',context={'name':name,'programme_name':programme_name,'modules':modules_list,'description':description,'image':image,"quizes":quiz_list, "mod_name":mod_name,"mod_count":mod_count,"Modules_name":modules,"Score":modules_score,"Student":stu})


class StudentlistView(ListView):
    model = Student
    students = Student.objects.all()
    template_name = 'base.html'
    context_object_name = 'students'




@login_required
def editprofile(request):


    if request.method != 'POST':
        p_form = EditProfile(instance=request.user.student)
        d_form = EditProfiledes(instance=request.user.student)

    else:
        p_form = EditProfile(data=request.POST,files= request.FILES,instance=request.user.student)
        d_form = EditProfiledes(data=request.POST, instance=request.user.student)

        if p_form.is_valid() and d_form.is_valid():
            p_form.save()
            d_form.save()
            return redirect('profile')
    return render(request,'editprofile.html',context={'form':p_form,'formd':d_form})



def module_guide(request,module):

    student = Student.objects.get(owner=request.user)
    
    for m in student.get_modules():
        objectives = []
        scores = []
        chapters = []
        sections = []
        obj_result = []
        module = Module.objects.get(title=module)
        for objective in module.objective_set.all():
            objectives.append(objective)
            obj_result.append(objective)
            scores.append(Objective_result.objects.get(student=student,module=module,objective=objective))

            for chapter in objective.chapter_set.all():
                chapters.append(chapter)
                for section in chapter.section_set.all():
                    sections.append(section)

    
        
        

    return render(request,context={"module":module,"Objectives":objectives,"Scores":scores,"Objective_results":obj_result,"Chapters":chapters,"Sections":sections,"Student":student},template_name='module_guide.html')


