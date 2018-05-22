import requests
from django.http import HttpResponse
from django.template import loader
import json

# to get the access tokens with received scope
def get_token(request):
    if 'scope1' in request.GET:
        scope = request.GET['scope']+' '+request.GET['scope1']
    else:
        scope = request.GET['scope']
    base_url = 'https://developer.api.autodesk.com'
    url_authenticate = base_url + '/authentication/v1/authenticate'
    data = {
        'client_id': 'D1e9SGgQ5zDOXQLfXDowCS35wtAN81CA',
        'client_secret': 'Eac52ede2a38f41b',
        'grant_type': 'client_credentials',
        'scope': scope
    }
    r = requests.post(url_authenticate, data=data)
    return HttpResponse(r)

# to create a bucket
def bucket_create(request):
    if request.method == "GET":
        template = loader.get_template('autodesk/create_bucket.html')
        context = {'request' : request}
        return HttpResponse(template.render(context, request))
    else:
        base_url = 'https://developer.api.autodesk.com'
        url_authenticate = base_url + '/oss/v2/buckets'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + request.POST['token'],
        }
        data = json.dumps({
            'bucketKey': request.POST['bucketKey'],
            'policyKey': request.POST['policyKey'],
        })
        r = requests.post(url_authenticate, headers=headers, data=data)
        return HttpResponse(r)

def bucket_check(request):
    base_url = 'https://developer.api.autodesk.com'
    url_authenticate = base_url + '/oss/v2/buckets/'+ request.GET['bucketKey'] +'/details'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(request.GET['token']),
    }
    r = requests.get(url_authenticate, headers=headers)
    return HttpResponse(r)

def bucket_upload(request):
    if request.method == "GET":
        template = loader.get_template('autodesk/bucket_upload.html')
        context = {'request' : request}
        return HttpResponse(template.render(context, request))
    else:
        base_url = 'https://developer.api.autodesk.com'
        url_authenticate = base_url + '/oss/v2/buckets/'+ request.POST['bucketKey'] +'/objects/' +request.POST['objectName']
        headers = {
            'Content-Type': 'application/octet-stream',
            'Authorization': 'Bearer ' + request.POST['token'],
        }

        # with open(request.FILES['modelFile'].temporary_file_path(), 'rb') as f:
        # if not request.FILES['modelFile'].multiple_chunks():
        # file_content = request.FILES['modelFile'].read() 
        with open(request.FILES['modelFile'].temporary_file_path(), 'rb') as myfile:
            file_content = myfile.read()
        files = {'file': file_content}

        r = requests.put(url_authenticate, headers=headers, files=files)
        return HttpResponse(r)

# to convert a file into svf
def convert_file(request):
    if request.method == "GET":
        template = loader.get_template('autodesk/convert_file.html')
        context = {'request' : request}
        return HttpResponse(template.render(context, request))
    else:
        base_url = 'https://developer.api.autodesk.com'
        url_authenticate = base_url + '/modelderivative/v2/designdata/job'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(request.POST['token']),
        }
        data = json.dumps({
            "input": {
                "urn": str(request.POST['urn']),
                 # "compressedUrn": True,
                 # "rootFilename": str(request.POST['filename'])
            },
            "output": {
                # "destination": {
                #     "region": "us"
                # },
                "formats": [{
                    "type": "svf",
                    "views": ["2d","3d"]
                }]
            }
        })
        r = requests.post(url_authenticate, headers=headers, data=data)
        return HttpResponse(r)

#to check the status of converted file
def file_status(request):
    base_url = 'https://developer.api.autodesk.com'
    url_authenticate = base_url + '/modelderivative/v2/designdata/'+request.GET['urn']+'/manifest'
    headers = {
        'Authorization': 'Bearer ' + str(request.GET['token']),
    }
    r = requests.get(url_authenticate, headers=headers)
    return HttpResponse(r)