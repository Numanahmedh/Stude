from django.shortcuts import render, redirect
from .models import RequestedNotes, AvailableNotes
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def request_notes(request):
    if request.method == 'POST':
        department_r = request.POST.get('department')
        semester_r = request.POST.get('semester')
        subject_name_r = request.POST.get('subject_name')
        subject_code_r = request.POST.get('subject_code')
        subject_code_r = subject_code_r.lower()
        module_number_r = request.POST.get('module_number')

        notes = RequestedNotes(department=department_r, semester=semester_r, subject_name=subject_name_r,
                               subject_code=subject_code_r, module_number=module_number_r)
        notes.save()

        return redirect('request_notes')
    else:

        objects = RequestedNotes.objects.raw("SELECT p* FROM notes_requestednotes")
        context = {
            'notes': objects,
        }
        print(objects)

        return render(request, 'request_notes.html', context)


@login_required(login_url='login')
def upload_notes(request):
    if request.method == 'POST' and request.FILES:
        department_r = request.POST.get('department')
        semester_r = request.POST.get('semester')
        subject_name_r = request.POST.get('subject_name')
        subject_code_r = request.POST.get('subject_code')
        subject_code_r = subject_code_r.lower()
        module_number_r = request.POST.get('module_number')
        notes_file_r = request.FILES.get('notes_file')

        notes = AvailableNotes(department=department_r, semester=semester_r, subject_name=subject_name_r,
                               subject_code=subject_code_r, module_number=module_number_r, notes_file=notes_file_r)
        notes.save()

        return redirect('available_notes')
    else:
        return render(request, 'upload_notes.html')


@login_required(login_url='login')
def available_notes(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        sql_query = f"SELECT * FROM notes_availablenotes WHERE subject_code='{search_query}'"
        objects = AvailableNotes.objects.raw(sql_query)
        context = {
            'notes': objects,
        }
        print(objects)
        return render(request, 'available_notes.html', context)
    else:
        objects = AvailableNotes.objects.raw("SELECT * FROM notes_availablenotes")
        context = {
            'notes': objects,
        }
        print(objects)
        return render(request, 'available_notes.html', context)
