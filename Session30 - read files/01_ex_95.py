'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(original, copy):
    with open(original) as file:
        reading = file.read()
    with open(copy, "a") as file:
        file.write(reading)

copy('copy/story.txt', 'copy/story_copy.txt')                

'''udemy
Here's my solution:

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)
'''