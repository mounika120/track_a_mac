#!/bin/bash

docker build -t track-a-mac .

docker run -it --rm --name track-a-mac -p 8000:8000 track-a-mac --add-host=docker:0.0.0.0