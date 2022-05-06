def speak_pig():
    """
	>>> speak_pig()
	'oink'
	"""
    return "oink"

def count_dollar_signs(word):
    """
    >>> count_dollar_signs("hello$my$friend")
    2
    """
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

def speak(animal="dog"):
    """
    >>> speak()
    'woof'
    >>> speak("pig")
    'oink'
    """
    if animal == 'pig':
        return "oink"
    elif animal == 'duck':
        return "quack"
    elif animal == 'cat':
        return "meow"
    elif animal == 'dog':
        return "woof"
    else:
        return "?"