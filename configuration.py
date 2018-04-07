#Define configuration for the bot

cc = "!" 	#Character used to call the bot

#List that contains groups of three words
	# first word is the command to the bot
	# second word is the argument of the command
	# third word is the role to give to the user
#Example ["finished", "chatper1", "beginner"]
	# call with !finished chapter1
	# gives user the role of beginner
conf_call_roles = [
	["finished","door1","door1"],
	["finished","door2","door2"]
]

#Set to 1 to activate logs, set to 0 to deactivate them
logs = 1