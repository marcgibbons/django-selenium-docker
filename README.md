# Example: Django Selenium Tests with Docker


## Requirements
- Docker
- Docker-compose
- VNC Viewer (optional for debugging)

## Installation
`$ docker-compose build`


## Running the tests
1. Start the selenium container:

   `$ docker-compose start selenium`

2. Open VNC Viewer and connect to `localhost:5900`. Password is `secret`

3. Run the tests

    `$ docker-compose run django`
