#!/bin/sh -l

PR_NUMBER=$(echo $GITHUB_REF | awk 'BEGIN { FS = "/" } ; { print $3 }')



python /app/messagesender.py $PR_NUMBER
