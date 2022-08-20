def tk(link):
    import requests
    import json

    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "cd6f1ce0bfmsh4ffe71b75bbdd41p14913ejsn9f80ae566bd2",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    return{"video":rest['video'][0],"music":rest['music'][0]}