# contact form backend package

This is the package in charge of handling the data receive by the contact form 
API.

This repo produces a python package witch can be reuse as part of the infrastructure deployments.

## local development

You need python 3.8 and a virtual env:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
make dev
```
After changes make a new dist release with:

```bash
$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags
```
