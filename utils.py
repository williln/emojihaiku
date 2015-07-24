from emoji_list import EMOJI_LIST 
import emoji 
import random 


def make_haiku_line(num): 
	""" 
	Returns a string of a specific number of emojis based on the passed-in
	number. 

	>>> make_haiku_line(5)
	:simple_smile: :blush: :sun: :umbrella: :heart:
	"""
	make_line = True 
	line = []

	while make_line:
		syllable = random.choice(EMOJI_LIST)
		line.append(emoji.emojize(syllable, use_aliases=True))
		if len(line) >= num:
			make_line = False  

	for emoticon in line:
		emoji.emojize(emoticon)

	return line