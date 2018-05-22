from django.shortcuts import render, redirect
from elasticsearch import Elasticsearch
from django.http import HttpResponse
from datetime import datetime
import simplejson as json
from .models import Course
from datetime import datetime


# to search courses by subcategory, category
def index(request):
    try:
        es = Elasticsearch()

        if request.method == "GET":
            if 'query' not in request.GET:
                params = {}
            else:
                params = {
                    '_source': 'coursename',
                    'suggest': {
                        'title-suggest' : {
                            'prefix' : request.GET['query'],
                            'completion' : { 
                                'field' : 'searchSuggest'
                            }
                        }
                    }
                }
                res = es.search(index='course', body=params)
                responseData = []
                for title in res['suggest']['title-suggest'][0]['options']:
                    tempData = {'id':title['_source']['coursename']}
                    responseData.append(tempData)
                return HttpResponse(json.dumps({'searchData':responseData}))
        else:
            matches = []
            if request.POST['category'] == '':
                pass
            else :
                match = {
                    'match': {
                        'category' : request.POST['category']
                    }
                }
                matches.append(match)
            if request.POST['subcategory'] == '':
                pass
            else :
                match = {
                    'match': {
                        'subcategory' : request.POST['subcategory']
                    }
                }
                matches.append(match)
            params = {
                'query': {
                    'bool' : {
                        'must' : matches
                    }
                }
            }
        res = es.search(index='course', body=params)
        phit = []
        for hit in res['hits']['hits']:
            hits = []
            hits.append(hit['_id'])
            hits.append(hit)
            phit.append(hits)

        context = {'phit': phit}
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return render(request, 'elasticsearch/index.html', context)


# to show create form for a record in elasticsearch
def create(request):
    context = {'request': request}
    return render(request, 'elasticsearch/create.html', context)


# to store a record in elasticsearch
def store(request):
    try:
        suggestions = []
        for word in request.POST['coursename'].split(' '):
            suggestions.append(word)
        # return HttpResponse(json.dumps({'suggestions':suggestions}))
        es = Elasticsearch()
        doc={
            'category': request.POST['category'],
            'subcategory': request.POST['subcategory'],
            'tags': request.POST['tag'],
            'topics': request.POST['topics'],
            'label': request.POST['label'],
            'coursename': request.POST['coursename'],
            'hours': request.POST['hours'],
            'image_url': request.POST['image'],
            'instructor': request.POST['instructor'],
            'offer': request.POST['offer'],
            'price': request.POST['price'],
            'rating_score': request.POST['rating'],
            'students': request.POST['students'],
            'short_description': request.POST['short_description'],
            'difficulty_level': request.POST['difficulty_level'],
            'languages': request.POST['languages'],
            'features': request.POST['features'],
            'course_link': request.POST['course_link'],
            'no_of_lectures': request.POST['lectures'],
            'subtitles': request.POST['subtitles'],
            'no_of_reviews': request.POST['no_of_reviews'],
            'created_at': datetime.now(),
            'searchSuggest' : {
               "input": suggestions,
               # "output": request.POST['coursename']
            }
        }
        # return HttpResponse(json.dumps({'doc':doc}))
        # d_type = (''.join(e for e in request.POST['subcategory'] if e.isalnum())).lower() 
        res = es.index(index='course', doc_type='courses', id=request.POST['id'], body=doc)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return redirect('/api/courses/search')


# to show edit form for a record in elasticsearch
def edit(request, id):
    es = Elasticsearch()
    res = es.search(index='course', doc_type='courses', body={"query": {"match": {"_id": id}}})
    context = {
        'id': res['hits']['hits'][0]['_id'],
        'document' : res['hits']['hits'][0]['_source']
    }
    return render(request, 'elasticsearch/edit.html', context)


# to update a record in elasticsearch
def update(request, id):
    try:
        es = Elasticsearch()
        doc={
            'category': request.POST['category'],
            'subcategory': request.POST['subcategory'],
            'tags': request.POST['tag'],
            'topics': request.POST['topics'],
            'label': request.POST['label'],
            'coursename': request.POST['coursename'],
            'hours': request.POST['hours'],
            'image_url': request.POST['image'],
            'instructor': request.POST['instructor'],
            'offer': request.POST['offer'],
            'price': request.POST['price'],
            'rating_score': request.POST['rating'],
            'students': request.POST['students'],
            'short_description': request.POST['short_description'],
            'difficulty_level': request.POST['difficulty_level'],
            'languages': request.POST['languages'],
            'features': request.POST['features'],
            'course_link': request.POST['course_link'],
            'no_of_lectures': request.POST['lectures'],
            'subtitles': request.POST['subtitles'],
            'no_of_reviews': request.POST['no_of_reviews'],
            'created_at': request.POST['created_at'],
            'updated_at': datetime.now()
        }
        res = es.index(index='course', doc_type='courses', id=id, body=doc)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return redirect('/api/courses/search')


