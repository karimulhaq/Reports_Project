from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reports
from .form import ReportForm
#  here we use it to restrict the user from other pages or views
from django.contrib.auth.decorators import login_required
# Create your views here.

# here we restrict the home page to not access without the user login
@login_required(login_url='users:login')
# this views shows all the reports
def home(request):
    all_reports = Reports.objects.all().order_by('-date')
    return render(request, 'reports/reports.html', {'all_reports':all_reports})

# this view update the report, we show create and update in same template
def update_report(request, pk):
    report= get_object_or_404(Reports, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('reports:home')
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/new_report.html', {'form':form})
# this veiw delete the report
def delete_report(request,pk):
    report = get_object_or_404(Reports, pk=pk)
    if request.method =='POST':
        report.delete()
        return redirect('reports:home')
    return render(request, 'reports/delete_report.html', {'report':report})

# this views is for creating new report
@login_required(login_url='users:login')
def new_report(request):
    if request.method =='POST':
        # here request.files is used for static file like image
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            # save the report with author
            newreport= form.save(commit=False)
            newreport.author = request.user
            newreport.save()
            return redirect("reports:home")
            
    else:
        form = ReportForm
    return render(request,"reports/new_report.html", {'form':form})

def aboutme(request):
    return render(request, 'about.html')