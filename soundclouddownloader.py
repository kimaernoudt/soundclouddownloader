# -*- coding: utf-8 -*-
#soundcloud playlistdownloader by kim aernoudt
#get your clientid from observing network when clicking download
#clientid might need renewal after a while

import soundcloud
import requests
import os.path
import string

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') 
    return filename
      
def findplaylist():
    client_id="2t9loNQH90kzJcsFCODdigxfp325aq4z"
    client = soundcloud.Client(client_id=client_id)   
    playlisttitle = raw_input("playlisttitle : ")
    playlistget = client.get('/playlists', q=playlisttitle)
    print "PLAYLIST = ",playlistget[0].id, playlistget[0].title
    playlist = client.get('playlists/' + str(playlistget[0].id))
    print "TRACKLIST = "
    for track in playlist.tracks: print track['title']
    question = raw_input("download all of these ? (y/n)")
    if question == "y":
        save_path = raw_input("directory to save in : ")
        print "dowloading"
        for track in playlist.tracks:
            track_id = str(track['id'])
            trackname = track['title']
            trackname = format_filename(trackname)
            url = "http://api.soundcloud.com/tracks/" + track_id + "/download?client_id=" + client_id
            r = requests.get(url)
            completefilename = str(os.path.join(save_path, trackname + ".mp3"))
            if os.path.exists(completefilename) == True:
                print "file already exists, skipping"
                continue
            else:
                open(completefilename, 'wb').write(r.content)
                print "completed", track['title'], url
    else:
        raise SystemExit(0)
    
    
findplaylist()