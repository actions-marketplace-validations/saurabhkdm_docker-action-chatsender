#!/bin/sh -l

pull_number=$(jq --raw-output .pull_request.number "$GITHUB_EVENT_PATH")



python /app/messagesender.py $pull_number
