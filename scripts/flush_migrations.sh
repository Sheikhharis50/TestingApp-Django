#!/bin/bash
# - By Sheikh Haris Zahid

source "$(pwd)/scripts/init.sh"

echo "$(log INFO 'INIT FLUSHING')"

find . -path "*/$PROJECT_FOLDER/*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/$PROJECT_FOLDER/*/migrations/*.pyc" -delete

echo "$(log INFO 'DONE FLUSHING')"
