#!/bin/sh -l

python /app/messagesender.py ${{github.event.number}}
