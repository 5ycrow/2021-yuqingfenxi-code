from flask import jsonify


def zhihu_list_serializer(zhihu):
    zhihu_list = []
    for zh in zhihu:
        alist = {
            'id': zh.id,
            'topic': zh.topic,
            'imgUrl': zh.imgUrl,
            'contentUrl': zh.contentUrl,
            'hotValue': zh.hotValue,
            'content': zh.content
        }
        zhihu_list.append(alist)
    return jsonify({"zhihu_list": zhihu_list, "status": 1})