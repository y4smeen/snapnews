from flask import Flask, render_template, json, url_for
import facebook
import requests, os, json
import httplib, urllib, base64
app = Flask(__name__)

graph = facebook.GraphAPI(access_token='ACCESS_TOKEN',version='2.5')

@app.route("/")
def index():
    my_likes = ["BuzzFeedNews"]
    my_videos = []
    i = 0
    for like in my_likes:
        recentVideos = graph.get_connections(id=like, connection_name='videos')
        while i < 5:
            my_videos.append(recentVideos['data'][i])
            i += 1

    # for key in my_videos[0]:
    #     print key
    print my_videos[0]['source']
    return render_template("index.html", videos=my_videos)

@app.route('/<page_id>')
def page(page_id):
    my_videos=[]
    i=0
    recentVideos = graph.get_connections(id=page_id, connection_name='videos')
    while i < 5:
        my_videos.append(recentVideos['data'][i])
        i += 1
    return render_template("index.html", videos=my_videos)

@app.route('/short/<page_id>')
def short_vid(page_id):
    limit = 3
    my_videos=[]
    i=0
    recentVideos = graph.get_connections(id=page_id, connection_name='videos', fields='thumbnails', limit=limit)
    while i < limit:
        my_videos.append(recentVideos['data'][i])
        i += 1
    # return render_template("index-old1.html", videos=my_videos)
    # return render_template("index-old2.html", videos=my_videos, limit=limit)
    return render_template("index-old2.html", limit=limit, videos=my_videos)

@app.route("/discover")
def discover():
    filename = os.path.join(app.static_folder, 'newsSources-copy.json')
    with open(filename) as File:
        data = json.load(File)
    # j = json.loads("newsSources-copy.json")
    sources = data['sources']
    return render_template("discover.html", sources = sources)

def getUserFeed():
    source_names = []
    userFeed = []
    filename = os.path.join(app.static_folder, 'newsSources-copy.json')
    with open(filename) as blog_file:
        boop = json.load(blog_file)
    # j = json.loads("newsSources-copy.json")
    sources = boop['sources']
    for source in sources:
        source_names.append(source['fbPageName'])

    page_names = []
    user_likes = graph.get_connections(id='me', connection_name='likes')
    for like in user_likes['data']:
        page = graph.get_object(id=like['id'])
        if 'username' in page:
            page_names.append(page['username'])
    print page_names


    # for like in user_likes:
    # print user_likes
    # print [method for method in dir(user_likes) if callable(getattr(user_likes, method))]
        # if like.username in source_names:
        #     userFeed.append(like.username)



    return userFeed

def getVideos():
    my_likes = ["nytimes"]
    my_videos = []
    i = 0
    for like in my_likes:
        # recentVideos = graph.get_connections(id=like, connection_name='videos', fields="")
        recentVideos = graph.get_connections(id=like, connection_name='videos', fields='thumbnails,source,title', limit=3)
        # for key in recentVideos['data'][0]['thumbnails']['data'][0]:
        #     print key
        # for i in range(0,3):
            # for j in range (0,3):
        for key in recentVideos['data'][0]:
            print key

    # print [method for method in dir(graph) if callable(getattr(graph, method))]

    # recentVideos['data'][i]['thumbnails']['data'][j]['uri']

        # my_videos.append(recentVideos['data'][i])
    # print my_videos[0]['embed_html']
        # print recentVideos['data'][i]['thumbnails']['data']['uri']
        # print recentVideos['data'][i]['embed_html']
        # for key in recentVideos['data'][i]:
        #     print key
        # while i < 5:
        #     print recentVideos['data'][i]['embed_html']
        #     i += 1

        # i = 0
        # while i < 2:
        #     my_video_links.append(recentVideos['data'][0]['embed_html'])
        #     i += 1
        # print [method for method in dir(like) if callable(getattr(like, method))]

    # print my_video_links
    # videos = my_video_links
    return my_videos

def getMicrosoftVideo(body):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'MICROSOFT_ACCESS_TOKEN',
    }

    params = urllib.urlencode({
        # Request parameters
        # 'maxMotionThumbnailDurationInSecs': '0',
        'outputAudio': 'true',
        'fadeInFadeOut': 'true',
    })

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/video/v1.0/generatethumbnail?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    # getUserFeed()
    # getVideos()
    # app.run()
    # getNewsSources()
    getMicrosoftVideo("https://scontent.xx.fbcdn.net/v/t43.1792-4/16235289_1198381300269874_465298206884888576_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6ImxlZ2FjeV9oZCJ9&oh=b20431ae5cf00d2df6067a0af26e201b&oe=58B89BEC")
