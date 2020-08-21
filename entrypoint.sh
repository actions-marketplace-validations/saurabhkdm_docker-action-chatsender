#!/bin/sh -l

PR_NUMBER=${{github.event.number}


python /app/messagesender.py $PR_NUMBER
