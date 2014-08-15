import csv
from forms import DataInput
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
def importcsv(request):
     if request.method == "POST":
        form = DataInput(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Url/')
     else:
        form = DataInput()
        context = {"form": form}
        return render_to_response("import.html", context,context_instance=RequestContext(request))
        
        
        
        
def csv(request):
    my_csv_list = MyCsvModel.import_data(data = open("my_csv_file_name.csv"))
    return render_to_response("import.html")
