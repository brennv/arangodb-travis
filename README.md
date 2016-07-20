# arangodb-travis

Integrating [ArangoDB](https://www.arangodb.com/) with [TravisCI](https://travis-ci.org/)

## Getting started

All `.travis.yml` config files have the same basic structure. Here's an example config for a python app that needs to run tests in concert with ArangoDB. ArangoDB is installed and started in the `before_install` section.

```
language: python

python:
  - "2.7"
  - "3.5"

before_install:
- echo arangodb3 arangodb/password password root | sudo debconf-set-selections  # set username 'root'
- echo arangodb3 arangodb/password_again password root | sudo debconf-set-selections  # set password 'root'
- curl -s -L https://raw.githubusercontent.com/brennv/arangodb-travis/master/setup_arangodb.sh -o setup_arangodb.sh
- chmod +x setup_arangodb.sh
- ./setup_arangodb.sh

install: pip install -r requirements.txt

script: python -m unittest discover tests/
```

## ArangoDB versions

The tags for this repo follow release tags for [ArangoDB](https://github.com/arangodb/arangodb).

Example curl for installer script with version tag:

```
curl -s -L https://raw.githubusercontent.com/brennv/arangodb-travis/v3.0.3/setup_arangodb.sh
```

## Examples

PRs for more examples are welcome to help fill out the `examples/` folder for more use cases.

## Background

For background see https://www.arangodb.com/download/travis-ci/ and [#207](https://github.com/arangodb/arangodb/issues/207)

## Way ahead

Add example for testing across multiple db versions.

Write a chef [travis-cookbook](https://github.com/brennv/travis-cookbooks/tree/add-arangodb/community-cookbooks/arangodb) for general inclusion [here](https://docs.travis-ci.com/user/database-setup/).
