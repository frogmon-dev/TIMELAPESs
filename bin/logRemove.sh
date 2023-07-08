#!/bin/bash
cd /home/pi/TIMELAPSEs/images
find ./*.jpg -ctime +30 -exec rm -f {} \;
