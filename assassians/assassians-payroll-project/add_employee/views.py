from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from add_employee.models import device
import datetime

# Create your views here.
def dashboard(request):
    deviceData = device.objects.all()

    data = {
        'key': deviceData
    }
    return render(request,'dashboard.html',data)

def form(request):
    return render(request,'reg_form.html')

def saveData(request):
    if request.method == "POST":
        id = request.POST.get('Id')
        DeviceType = request.POST.get('DeviceType')
        DeviceVersion = request.POST.get('DeviceVersion')
        DeviceLocation = request.POST.get('DeviceLocation')
        PrimaryGroup = request.POST.get('PrimaryGroup')
        SecondaryGroup = request.POST.get('SecondaryGroup')
        CurrentTime = datetime.datetime.now()   #.strftime('%Y-%M-%D %H:%M:%S')
        en = device(Id=id, DeviceType=DeviceType,
        DeviceVersion=DeviceVersion, DeviceLocation=DeviceLocation, PrimaryGroup=PrimaryGroup, SecondaryGroup=SecondaryGroup,RegistrationTime=CurrentTime)
        en.save()
        print(CurrentTime)
        msg = "Device registerd Successfully"
    return render(request,'reg_form.html',{'msg':msg})

def more(request):
    Id = request.GET['Id']  # getting the id of device that have to show more details
    for data in device.objects.filter(Id=Id):
        Id  = data.Id
        DeviceType = data.DeviceType
        DeviceVersion = data.DeviceVersion
        DeviceLocation = data.DeviceLocation
        PrimaryGroup = data.PrimaryGroup
        SecondaryGroup = data.SecondaryGroup
        RegistrationTime = data.RegistrationTime
        Status = data.Status
        LastContact = data.LastContact   # LastConntact :we have to shift this attribute in DeviceLastUpdate and can access by foreign key

    return render(request,"MoreDetails.html",{'Id':Id,'DeviceType':DeviceType,'DeviceVersion':DeviceVersion,'DeviceLocation':DeviceLocation,'PrimaryGroup':PrimaryGroup,'SecondaryGroup':SecondaryGroup,'LastContact':LastContact,'RegistrationTime':RegistrationTime,'Status':Status})

def edit(request):
    Id = request.GET['Id']
    PrimaryGroup = SecondaryGroup="Not Available"
    for data in device.objects.filter(Id=Id):
        Id = data.Id
        DeviceType = data.DeviceType
        DeviceLocation = data.DeviceLocation
        DeviceVersion = data.DeviceVersion
        PrimaryGroup = data.PrimaryGroup
        SecondaryGroup = data.SecondaryGroup
    msg = "Device record data edited successfully"
    return render(request,"edit.html",{'Id':Id,'DeviceType':DeviceType,'DeviceVersion':DeviceVersion,'DeviceLocation':DeviceLocation,'PrimaryGroup':PrimaryGroup,'SecondaryGroup':SecondaryGroup,'msg':msg})

def RecordEdited(request):
    if request.method =="POST":
        Id = request.POST['Id']
        DeviceType = request.POST['DeviceType']
        DeviceVersion = request.POST['DeviceVersion']
        DeviceLocation = request.POST['DeviceLocation']
        PrimaryGroup = request.POST['PrimaryGroup']
        SecondaryGroup = request.POST['SecondaryGroup']
        device.objects.filter(Id=Id).update(Id=Id,DeviceType=DeviceType,DeviceVersion=DeviceVersion,DeviceLocation=DeviceLocation,PrimaryGroup=PrimaryGroup,SecondaryGroup=SecondaryGroup)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


def delete(request):
    Id = request.GET['Id']
    device.objects.filter(Id=Id).delete()
    return HttpResponseRedirect("show")
