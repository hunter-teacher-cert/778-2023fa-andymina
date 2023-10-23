# demonstration of a speaking program


# please note that most of this code was taken directly from pypi reference website
# reference: https://pypi.org/project/python-espeak/

# pauses added by Edgar
import espeak

espeak.init()
speaker = espeak.Espeak()
speaker.say("Hello world")
x = input("...pause...")		# pauses keeps program from speaking over itself.

speaker.rate = 300
speaker.say("Faster hello world")

x = input("...pause...")		# pauses keep program from exiting before end of speech.
					# that would lead to a segfault.