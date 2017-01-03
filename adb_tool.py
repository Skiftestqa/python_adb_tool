"""
Tool in Python to capture video/screenshots/build installation
"""

import time


def time_diff(start, finish):
    """Runtime Calculator"""

    round(finish, 2) - round(start, 2)

#=== ADB commands for convenient system execution ===
kill_server = 'adb kill-server >nul 2>&1'
start_server = 'adb start-server'
tcpip = 'adb tcpip 5555 >nul 2>&1'
devices = 'adb devices'
wake = 'adb shell input keyevent 82 >nul 2>&1'
download = 'adb shell am start -a android.intent.action.VIEW -d "http://www.apk20.com/apk/187428/start" >nul 2>&1'
kill_chrome = 'adb -d shell am force-stop com.android.chrome'
notifications = 'adb shell service call statusbar 1 >nul 2>&1'
clear_data = 'adb shell pm clear com.kabam.marvelbattle >nul 2>&1'
start_time = 0
end_time = 0
total_run_time = 0
#====================================================


#=== START MENU ===
start_menu = """
Choose an option:
0) Download & Install build via USB connection
1) Install IP Widget
3) Download Only
4) Install Only
5) Download & Install build
7) Capture a screenshot
8) Capture a video (Requires 4.4 firmware and up)
"""
print start_menu
#=================

n = raw_input()
