from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.http import HttpResponse
# from datetime import datetime
import simplejson as json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = {'request': request}
    return render(request, 'elasticsearch/searchform.html', context)


# to search into elasticsearch data by - difficulty_levels, languages, features, title. If order parameters are passed then sorting will be done
@csrf_exempt
def search(request):
    try:
        es = Elasticsearch()

        if request.method == "GET":
            if 'sort' in request.GET:
                sort = request.GET['sort']
            else:
                sort = '_uid'
            if 'order' in request.GET:
                order = request.GET['order']
            else:
                order = 'asc'

            queries = []
            if 'difficulty_level' in request.GET:
                # return HttpResponse(json.dumps({'get':request.GET.getlist('difficulty_level')}))
                for level in request.GET.getlist('difficulty_level'):
                    queries.append(
                        {
                            'query_string': {
                                'default_field': 'difficulty_level',
                                'query': level,
                                'default_operator': 'or'
                            }    
                        }
                    )
            if 'languages' in request.GET:
                for language in request.GET.getlist('languages'):
                    queries.append(
                        {
                            'query_string': {
                                'default_field': 'languages',
                                'query': language,
                                'default_operator': 'or'
                            }    
                        }
                    )
            if 'features' in request.GET:
                for feature in request.GET.getlist('features'):
                    queries.append(
                        {
                            'query_string': {
                                'default_field': 'features',
                                'query': feature,
                                'default_operator': 'or'
                            }    
                        }
                    )
            if 'title' in request.GET:
                queries.append(
                    {
                        'query_string': {
                            'default_field': 'coursename',
                            'query': request.GET['title'],
                            'default_operator': 'or'
                        }    
                    }
                )

            params = {
                'sort': {
                    sort: {
                        'order': order
                    }
                },
                'query': {
                    'bool' : {
                        'must' : queries
                    }
                }
            }

        else:
            params = {
                'query': {
                    'multi_match': {
                        'query': request.POST['query'],
                        'fields': ['category', 'subcategory', 'coursename', 'instructor', 'short_description'],
                        "operator": "and"
                    }
                }
            }
        # return HttpResponse(json.dumps({'params':params}))

        res = es.search(index='course', body=params)
        phit = []
        for hit in res['hits']['hits']:
            hits = list()
            hits.append(hit['_id'])
            hits.append(hit)
            phit.append(hits)

    except ConnectionError:
        return HttpResponse(json.dumps({ 'error': 'Elasticsearch not working' }))

    return HttpResponse(json.dumps({'phit':phit}))
    # context = {'phit': phit}
    # return render(request, 'elasticsearch/searchform.html', context)
