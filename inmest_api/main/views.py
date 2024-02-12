from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
def say_hello(req):
    return HttpResponse("<h1>Hello World</h1>")

def user_profile(req):
    return JsonResponse(
        {
            "name": 'Tumisang Swabi',
            "email": 'tumisangswabi@gmail.com',
            "phone_number":  "+91-8765432101"
        }
    )

def filter_queries (req, qid):
    queries = {
        
        "id": qid,
        "title": "Born a crime",
        "description": "novel",
        "status": "received",
        "submitted_by": "tumisang",
    
    },
    {
        
        "id": qid,
        "title": "Before i let go",
        "description": "novel",
        "status": "received",
        "submitted_by": "tumisang",
    
    }

    return JsonResponse(queries)


class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama declined Val shots"},
            {"id": 2, "title": "Samson declined Val shots"},
        ] 
    def get(self, request):       
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse({"status": "ok"})