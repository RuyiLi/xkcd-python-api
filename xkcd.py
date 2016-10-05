import requests
import json

parsable = "month, num, link, year, news, safe_title, transcript, alt, img, title, day"

def get_json(pagenumber):
    """Returns JSON from page number. Usage: get_json(pagenumber)"""
    return json.loads(requests.get("http://xkcd.com/" + str(pagenumber) + "/info.0.json").text)

def get_image_url(pagenumber):
    """Return the image URL of the specified Xkcd comic. Usage: get_image_url(pagenumber)"""
    parsed = get_json(pagenumber)
    return parsed['img']

def get_newest():
    """Return the JSON of the latest Xkcd comic. Usage: get_newest()"""
    parsed = json.loads(requests.get("http://xkcd.com/info.0.json").text)
    return parsed

def get_newest_page_number():
    """Return the page number of the latest Xkcd comic. Usage: get_newest_page_number()"""
    parsed = json.loads(requests.get("http://xkcd.com/info.0.json").text)
    return parsed["num"]

def get_newest_image_url():
    """Return the image URL of the latest Xkcd comic. Usage: get_newest_image_url()"""
    parsed = json.loads(requests.get("http://xkcd.com/info.0.json").text)
    return parsed["img"]

def parse_newest(parsefor):
    """Return a JSON object with the specified object name of the latest Xkcd comic. Usage: parse_newest(obj)"""
    parsed = json.loads(requests.get("http://xkcd.com/info.0.json").text)
    return parsed[parsefor]

def parse_comic(pagenumber, parsefor):
    """Return a JSON object with the specified object name of the specified Xkcd comic. Usage: parse_comic(pagenumber, obj)"""
    parsed = get_json(pagenumber)
    return parsed[parsefor]
