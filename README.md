# contact-form-manager

API for managing messages from Contact Form in Landing Page

# local dev

Install and config docker, them run:

```bash
docker-compose build
docker-compose run contact-form ./wait-for-it.sh localstack:4569 -- flask dynamodb create
docker-compose up
```

The first 2 command's only the first time. This uses localstack docker image for local development. The tables data will be store in `/tmp`.

Build the client script, need's at least node 10 installed:

```bash
cd jsclient
yarn install
yarn run prod
```

Open your browser on: http://127.0.0.1:5000/example-form
