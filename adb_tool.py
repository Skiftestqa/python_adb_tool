#! /usr/bin/env python
"""
Tool in Python to capture video/screenshots/build installation. Works with python 2.7
"""

import sys
from datetime import datetime
from subprocess import call


def time_diff(start, finish):
    """Runtime Calculator"""

    print round(finish, 2) - round(start, 2)


#=== ADB commands for convenient system execution ===
app_package = ""
path_to_apk_on_PC = ""
kill_server = 'adb kill-server >nul 2>&1'
start_server = 'adb start-server'
tcpip = 'adb tcpip 5555 >nul 2>&1'
devices = 'adb devices'
wake = 'adb shell input keyevent KEYCODE_WAKEUP >nul 2>&1'
download = 'adb shell am start -a android.intent.action.VIEW -d "http://www.apk20.com/apk/187428/start" >nul 2>&1'
uninstall = 'adb uninstall %s' % app_package
install = 'adb install %s' % path_to_apk_on_PC
notifications = 'adb shell service call statusbar 1 >nul 2>&1'
clear_data = 'adb shell pm clear %s' % app_package
start_time = 0
end_time = 0
total_run_time = 0
exit_text = ""
#====================================================


#=== START MENU ===
start_menu = """
================= Welcome========================
Please choose an option below:
0) Install build via USB connection
1) Capture a screenshot
2) Capture a video (Requires 4.4 firmware and up)
Type 'quit' to exit script.
"""
print start_menu
#=================
while True:
    n = raw_input("Please input your selection: ")
    while n == str(0):
        start_time = datetime.now()
        welcome_text_0 = """
        ========================================================
        === Welcome to the APK Installation Tool V.0.1 =========
        ================ [Install Build] =======================
        ========================================================

        Connecting to device
        """
        print welcome_text_0
        call(kill_server)
        call(start_server)
        call(devices)
        Prompt_app_package = """
        Please enter application package name at prompt
        You can find this info in Settings=>App info=> Your app.
        It should be named like com.example.apk
        """
        print Prompt_app_package
        app_package = raw_input("Please enter application package name: ")
        path_to_apk_on_PC = raw_input("Please enter full path to APK on PC"
                                      "(it should look like'C:\Users\username\Downloads\example.apk'): ")
        print "Clearing application data"
        call(clear_data)
        print "Uninstall any existing build"
        call(uninstall)
        print "APK will now install the build!"
        call(wake)
        call(install)
        end_time = datetime.now()
        time_diff(start_time, end_time)
        raw_input("Type enter to exit")
        sys.exit(0)
    if n.lower() == 'quit':
        sys.exit(0)

    else:
        print "Please type in valid selection"


