#!/bin/bash
# - By Sheikh Haris Zahid

dateTime () {
    echo $(date '+%D %T')
}

log () {
    echo "[$(dateTime)][$1]: $2"
}

