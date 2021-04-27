from flask import jsonify


def weibo_list_serializer(weibo,offset,limit,total):
    weibo_list = []
    for wb in weibo:
        alist = {
            'id': wb.id,
            'user_id': wb.user_id,
            'content': wb.content,
            'original_pictures': wb.original_pictures,
            'publish_time': wb.publish_time,
            'publish_tool': wb.publish_tool,
            'up_num':wb.up_num,
            'retweet_num':wb.retweet_num,
            'comment_num':wb.comment_num
        }
        weibo_list.append(alist)
    return jsonify({"weibo_list": weibo_list, "status": 1,
                    "offset":offset,"limit":limit,"total":total})

def weibouser_list_serializer(weibouser,offset,limit,total):
    weibouser_list = []
    for wb in weibouser:
        alist = {
            'id': wb.id,
            'nickname': wb.nickname,
            'gender': wb.gender,
            'location': wb.location,
            'birthday': wb.birthday,
            'description': wb.description,
            'verified_reason':wb.verified_reason,
            'education':wb.education,
            'work':wb.work,
            'weibo_num': wb.weibo_num,
            'following': wb.following,
            'followers': wb.followers
        }
        weibouser_list.append(alist)
    return jsonify({"weibouser_list": weibouser_list, "status": 1,
                    "offset":offset,"limit":limit,"total":total})


def weibotopic_list_serializer(weibotopic,offset,limit,total):
    weibotopic_list = []
    for wb in weibotopic:
        alist = {
            'weibo_id': wb.weibo_id,
            'nickname': wb.nickname,
            'gender': wb.gender,
            'location': wb.location,
            'follow_num': wb.follow_num,
            # 'follower_num': wb.follower_num,
            'content':wb.content,
            'publish_time':wb.publish_time,
            'publish_tool':wb.publish_tool,
            'like_num': wb.like_num,
            'retweet_num': wb.retweet_num,
            'comment_num': wb.comment_num,
        }
        weibotopic_list.append(alist)
    return jsonify({"weibotopic_list": weibotopic_list, "status": 1,
                    "offset":offset,"limit":limit,"total":total})