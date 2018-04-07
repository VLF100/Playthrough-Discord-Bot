INSTRUCTIONS

	* Set up the token in a environment variable. If you use a unix based system you can just edit the app-env file and use it:
		```bash
		. ./app-env.sh
		```
		* You can also hardcode it into the main.py file in this line
		```python
		client.run("YOUR_TOKEN_HERE")
		```
	* Start it with:
		```python
		python3 main.py
		```

FEATURES

	* Easy way for customization. Just edit the configuration.py file!
	* Log of roles given and to whom. Easily enabled and disabled.



TODO

	If user has already role do nothing
	What happens if role doesnt exist
	Empty arguments or empty command
	Option to disable logs
	Edit configuration dinamically and reload
	Test roles with spaces