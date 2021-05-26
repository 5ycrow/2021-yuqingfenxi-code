import random

import networkx as nx
import json
import matplotlib.pyplot as plt

G = nx.Graph()
# dictNode = list(G.nodes)
# dictEdges = list(G.edges)
# print(dictNode)
# print(dictEdges)
with open('../static/export.json', 'r', encoding='utf-8') as f:
    jojoDict = json.load(f)
    jojoRole = jojoDict["data"]["nodes"]
    jojoEdges = jojoDict["data"]["edges"]
jojoRoleIds = [i["id"] for i in jojoRole]
# print(jojoRole)
roleFormatter = []
edgeFormatter = []
roleNetworkxFormatter = []
edgeNetworkxFormatter = []
for role in jojoRole:
    # print(role)
    roleNetworkxFormatter.append(role["id"])
    # roleFormatter.append({"name": role["label"]})
for edge in jojoEdges:
    source = int(edge["from"])
    target = int(edge["to"])
    real_source = jojoRoleIds.index(source)
    real_target = jojoRoleIds.index(target)
    edgeNetworkxFormatter.append((source,target))
    edgeFormatter.append(
        {"source": real_source, "target": real_target, "relation": edge["label"], "value": 5 * random.random()})
# response = network_serializer(roleFormatter, edgeFormatter)
# return response
G.add_nodes_from(roleNetworkxFormatter)
G.add_edges_from(edgeNetworkxFormatter)
degree = nx.degree_histogram(G)
x = range(len(degree))
# y是频率，非频次
y = [z/float(sum(degree))for z in degree]
plt.plot(x,y,color='blue',linewidth=2)
plt.savefig('../static/degree.png')
# plt.show()
# print(nx.degree_histogram(G))
# HITS,前面的值是Hub的值，后面的authorities
# print(nx.hits(G))
# print(roleNetworkxFormatter)
# print(edgeNetworkxFormatter)
dictHits = nx.hits(G)
# nx.draw(G,node_size = 30)
plt.show()
for role in jojoRole:
    # print(role["id"])
    Hub = dictHits[0][role["id"]]
    Auth = dictHits[1][role["id"]]
    # print(Hub,Auth)
    roleFormatter.append({"name": role["label"],"intro":"Hub:"+str(Hub)+" Auth:"+str(Auth)})
# return render_template("Network.html", nodes=roleFormatter, edges=edgeFormatter,nodesNet=roleNetworkxFormatter,edgeNet=edgeNetworkxFormatter)