# -*- coding: utf-8 -*-
# uCommon.py

import os

from datetime    import datetime, timedelta
from collections import OrderedDict

class COM:
	gSetupFile = 'setup.ini'
	gControlFile = 'control.ini'
	
	gHomeDir   = '/home/pi/TIMELAPSEs/bin/'
	gLogDir    = '/home/pi/TIMELAPSEs/bin/logs/'
	gJsonDir   = '/home/pi/TIMELAPSEs/bin/json/'	
	gImageDir  = '/home/pi/TIMELAPSEs/images/'
	gFontDir   = '/home/pi/TIMELAPSEs/bin/fonts/'
	
	gProcessNM = os.path.abspath( __file__ )

	gYYYY = '0000'
	gMM   = '00'
	gDD   = '00'
	gHH   = '00'
	gNN   = '00'
	gSS   = '00'
	gAPM  = 'AM'
	gII   = '00'
	
	gNEXT_LINE = 64
	
	gstrYMD    = datetime.now().strftime('%Y%m%d')
	gstrYMDHMS = datetime.now().strftime('%Y%m%d%H%M%S')
	gstrDATE   = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	
	gNOW  = datetime.now()
	
	gPORT = '/dev/ttyUSB0'
	#gPORT = '/dev/ttyAMA0'
