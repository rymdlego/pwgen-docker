# Simple password generator image

Just a super simple Flask application for generating decent passwords.

## Usage
The app will expose a webserver on port 5000 and display a password (ie. FunkyTiger.2336) when you access the root, but it also exposes a simple API for retrieving passwords in JSON format:

`/api/v1/passwords`

For multiple passwords you can use something like:

`/api/v1/passwords?count=10`
