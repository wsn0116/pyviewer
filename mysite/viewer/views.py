import datetime
import os
import shutil

from viewer.utils import get_name, get_path

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('list')

@login_required
def list(request):
    path = get_path("images/")
    files = os.listdir(path)
    rows = []
    for file in files:
        rows.insert(0, {'file' : file, 'name' : get_name(file)})
    context = {
        'rows': rows,
    }
    return render(request, "viewer/list.html", context)

@login_required
def detail(request):
    try:
        date = request.GET['date']
        sort = 'desc'
        with open(get_path("logs/") + "webui-user-" + date.replace("-", "") + ".txt", "r") as f:
            logs = f.readlines()
        is_exists_log = True
    except:
        sort = 'asc'
        is_exists_log = False
    rows = []
    path = get_path("images/") + date
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            rows.insert(0, {'date': date, 'file': file, 'date_file': date + '/' + file})
    dt = datetime.datetime.now()
    is_available_remove_log = (dt.strftime("%Y-%m-%d") != date)
    context = {
        'rows': rows if sort == 'desc' else reversed(rows),
        'is_exists_log': is_exists_log,
        'logs': logs[-6:] if is_exists_log else [],
        'date': date,
        "is_available_remove_log": is_available_remove_log
    }
    return render(request, "viewer/detail.html", context)

@login_required
def trash(request):
    rows = []
    path = get_path("trashes")
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            rows.insert(0, file)
    context = {
        'files': rows
    }
    return render(request, "viewer/trash.html", context)

@login_required
def move_to_trash(request):
    try:
        date = request.POST['date']
        file = request.POST['file']
        shutil.move(get_path("images/") + date + "/" + file, get_path("trashes"))
    except Exception as e:
        is_already_exists = ("already exists" in e.args[0])
        context = {
            'date': date,
            'file': file,
            'is_already_exists': is_already_exists
        }
        return render(request, "viewer/move_to_trash.html", context)
    response = redirect('detail')
    response['location'] += '?date=' + date
    return response

@login_required
def remove_image(request):
    try:
        date = request.POST['date']
        file = request.POST['file']
        os.remove(get_path("trashes/") + file)
    except Exception as e:
        return render(request, "viewer/remove_error.html")
    if date == '':
        return redirect('trash')
    response = redirect('detail')
    response['location'] += '?date=' + date
    return response

@login_required
def remove_log(request):
    try:
        date = request.POST['date']
        os.remove(get_path("logs/") + "webui-user-" + date.replace("-", "") + ".txt")
    except Exception as e:
        return render(request, "viewer/remove_error.html")
    response = redirect('detail')
    response['location'] += '?date=' + date
    return response

def logout_view(request):
    logout(request)
    return redirect('/admin/login/?next=/viewer/list')
