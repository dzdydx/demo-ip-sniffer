from django.shortcuts import render
from django.http import JsonResponse
from main.models import IPAddr
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def load_index(request):
  itemList = IPAddr.objects.all()
  IPs = []
  for item in itemList:
    IPs.append({
      'ip': item.ip,
      'time': item.visitTime,
      'count': item.visitCount
    })
  context = {
    'itemCount' : len(IPs),
    'itemList' : IPs
  }
  return render(request, 'index.html', context)

@csrf_exempt
def ip_query(request):
  if request.method == "POST":
    IP = request.POST.get('ip')
    if IPAddr.objects.filter(ip=IP).exists():
      count = IPAddr.objects.get(ip=IP).visitCount
      IPAddr.objects.filter(ip=IP).update(visitCount=count+1)
      response = {
        'isRecorded': True,
        'ip': IP,
        'count': count + 1
      }
      return JsonResponse(response)
    else:
      newIP = IPAddr.objects.create(ip=IP)
      response = {
        'isRecorded': False,
        'ip': newIP.ip,
        'time': newIP.visitTime,
        'count': newIP.visitCount
      }
      return JsonResponse(response)
      