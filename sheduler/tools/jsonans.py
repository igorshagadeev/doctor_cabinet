from django.http import HttpResponse
#import simplejson
import json


def jsonSimpleAns(error = None, info = None):
  ans = {}
  ans['ok'] = True
  ans['error'] = ""
  if error:
    ans['ok'] = False
    ans['error'] = error
  if info:
    if info and type(info) == type(ans):
      ans.update(info)
    else:
      ans['info'] = info
  #json_info = simplejson.dumps(ans)
  json_info = json.dumps(ans)
  return HttpResponse(json_info)

