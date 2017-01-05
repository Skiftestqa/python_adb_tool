#! /usr/bin/env python
"""
Tool in Python to capture video/screenshots/build installation. Works with python 2.7
"""

import sys

from datetime import datetime
from subprocess import call


def time_diff(start, finish):
    """Runtime Calculator"""

    print "Run in %s" % (finish - start)


def exit_script():
    end_time = datetime.now()
    time_diff(start_time, end_time)
    exit_text = raw_input("Exit?(Y/N): ")
    if exit_text.lower() == 'n':
        sys.exit(0)
    else:
        pass

# === START MENU ===
start_menu = """
================= Welcome========================
Please choose an option below:
0) Install build via USB connection
1) Capture a screenshot
2) Capture a video (Requires 4.4 firmware and up)
-------------------------------------------------
Type 'quit' to exit script.
-------------------------------------------------
"""
print start_menu

selection = raw_input("Do you want to proceed?(Y/N): ")
if selection.lower() == 'n' or 'quit':
    sys.exit(0)
elif selection.lower() == 'y':
    pass

# =================

# =============== ADB commands aliases ==============================
kill_server = 'adb kill-server'
start_server = 'adb start-server'
devices = 'adb devices'
wake = 'adb shell input keyevent KEYCODE_WAKEUP'
notifications = 'adb shell service call statusbar 1'
start_time = 0
end_time = 0
total_run_time = 0
exit_text = ""
# ====================================================================


n = raw_input("Please input your selection: ")
if n == str(0):
    start_time = datetime.now()
    welcome_text_0 = """
    ========================================================
    === Welcome to the APK Installation Tool V.0.1 =========
    ================ [Install Build via USB] ===============
    ========================================================

    Connecting to device
    """
    print welcome_text_0
    call(kill_server)
    call(start_server)
    call(devices)
    raw_input("Type package name you wish to work with at prompt."
              "You can download an Package Reader app from Google"
              "Play to find out name of the app package."
              "Press Enter to proceed.")
    app_package = raw_input("Please type in name of the package: ")
    print "Clearing application data"
    if app_package == call('adb shell pm list packages | grep %s' % app_package):
        clear_data = 'adb shell pm clear %s' % app_package
        call(clear_data)
    else:
        pass
    print "Uninstall existing build"
    if app_package == call('adb shell pm list packages | grep %s' % app_package):
        uninstall = 'adb shell pm uninstall %s' %app_package
        call(uninstall)
    else:
        pass
    apk_path = raw_input("Please provide full path to APK you wish to install on your computer: ")
    print "APK will now install the build!"
    call(wake)
    install = 'adb install %s' % apk_path
    call(install)
    exit_script()


elif n == str(1):
    while True:
        screenshot_name = raw_input('Enter screenshot name. It will be amended with timestamp automatically: ')
        screenshot_timestamped = screenshot_name + datetime.strftime(datetime.today(), "%Y_%m_%d-%H_%M_%S") + '.png'
        call('adb shell screencap /sdcard/%s && adb pull /sdcard/%s' % screenshot_timestamped)
        exit_screencap = raw_input("Finished taking screenshots?(Y/N): ")
        if exit_screencap.lower() == 'y':
            break
        else:
            continue
elif n.lower() == 'quit':
    sys.exit(0)
else:
    print "Please type in valid selection"

