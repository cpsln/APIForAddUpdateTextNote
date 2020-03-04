
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import UrbanstopNotetext

from datetime import datetime
import json


@csrf_exempt
def add_note(request):
    if request.method == "POST":
        try:
            data = request.body
            user_data = json.loads(data)

            user_notes = UrbanstopNotetext(
                UserName = user_data["UserName"],
                TextNote = user_data["TextNote"]
            )

            user_notes.save()
            
            return JsonResponse({"status":True, "message":"User name and Text note are added"})

        except Exception as e:
            return JsonResponse({"status":False, "error":str(e)})

    return JsonResponse({"status":False, "message":"Method is 'POST'"})

@csrf_exempt
def update_note(request):
    if request.method == "PUT":
        try:

            data = request.body
            update_data = json.loads(data)

            notes = UrbanstopNotetext.objects.get(id=update_data["id"])

            notes.TextNote = update_data["TextNote"]
            notes.LastUpdateDate = notes.UpdateDate if notes.UpdateDate else None
            notes.UpdateDate = datetime.now()

            notes.save()
            
            return JsonResponse({"status":True, "message":"Text notes updated"})
        
        except Exception as e:
            return JsonResponse({"status":False, "error":str(e)})

    return JsonResponse({"status":False, "message":"Method is 'PUT'"})

def get_all_note(request):
    if request.method == "GET":

        all_notes = UrbanstopNotetext.objects.all().values()
        
        return JsonResponse({"status":True, "all_Notes":list(all_notes)})

