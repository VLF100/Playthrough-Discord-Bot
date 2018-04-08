# Define configuration for the bot

cc = "!" 	# Character used to call the bot

# List that contains lists of three words and one number
	# first word is the command to the bot
	# second word is the argument of the command
	# third word is the role to give to the user
	# the number specifies if the previous roles before that one should be deleted when giving it
		# set to 1 to delete previous roles with 0, or to 0 to keep them
		# recommended use: for linear story use 0 and for non-linear/branching stories when the order of play may change use 1
# Example ["finished", "chapter1", "beginner",0]
	# call with !finished chapter1
	# gives user the role of beginner
	# keeps roles before this one, in this case because it is the first one it does nothing
conf_call_roles = [
	["finished","chapter1","beginner",0],
	["finished","chapter2","intermediate",0],
	["finished","branchA","branch A",1],
	["finished","branchB","branch B",1],
	["finished","chapter3","completed",1]
]

# Set to 1 to activate logs, set to 0 to deactivate them
logs = 1


# Set to 1 to remove all previous roles 
# when the last role of the list is given, set to 0 to still keep them
final_role = 1