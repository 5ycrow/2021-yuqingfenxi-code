from flask import jsonify


def network_serializer(nodelist, edgelist):
    return jsonify({"nodes": nodelist, "edges": edgelist})