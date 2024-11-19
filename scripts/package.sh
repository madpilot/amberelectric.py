#!/bin/bash
rm -rf dist/*
poetry build
python3 -m twine upload dist/*
