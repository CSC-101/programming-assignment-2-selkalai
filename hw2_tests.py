import data
import hw2
import unittest
from data import Point
from data import Rectangle
from data import Song
from data import Duration


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = Point(2,2)
        point2 = Point(10,10)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        point1 = Point(-4,9)
        point2 = Point(100,0)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(-4, 9), Point(100, 0))
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = Duration(100, 23)
        duration2 = Duration(45, 12)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        duration1 = Duration(100, 12)
        duration2 = Duration(100, 12)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration_than_3(self):
        duration1 = Duration(10, 12)
        duration2 = Duration(100, 12)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(expected, result)

    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = Song("artist 1", "song 1", Duration(3, 18))
        song2 = Song("artist 2", "song 2", Duration(4, 1))
        song3 = Song("artist 3", "song 3", Duration(3, 45))
        list_of_songs = [song1, song2, song3]
        duration = Duration(3, 45)
        result = hw2.songs_shorter_than(list_of_songs, duration)
        expected = [song1]
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        song1 = Song("artist 1", "song 1", Duration(1, 18))
        song2 = Song("artist 2", "song 2", Duration(2, 45))
        song3 = Song("artist 3", "song 3", Duration(0, 0))
        list_of_songs = [song1, song2, song3]
        duration = Duration(3, 45)
        result = hw2.songs_shorter_than(list_of_songs, duration)
        expected = [song1, song2, song3]
        self.assertEqual(expected, result)

    def test_songs_shorter_than_3(self):
        list_of_songs = []
        duration = Duration(3, 45)
        result = hw2.songs_shorter_than(list_of_songs, duration)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        song1 = Song("artist 1", "song 1", Duration(4, 30))
        song2 = Song("artist 2", "song 2", Duration(3, 40))
        song3 = Song("artist 3", "song 3", Duration(3, 29))
        song4 = Song("artist 4", "song 4", Duration(3, 58))
        list_of_songs = [song1, song2, song3, song4]
        int_list = [0, 2, 1, 3, 0]
        result = hw2.running_time(list_of_songs, int_list)
        expected = Duration(20, 7)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        song1 = Song("artist 1", "song 1", Duration(4, 30))
        song2 = Song("artist 2", "song 2", Duration(3, 40))
        song3 = Song("artist 3", "song 3", Duration(3, 29))
        song4 = Song("artist 4", "song 4", Duration(3, 58))
        list_of_songs = [song1, song2, song3, song4]
        int_list = [0, 0, 0, 0, 0]
        result = hw2.running_time(list_of_songs, int_list)
        expected = Duration(22, 30)
        self.assertEqual(expected, result)

    # Part 5
    def test_validate_route_1(self):
        city_link_list = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(city_link_list, route)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        city_link_list = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
        route = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(city_link_list, route)
        expected = False
        self.assertEqual(expected, result)

    def test_validate_route_3(self):
        city_link_list = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
        route = []
        result = hw2.validate_route(city_link_list, route)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_4(self):
        city_link_list = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
        route = ['atascadero']
        result = hw2.validate_route(city_link_list, route)
        expected = True
        self.assertEqual(expected, result)

    # Part 6
    def test_longest_repetition_1(self):
        numbers = []
        result = hw2.longest_repetition(numbers)
        expected = None
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        numbers = [1, 2, 3]
        result = hw2.longest_repetition(numbers)
        expected = None
        self.assertEqual(expected, result)

    def test_longest_repetition_3(self):
        numbers = [1, 2, 2, 2, 3, 3, 3]
        result = hw2.longest_repetition(numbers)
        expected = 1
        self.assertEqual(expected, result)

    def test_longest_repetition_4(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        result = hw2.longest_repetition(numbers)
        expected = 4
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
