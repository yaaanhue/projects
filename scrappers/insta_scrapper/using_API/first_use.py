#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

username = 'yaaanhue'
password = input()
api = InstagramAPI(username, password)
if (api.login()):
    print("Login succes!")
else:
    print("Can't login!")

'''
api.getProfileData()
result = api.LastJson

pprint.pprint(result['user'])
'''

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

user_id = 1464485965
followers = getTotalFollowers(api, user_id)

mediaID = 1836319163707501078
likers = api.getMediaLikers(mediaID)

likers = api.LastJson
type(likers)

len(followers)

pprint.pprint(followers)