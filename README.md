This is a sample websocket server implementation. It is a small test bench for development of a websocket client.

This simple server will accept incoming connections on `ws://localhost:8080` and echo a JSON payload in response. The connection will then be closed.

Note that this does not use secure TLS connection. That's an additional layer of complexity left to the implementor :)

To use:
* Set up and enter a `venv`
    * `python3 -m venv .env`
    * `source ./.env/bin/activate`
* Install the deps
    * `pip install -r requirements.txt`
* Run the server
    * `python3 server.py`

