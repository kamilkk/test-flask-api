# Time series API test with Docker support 🐳

<!-- Project description -->
This repository aims to show how to create simple Time series API using Python Flask, SQLAlchemy, Pandas and running it using Docker.

## Installation

First you must have [Docker](https://www.docker.com/) installed, then `git clone` the repo.

Run following command to start building images and run containers.

```sh
docker-compose up --build -d
```

Then you have to run `docker ps` to verify running containers and ports.

```sh
PORTS
0.0.0.0:5000->5000/tcp
0.0.0.0:5432->5432/tcp
```

Finally you can check the server in the url `http://localhost:5000/heartbeat`

## Test APIs
....

## Contact

If you want to contact me you can reach me at <kamil.k.kowalski@gmail.com>.

## License

This project uses an [MIT License](https://github.com/kamilkk/test-flask-api/blob/master/LICENSE).
