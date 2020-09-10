# contact-form-manager

API for managing messages from Contact Form in Landing Page

# local dev

Install and config docker, them run:

```bash
docker-compose build
docker-compose run contact-form flask dynamodb
docker-compose up
```

The first 2 command's only the first time. This uses dynamodb-local from aws
for local development. The tables data will be store in `/tmp`.

Open your browser on: http://127.0.0.1:5000/example-form
