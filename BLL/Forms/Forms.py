import json


def get_all_forms():
    return json.dumps(
        {"forms": [{"id": "hul", "displayName": "tofesHul", "description": "a form to ask premission to hul",
                    "jpeg": "http://files.softicons.com/download/web-icons/free-web-icon-pack-1-by-rockettheme/png/128x128/earth.png"},
                   {"id": "haaracha", "displayName": "tofes haarachat keva", "description": "a form to ask premission to hul",
                    "jpeg": "http://files.softicons.com/download/holidays-icons/desktop-halloween-icons-by-aha-soft/png/128x128/Death.png"}]})
