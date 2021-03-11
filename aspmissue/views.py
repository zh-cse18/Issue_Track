from datetime import datetime
import xlwt
from django.shortcuts import render
from django.http import HttpResponse
from xlwt import easyxf

from aspmissue.models import ModelName, IssueSummary, Software, MajorIssue, IssueAnalysis
start_date = ""
end_date = ""

def index(request):
    context = dict()
    version = []
    if request.method == 'POST':
        search_model = request.POST.get('search_model')
        print(search_model)
        context['model_name'] = search_model
        model = ModelName.objects.filter(modelname__icontains= search_model)

        for x in model:
            model_detail = Software.objects.filter(modelname=x.id).latest('software_full_name')
            version.append(model_detail)

        context['version'] = version

        return render(request, 'aspmissue/dashboard.html', context)

    model = ModelName.objects.filter(isFinished=False).order_by('-id')

    for x in model:

        model_detail = Software.objects.filter(modelname=x.id).latest('software_full_name')
        version.append(model_detail)

    context['version'] = version

    return render(request, 'aspmissue/dashboard.html', context)


def modelDetail(request, id):
    context = dict()
    modeltest = ModelName.objects.get(pk=id)
    issue_detail = MajorIssue.objects.filter(modelname=id).values('issue')
    issue_analysis = IssueAnalysis.objects.filter(model=modeltest)

    issue_summary = IssueSummary.objects.filter(model=modeltest)
    print(issue_summary)


    context['issue_summary'] = issue_summary
    context['issue_detail'] = issue_detail
    context['issue_analysis'] = issue_analysis
    return render(request, 'aspmissue/issue_summary.html', context)

def marketIssue(request):
    context = dict()
    issues = IssueAnalysis.objects.all().order_by('-id')
    context['issues'] = issues
    return render(request, 'aspmissue/market_issue.html', context)


def xcel_view(request, id):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachment; filename=models' + str(datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    date_xf = easyxf(num_format_str='DD/MM/YYYY')
    columns = ['Model Name', 'Software Version', 'Total Issue Number', 'Expected Date By Pm', 'Actual Date By Pm',
               'FeedBack Expected Date', 'FeedBack Actual Date', 'New Issue', 'Re-open Issue', 'closed Issue',
               'supplier_can_not_fixed', 'issue clsoed by pm', 'Is Mp',
               'Delay By', 'Delay PM', 'Delay QC','New version after','Remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = IssueSummary.objects.filter(model=id).values_list('model__modelname',
                                                             'software__software_full_name',
                                                             'total_issue',
                                                             'expected_software_date', 'actual_software_date',
                                                             'feedback_expected_date', 'feedback_actual_date',
                                                             'new_issue', 'reopen_issue', 'closed_issue',
                                                             'supplier_can_not_fixed', 'issue_clsoed_by_pm',
                                                             'is_mp', 'delay', 'delay_by_pm', 'delay_by_qc','diff_two_version','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 3 or col_num == 4 or col_num == 5 or col_num == 6:
                ws.write(row_num, col_num, row[col_num], date_xf)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def weekly_report(request):
    context = dict()
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        issue_summary = IssueSummary.objects.all().filter(feedback_actual_date__gte = start_date ,feedback_actual_date__lte = end_date).order_by('-id')

        print(start_date, end_date)
        context['issue_summary'] = issue_summary

        context['start_date'] = start_date
        context['end_date'] = end_date

        return render(request, 'aspmissue/weekly_report.html', context)

    issue_summary = IssueSummary.objects.all().order_by('-id')

    context['issue_summary'] = issue_summary

    return render(request, 'aspmissue/weekly_report.html', context)


def weekly_report_xcel_view(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachment; filename=new' + str(datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    date_xf = easyxf(num_format_str='DD/MM/YYYY')
    columns = ['Model Name', 'Software Version', 'Total Issue Number', 'Expected Date By Pm', 'Actual Date By Pm',
               'FeedBack Expected Date', 'FeedBack Actual Date', 'New Issue', 'Re-open Issue', 'closed Issue',
               'supplier_can_not_fixed', 'issue clsoed by pm', 'Is Mp',
               'Delay By', 'Delay PM', 'Delay QC', 'Remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = IssueSummary.objects.filter(model=id).values_list('model__modelname',
                                                             'software__software_full_name',
                                                             'total_issue',
                                                             'expected_software_date', 'actual_software_date',
                                                             'feedback_expected_date', 'feedback_actual_date',
                                                             'new_issue', 'reopen_issue', 'closed_issue',
                                                             'supplier_can_not_fixed', 'issue_clsoed_by_pm',
                                                             'is_mp', 'delay', 'delay_by_pm', 'delay_by_qc', 'remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 3 or col_num == 4 or col_num == 5 or col_num == 6:
                ws.write(row_num, col_num, row[col_num], date_xf)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response



