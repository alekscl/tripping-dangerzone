#!/usr/bin/env python
import gdata.youtube
import gdata.youtube.service

youtube_service = gdata.youtube.service.YouTubeService()
playlist = raw_input("Please enter the user ID: ")

url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

video_feed = youtube_service.GetYouTubePlaylistFeed(playlist_url)

print("\nPlaylists for %s\n" % (playlist))

for p in video_feed.entry:
    print p.title.text
