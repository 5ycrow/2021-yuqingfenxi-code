from flask import jsonify

def Jojo_list_serializer(jojo,offset,limit,total):
    jojo_list = []
    for wb in jojo:
        alist = {
            'id': wb.id,
            'bid': wb.bid,
            'user_id': wb.user_id,
            '用户昵称': wb.用户昵称,
            '微博正文': wb.微博正文,
            # 'follower_num': wb.follower_num,
            '头条文章url':wb.头条文章url,
            '发布位置':wb.发布位置,
            '艾特用户':wb.艾特用户,
            '话题': wb.话题,
            '转发数': wb.转发数,
            '评论数': wb.评论数,
            '点赞数': wb.点赞数,
            '发布时间': wb.发布时间,
            '发布工具': wb.发布工具,
            '微博图片url': wb.微博图片url,
            '微博视频url': wb.微博视频url,
            'retweet_id': wb.retweet_id
        }
        jojo_list.append(alist)
    return jsonify({"jojo_list": jojo_list, "status": 1,
                    "offset":offset,"limit":limit,"total":total})