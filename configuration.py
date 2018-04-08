# Define configuration for the bot

cc = "!" 	# Character used to call the bot

# List that contains lists of three words and one number
	# first word is the command to the bot
	# second word is the argument of the command
	# third word is the role to give to the user
	# the number specifies if the previous roles before that one should be deleted when giving it
		# set to 1 to delete previous roles with 0, or to 0 to keep them
# Example ["finished", "chapter1", "beginner",0]
	# call with !finished chapter1
	# gives user the role of beginner
	# keeps roles before this one, in this case because it is the first one it does nothing
conf_call_roles = [
	["finished","door1","Rose Manor",1],
	["finished","door2","Weeping Manor",1],
	["finished","door3","Pig Iron Manor",1],
	["finished","door4","Misty Manor",1],
	["finished","door5","Fifth Door",1],
	["finished","door6","Sixth Door",1],
	["finished","door7","Seventh Door",1],
	["finished","door8","Final Door",1],
	["finished","all","Fata Morgana",1]
]

# Set to 1 to activate logs, set to 0 to deactivate them
logs = 1


# Set to 1 to remove all previous roles 
# when the last role of the list is given, set to 0 to still keep them
final_role = 1