# Visualizing Wisconsin's Efficiency Gap
visualize_wi_efficiency_gap

The case Gill v.  Whitford is about whether Wisconsin's state legislative districts should be struck down due to extreme partisan gerrymandering.
Key to the case is the how partisan gerrymandering is being measured, the *efficiency gap*.
While reading about the efficiency gap, here [https://www.brennancenter.org/legal-work/whitford-v-gill](https://www.brennancenter.org/legal-work/whitford-v-gill), and elsewhere, I noticed that there were no maps showing what this looks like across the state, and so I have made an effort to display what it looks like for the Assembly districts in the 2016 elections. 

Perhaps there is a reason there are no maps like these for a reason, and if you know one, please let me know.

TODO:

	- DONE: deploy
		- Still need to make smoother transition to webserver, adjusting user names and etc
		- Also need to investigate how to make use of peer authentication to db
	- DONE: simplify dist boundaries for faster load, cut down on load time by factor of ten or so
	- DONE: Before below, need to restructure data load so it is only loaded once and can be
	restyled without undue strain
	- DONE: add drop down for different years
	- add radio button or other selector for SEN and maybe con districts
	- add overall election efficiency gap
	- How many other years to add?
