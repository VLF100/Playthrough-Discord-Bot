# Define configuration for the bot

cc = "!" 	# Character used to call the bot

# List that contains groups of three words
	# first word is the command to the bot
	# second word is the argument of the command
	# third word is the role to give to the user
# Example ["finished", "chapter1", "beginner"]
	# call with !finished chapter1
	# gives user the role of beginner
conf_call_roles = [
	["finished","chapter1","beginner"],
	["finished","chapter2","intermediate"],
	["finished","chapter3","completed"]
]

# Set to 1 to activate logs, set to 0 to deactivate them
logs = 1

# Set to 1 to remove previous roles, set to 0 to keep them
# Previous roles are defined as the one before that one in the list
rm_prev = 0

# Set to 1 to remove all previous roles 
# when the last role of the list is given, set to 0 to still keep them
final_role = 1
