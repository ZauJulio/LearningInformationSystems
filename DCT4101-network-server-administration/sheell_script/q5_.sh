#!/bin/bash

croncmd="sh `pwd`/q5_job.sh"
cronjob="* * * * * $croncmd"

( crontab -l | grep -v -F "$croncmd" ; echo "$cronjob" ) | crontab -
