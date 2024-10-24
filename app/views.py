# views.py

from banjo.urls import route_get, route_post
from .models import Drill
from settings import BASE_URL

@route_post(BASE_URL + 'user_comments', args={'id': int, 'new_comments': str})
def user_comments(args):
    if Drill.objects.filter(id=args['id']).exists():
        whole_drill= Drill.objects.get(id=args['id'])
        whole_drill.user_comments(args['new_comments'])
        return {'Fortune': whole_drill.json_response()}
    else:
        return {'error' : 'no drill exists'}
    
    
@route_post(BASE_URL + 'change_tip', args={'id': int, 'new_tip': str})
def change_tip(args):
    if Drill.objects.filter(id=args['id']).exists():
        whole_drill = Drill.objects.get(id=args['id'])
        whole_drill.change_tip(args['new_tip'])
        return {'Fortune': whole_drill.json_response()}
    else:
        return {'error' : 'no drill exists'}
    
@route_post(BASE_URL + 'add_likes', args={'id':int})
def add_likes(args):
    if Drill.objects.filter(id=args['id']).exists():
        liked_drill = Drill.objects.get(id=args['id'])
        liked_drill.add_likes()
        return {'Drill': liked_drill.json_response()}
    else:
        return {'error' : 'no drill exists'}
    
