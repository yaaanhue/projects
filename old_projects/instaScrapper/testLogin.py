#!/usr/bin/python3

from InstagramAPI import InstagramAPI
username="yaaanhue"
InstagramAPI = InstagramAPI(username, "1888948**")
InstagramAPI.login()

profile = InstagramAPI.getProfileData()
timeFeed = InstagramAPI.timelineFeed()
lastJason = InstagramAPI.LastJson()
