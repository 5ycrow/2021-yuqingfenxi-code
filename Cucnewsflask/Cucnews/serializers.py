from flask import jsonify


def info_serializer(info):
    message = {
        'info': info
    }
    return jsonify({"info": info, "status": 1})

def cucnews_list_serializer(cucnews,offset,limit,total):
    cnews_list = []
    for cnews in cucnews:
        alist = {
            'id': cnews.id,
            'url': cnews.url,
            'title': cnews.title,
            'picurl': cnews.picurl,
            'content': cnews.content
        }
        cnews_list.append(alist)
    return jsonify({"cnewsList": cnews_list, "status": 1,"offset":offset,"limit":limit,"total":total})