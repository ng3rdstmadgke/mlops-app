import json


def hello(event, context):
    limit = event.get("limit", 100)
    count = event.get("count", 0)
    return {"limit": limit, "count": count + 1}
