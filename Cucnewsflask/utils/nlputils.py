#coding:utf-8
from snownlp import SnowNLP
from flask import jsonify

def nplutils(text):
    s = SnowNLP(text)
    return jsonify({"sentiments":s.sentiments,"keywords":s.keywords(6),"summary":s.summary(6),"status":1})

# text="（记者 宋佳音 摄影 申皓文）1月13日下午3：30，第三次党代会主席团第二次会议在国重大楼7层会议室举行。廖祥忠同志主持会议。会议听取了各团长对党委、纪委工作报告审议情况的汇报，研究了修改意见；听取了各团长对党费收缴使用管理情况报告审议情况的汇报，研究了修改意见并讨论通过。会议审议通过了党委、纪委工作报告决议（草案）和大会选举办法（草案），并提交各代表团讨论。会议讨论了党委、纪委委员预备人选，确定了候选人建议名单并提交各代表团酝酿。（编辑：阎玺）"
# r=nplutils(text)
# print(r)
