"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    for i in range(len(paragraphs)):
        if select(paragraphs[i]):
            k -= 1
        if k < 0:
            return paragraphs[i]
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!' 
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def about_topic(words):
        processed_words = split(remove_punctuation(lower(words)))
        for w in topic:
            if w in processed_words:
                return True
        return False
    return about_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    typed_length = len(typed_words)
    reference_length = len(reference_words)
    num_correct_words = 0
    if typed_length == 0 or reference_length == 0:
        return 0.0
    for i in range(min(typed_length, reference_length)):
        if typed_words[i] == reference_words[i]:
            num_correct_words += 1
    return round(num_correct_words / typed_length * 100, 2)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        difference = float('inf')
        return_word = ''
        for w in valid_words:
            if diff_function(user_word, w, limit) < difference:
                return_word = w
                difference = diff_function(user_word, w, limit)
        if difference <= limit:
            return return_word
        else:
            return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if start == '':
        return len(goal)
    elif goal == '':
        return len(start)
    elif start[0] != goal[0]:
        if limit == 0:
            return 1
        return shifty_shifts(start[1:], goal[1:], limit - 1) + 1
    else:
        return shifty_shifts(start[1:], goal[1:], limit)
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    

    if limit < 0: 
        # BEGIN
        return 1
        # END

    elif len(start) == 0 or len(goal) == 0: 
        # BEGIN
        return len(start) + len(goal)
        # END

    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)

    else:
        add_diff = meowstake_matches(start,  goal[1:], limit - 1)
        remove_diff = meowstake_matches(start[1:], goal, limit - 1)
        substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1)
        # BEGIN
        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    index = 0
    progress = 0
    while index < min(len(typed), len(prompt)):
        if typed[index] == prompt[index]:
            index += 1
            progress += 1
        else:
            break
    send({'id':id, 'progress':progress / len(prompt)})
    return progress / len(prompt)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    time = []
    for player in times_per_player:
        player_time = []
        for i in range(len(player) - 1):
            player_time.append(player[i+1] - player[i])
        time.append(player_time)
    return game(words, time)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    words = all_words(game)
    time = all_times(game)
    num_player = len(time)
    result = [[] for i in range(num_player)]

    def fastest_index(num_player, word_index, time):
        fast_one = 0
        for i in range(num_player):
            if time[i][word_index] < time[fast_one][word_index]:
                fast_one = i
        return fast_one
    
    for i in range(len(words)):
        result[fastest_index(num_player, i, time)].append(words[i])
    
    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    if limit < 0 :
        return float('inf')
    if len(start) == 0 or len(goal) == 0:
        return len(start) + len(goal)
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + key_distance_diff(start,  goal[1:], limit - 1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit - 1)
        kd = key_distance[start[0], goal[0]]
        substitute_diff = kd + key_distance_diff(start[1:], goal[1:], limit - 1)
        # BEGIN
        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

key_distance_diff = count(key_distance_diff)

# 不会做，没搞懂。。。
def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    diff_function = memo(diff_function)

    if user_word in valid_words:
        return user_word
    else:
        difference = float('inf')
        return_word = ''
        for w in valid_words:
            if diff_function(user_word, w, limit) < difference:
                return_word = w
                difference = diff_function(user_word, w, limit)
        if difference <= limit:
            return return_word
        else:
            return user_word
    # END PROBLEM EC2

    # 大佬的答案
# key_distance_diff = memo(key_distance_diff)
# memo_for_fa = {}
#     idx = tuple([user_word, tuple(valid_words), diff_function, limit])
#     if user_word in valid_words:
#         return user_word
#     if idx in memo_for_fa:
#         return memo_for_fa[idx]
#     else:
#         # print("DEBUG: will is in the valid_words", "will" in valid_words)
#         # print("DEBUG: dist(woll, will) = ", diff_function(user_word, "will", limit))
#         # print("DEBUG: dist(woll, well) = ", diff_function(user_word, "well", limit))
#         words_diff = [diff_function(user_word, w, limit) for w in valid_words]
#         similar_word, similar_diff = min(zip(valid_words, words_diff), key=lambda item: item[1])
#         print("DEBUG:", similar_word)
#         if similar_diff > limit:
#             ret = user_word
#         else:
#             ret = similar_word
#         memo_for_fa[idx] = ret
#         return ret


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)