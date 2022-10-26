from django.shortcuts import render, redirect
from django.http import Http404
from urllib.parse import unquote
from conferences.models import Conference, Comment
import base64
import hashlib
import json
import codecs

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def get_b64(uri_path):
    raw_url = unquote(uri_path)
    return raw_url.split("/")[-1]

def get_md5(uri_path):
    raw_url = unquote(uri_path)
    return raw_url.split("/")[-2]

def _decode_b64string(b64):
    _decodedBytes = base64.urlsafe_b64decode(b64)
    return str(_decodedBytes, "utf-8")
    
# Create your views here.
def secret_page(request):
    full_path = request.get_full_path()

    md5string = get_md5(full_path)
    input_b64 = get_b64(full_path)

    computed_md5_hash = hashlib.md5(bytes(input_b64, 'utf-8')).hexdigest()
    user_md5_hash = bytes(md5string, 'utf-8').decode('utf-8')
    if user_md5_hash != computed_md5_hash:
        return redirect('https://youtube.com/watch?v=dQw4w9WgXcQ')

    json_obj = _decode_b64string(input_b64)
    if not is_json(json_obj):
        return redirect('https://youtube.com/watch?v=dQw4w9WgXcQ')

    try:
        cse1_conf = Conference.objects.get(id=6)
    except Conference.DoesNotExist:
        raise Http404

    if json_obj:
        comment=json.loads(json_obj)
        #  import pdb; pdb.set_trace()
        try:
            given_name = codecs.encode(comment["name"],'rot_13')
            given_email = codecs.encode(comment["email"],'rot_13')
            given_comment =codecs.encode(comment["comment"],'rot_13')
        except KeyError:
            return redirect('https://youtube.com/watch?v=dQw4w9WgXcQ')

        msg = " -- Congratulations! - Sir Roy" if 'psu.palawan' in given_email else "" 

        new_comment = Comment(conference=cse1_conf, 
                            name=given_name,
                            email=given_email,
                              body=given_comment+msg,
                            active=True)
        new_comment.save()
        return redirect('conf:conference-detail',pk=cse1_conf.id)
    return redirect('https://youtube.com/watch?v=dQw4w9WgXcQ')


   
