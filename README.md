PyAiml2
===
***v0.8.7***

This repository has been forked from [huntersan9/Py3kAiml](https://github.com/huntersan9/Py3kAiml).
The objective of this fork is to update PyAiml for AIML2.0 compatibility.

Additional notes can be viewed in [DOCS.md](DOCS.md)

- Apr 2016: Starting v0.9 - Updating code to AIML2.0 standards
- Oct 2016: Don't have time to develop on a regular basis. Will be monitoring and improving on a as-needed basis until schedule clears up some more.

Eric Su

## Original README

Updating the code for Python 3.2

Jason Ayres

PyAIML -- The Python AIML Interpreter
author: Cort Stratton (cort@users.sourceforge.net)
web: http://pyaiml.sourceforge.net/

PyAIML is an interpreter for AIML (the Artificial Intelligence Markup
Language), implemented entirely in standard Python.  It strives for
simple, austere, 100% compliance with the AIML 1.0.1 standard, no less
and no more.

This is currently pre-alpha software.  Use at your
own risk!

For information on what's new in this version, see the
CHANGES.txt file.

For information on the state of development, including
the current level of AIML 1.0.1 compliance, see the
SUPPORTED_TAGS.txt file.

Quick & dirty example (assuming you've downloaded the
"standard" AIML set):

	import aiml

	# The Kernel object is the public interface to
	# the AIML interpreter.
	k = aiml.Kernel()

	# Use the 'learn' method to load the contents
	# of an AIML file into the Kernel.
	k.learn("std-startup.xml")

	# Use the 'respond' method to compute the response
	# to a user's input string.  respond() returns
	# the interpreter's response, which in this case
	# we ignore.
	k.respond("load aiml b")

	# Loop forever, reading user input from the command
	# line and printing responses.
	while True: print k.respond(str(input("> ")))
