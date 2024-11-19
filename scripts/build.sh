#!/bin/bash
VERSION=`cat VERSION`
openapi-generator-cli generate -g python-pydantic-v1 -t ./.openapi-template -i https://app.amber.com.au/swagger.json --additional-properties=packageName=amberelectric,projectName=amberelectric,library=urllib3,packageVersion=$VERSION,packageUrl=https://github.com/madpilot/amberelectric.py,mapNumberTo=float
black amberelectric/**/*.py
rm setup.py
