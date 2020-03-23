import requests

from flask import Blueprint, render_template, current_app, request, redirect

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@main.route('/Piano', methods=['GET', 'POST'])
def Piano():
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    list_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    videos = []
    #PLyOJ5ZNIl-zBK15LfQpxIeN5czgYpvf8L
    list_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        #'playlistId': request.form.get('query'),
        'playlistId': 'PLyOJ5ZNIl-zBK15LfQpxIeN5czgYpvf8L',
        'part': 'snippet',
        'fields': 'items',
        'maxResults': 9
    }
    r = requests.get(list_url, params=list_params)

    results = r.json()['items']

    list_ids = []
    for result in results:
        list_ids.append(result['snippet']['resourceId']['videoId'])

    video_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        'id': ','.join(list_ids),
        'part': 'snippet, contentDetails',
        'maxResults': 9
    }
    r = requests.get(video_url, params=video_params)

    results = r.json()['items']
    for result in results:

        video_data = {
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={ result["id"] }',
            'thumbnail': result['snippet']['thumbnails']['high']['url'],
            'title': result['snippet']['title'],
        }
        videos.append(video_data)
    videos.reverse()
    return render_template('index.html', videos=videos)

@main.route('/Hiphop', methods=['GET', 'POST'])
def Hiphop():
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    list_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    videos = []
    #PLyOJ5ZNIl-zBK15LfQpxIeN5czgYpvf8L
    list_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        #'playlistId': request.form.get('query'),
        'playlistId': 'PLJp3EuGIUfbIUNqe3Bxj1q4Q4U_4aVp7R',
        'part': 'snippet',
        'fields': 'items',
        'maxResults': 9
    }
    r = requests.get(list_url, params=list_params)

    results = r.json()['items']

    list_ids = []
    for result in results:
        list_ids.append(result['snippet']['resourceId']['videoId'])

    video_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        'id': ','.join(list_ids),
        'part': 'snippet, contentDetails',
        'maxResults': 9
    }
    r = requests.get(video_url, params=video_params)

    results = r.json()['items']
    for result in results:

        video_data = {
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={ result["id"] }',
            'thumbnail': result['snippet']['thumbnails']['high']['url'],
            'title': result['snippet']['title'],
        }
        videos.append(video_data)
    videos.reverse()
    return render_template('index.html', videos=videos)
