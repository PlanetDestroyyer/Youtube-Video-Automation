import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient.http import MediaFileUpload



CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                    scope=YOUTUBE_UPLOAD_SCOPE)

    storage = Storage("upload-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))


def upload(file, metadata):
    youtube = get_authenticated_service()

    try:
        insert_request = youtube.videos().insert(
            part="snippet,status",
            body={
              "snippet": {
                "title": metadata["title"],
                "description": metadata["description"],
                "tags": metadata["tags"],
              },
              "status": {
                "privacyStatus": "public"
              }
            },
            media_body=MediaFileUpload(file)
        )
        response = insert_request.execute()
        return response
    except TabError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return None


if __name__ == "__main__":
    pass
    # video_file = "The case of the missing masterpiece.mp4"
    # metadata = {
    #     "title": "The case of the missing masterpiece",
    #     "description": "#shorts #Story #Adventure #Mystery #random #stories #newworld #askreddit #newask #ask more",
    #     "tags": ["shorts","random","stories","new","askreddit","stories","randomstoires"],
    #     "status": "public",  
    # }

    # upload(video_file, metadata)