#to delete the record in elasticsearch
def delete(request, id):
    try:
        es = Elasticsearch()
        es.delete(index='course', doc_type='courses', id=id)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return redirect('/api/courses/search')


# To create a new index
def create_index(request, name):
    try:
        es = Elasticsearch()

        # ignore 400 cause by IndexAlreadyExistsException when creating an index
        es.indices.create(index=name, ignore=400)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return HttpResponse('New index created '+name)


# To delete an index
def delete_index(request, name):
    try:
        es = Elasticsearch()

        # ignore 404 and 400
        es.indices.delete(index=name, ignore=[400,404])
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return HttpResponse(name+' index deleted')


# To get mapping
def mapping_get(request, name):
    try:
        es = Elasticsearch()

        phit = es.indices.get_mapping(index=name, doc_type='courses')
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
        
    return HttpResponse(json.dumps({'phit': phit}))


# To put mapping
def mapping_modify(request, name):
    try:
        es = Elasticsearch()

        body = {
            "courses": {
                "properties": {
                    "category": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword", "ignore_above": 256
                            }
                        }
                    },
                    "course_link": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    },
                    "coursename": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "created_at": {
                        "type": "date"
                    }, 
                    "description": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "difficulty_level": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "features": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "hours": {
                        "type": "float"
                    }, 
                    "image": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "image_url": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "instructor": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "instructorHeadline": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "label": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "languages": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "lectures": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "no_of_lectures": {
                        "type": "long"
                    },
                    "no_of_reviews": {
                        "type": "long"
                    }, 
                    "offer": {
                        "type": "float"
                    }, 
                    "price": {
                        "type": "float"
                    },
                    "rating": {
                        "type": "long"
                    }, 
                    "rating_score": {
                        "type": "float"
                    }, 
                    "short_description": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "students": {
                        "type": "long"
                    }, 
                    "subcategory": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "subtitles": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "tag": {
                        "type": "text",
                         "fields": {
                            "keyword": {
                                "type": "keyword",
                                 "ignore_above": 256
                            }
                        }
                    }, 
                    "tags": {
                        "type": "text",
                         "fields": {
                            "keyword": {
                                "type": "keyword",
                                 "ignore_above": 256
                            }
                        }
                    }, 
                    "title": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "topics": {
                        "type": "text", 
                        "fields": {
                            "keyword": {
                                "type": "keyword", 
                                "ignore_above": 256
                            }
                        }
                    }, 
                    "updated_at": {
                        "type": "date"
                    },
                    "searchSuggest": {
                        "type": "completion",
                    },
                }
            }
        }

        phit = es.indices.put_mapping(index=name, doc_type='courses', body=body)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return HttpResponse(json.dumps({'phit': phit}))


# to sync elasticsearch with database
def syncDB(request):
    try:
        for course in Course.objects.all():
            es = Elasticsearch()
            suggestions = []
            for word in course.title.split(' '):
                suggestions.append(word)
            tagname = []
            for tag in course.tags.all():
                tagname.append(tag.name)
            instructors_names = []
            for instructor in course.instructor_id.all():
                instructors_names.append(instructor.user_id.first_name +' '+ instructor.user_id.last_name)

            features = []
            for f in request.POST.getlist('features[]'):
                features.append(f)

            doc={
                'category': course.course_subcategory_id.course_category_id.name,
                'subcategory': course.course_subcategory_id.name,
                'tags': tagname,
                'topics': course.no_lectures,
                'label': 'New',
                'coursename': course.title,
                'hours': course.no_hours,
                'image_url': course.preview_image_url,
                'instructor': instructors_names,
                'offer': course.discount,
                'price': course.price,
                'rating_score': course.ratings,
                'students': course.students_enrolled,
                'short_description': course.description[:200],
                'difficulty_level': course.level,
                'languages': course.course_language_id.name,
                'features': ['Full lifetime access','Access on Mobile and TV'],
                # 'course_link': ''course.id,
                'no_of_lectures': course.no_lectures,
                'subtitles': course.subtitle,
                'no_of_reviews': course.rating_count,
                'created_at': datetime.now(),
                'searchSuggest' : {
                   "input": suggestions,
                   # "output": request.POST['coursename']
                }
            }
            res = es.index(index='course', doc_type='courses', id=course.id, body=doc)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({ 'error': 'An unknown error occured connecting to ElasticSearch', 'error_details': '%s' % e }))
    return HttpResponse(json.dumps({ 'status': '1', 'msg': 'Synced with database' }))