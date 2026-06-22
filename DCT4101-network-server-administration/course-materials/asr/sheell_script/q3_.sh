#!/bin/bash

get_pid() {
    ps -ef | grep $1 | grep -v grep | awk '{print $2}'
}

pid=$(get_pid $1)

echo "PID: $pid"
