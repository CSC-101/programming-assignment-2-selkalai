from typing import Optional

import data
import math
from data import Point
from data import Rectangle
from data import Song
from data import Duration


# Write your functions for each part in the space below.

# Part 1
#function def create_rectangle takes 2 parameters of type Point(x,y) and returns a Rectangle
# object that is based on these Points. From the two points, the top-left and bottom-right corners
#must be found by finding the left-most and right-most x values and the highest and lowest y values.
#If the values of either x or y are equal then the rectangle will be abnormal

def create_rectangle(point_one: Point, point_two:Point)->Rectangle:
    min_x = min(point_one.x, point_two.x)
    min_y = min(point_one.y, point_two.y)
    max_x = max(point_one.x, point_two.x)
    max_y = max(point_one.y, point_two.y)
    rect_top_left = Point(min_x, max_y)
    rect_bot_right = Point(max_x, min_y)
    return Rectangle(rect_top_left, rect_bot_right)

# Part 2
#function shorter_duration_than takes 2 parameters of type
# Duration(self, minutes:int, seconds:int) and returns True if the duration first parameter
#is shorter than the second and False if not.

def shorter_duration_than(duration_one:Duration, duration_two:Duration)->bool:
    total_one_sec = duration_one.minutes * 60 + duration_one.seconds
    total_two_sec = duration_two.minutes * 60 + duration_two.seconds
    if total_one_sec < total_two_sec:
        return True
    else:
        return False

# Part 3
#function songs_shorter_than takes 2 parameters: one of type
# list[Song(self, artist: str, title: str, duration:Duration) and the second of
# type Duration(self, minutes:int, seconds:int) that indicates the upper bound of a song's
#length. It returns a list of type list[Song] that has all the songs from the input list
# with a duration less than the 2nd parameter

def songs_shorter_than(song_list:list[Song], upper_bound:Duration)->list[Song]:
    shorter_song_list = []
    upper_bound_secs = upper_bound.minutes * 60 + upper_bound.seconds
    for song in song_list:
        song_secs = song.duration.minutes * 60 + song.duration.seconds
        if song_secs < upper_bound_secs:
            shorter_song_list.append(song)
    return shorter_song_list

# Part 4
#function running_time takes 2 parameters - one of type list[Song] and the other of
# list[int] that acts as a 'playlist' (each number represents the # of a song in the
# playlist). It returns an object of type Duration that is the total running time for the
#playlist. The duration seconds must be below 60 and positive. If a song number is out of
#range then skip it.

def running_time(song_list:list[Song], playlist:list[int])->Duration:
    total_duration_secs = 0
    for song_idx in playlist:
        if 0 <= song_idx < len(song_list):
            song = song_list[song_idx]
            total_duration_secs += song.duration.minutes * 60 + song.duration.seconds
    playlist_minutes = total_duration_secs//60
    playlist_secs = total_duration_secs % 60
    return Duration(playlist_minutes, playlist_secs)

# Part 5
# function validate_route takes 2 parameters: one a list of city links of type
# list[list[str]] and the other with a list of city names representing a route of
# type list[str]. The route should run from teh 1st city in the list to the last
# but passed through each intermediate city in the specified order. The function will
# return True if the route is valid and False otherwise. To be valid the route must
# have a link between the consecutive cities in the list.
# an empty route is valid and a route with oen city is valid

def validate_route(city_links:list[list[str]], route_list:list[str])->bool:
    link_valid = False
    if len(route_list) < 2:
        return True
    valid_city_links = []
    for link in city_links:
        valid_city_links.append([link[0], link[1]])
        valid_city_links.append([link[1], link[0]])

    for i in range(len(route_list)-1):
        city = route_list[i]
        city_after = route_list[i+1]
        for link in city_links:
            if (link[0] == city and link[1] == city_after):
                link_valid = True
        if link_valid == False:
            return False
    return True

# Part 6
#function longest_repetition takes a single parameter of type list[int]. The function will
# find the longest contiguous repetition and will return the index at which it begins.
#it will return None if no repetition is found(empty list). If there a multiple repetitions
#equal length then it will return the index of the 1st.

def longest_repetition(nums:list[int])->Optional[int]:
    if not nums:
        return None
    longest_len = 1
    current_idx_len = 1
    current_start_idx = 0
    longest_start_idx = 0
    for num in range(len(nums)-1):
        if nums[num] == nums[num + 1]:
            current_idx_len += 1
        else:
            if current_idx_len > longest_len:
                longest_start_idx = current_start_idx
                longest_len = current_idx_len
            current_idx_len = 1
            current_start_idx = num + 1
    if current_idx_len > longest_len:
        longest_start_idx = current_start_idx
        longest_len = current_idx_len
    if longest_len > 1:
        return longest_start_idx
    else:
        return None


