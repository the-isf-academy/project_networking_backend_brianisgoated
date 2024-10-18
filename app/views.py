# views.py

from banjo.urls import route_get, route_post
from .models import Drill
from settings import BASE_URL

@route_post(BASE_URL + 'change_comments', args={'id': int, 'new_comments': str})
def change_comments(args):
    if Drill.objects.filter(id=args['id']).exists():
        change_comments = Drill.objects.get(id=args['id'])
        change_comments.change_comments(args['new_comments'])
        return {'Fortune': change_comments.json_response()}
    else:
        return {'error' : 'no drill exists'}
    
    
@route_post(BASE_URL + 'change_tip', args={'id': int, 'new_tip': str})
def change_tip(args):
    if Drill.objects.filter(id=args['id']).exists():
        change_tip = Drill.objects.get(id=args['id'])
        change_tip.change_tip(args['new_comments'])
        return {'Fortune': change_tip.json_response()}
    else:
        return {'error' : 'no drill exists'}