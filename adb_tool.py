#! /usr/bin/env python
"""
Tool in Python to capture video/screenshots/build installation. Works with python 2.7
"""

import sys
from datetime import datetime
from subprocess import call, check_output

def time_diff(start, finish):
    """Runtime Calculator"""

    print "Run in %s" % (finish - start)


def exit_script():
    time_end = datetime.now()
    time_diff(start_time, time_end)
    exit_script.text_exit = raw_input("Exit?(Y/N): ")
    while True:
        if exit_script.text_exit.lower() not in {'y', 'n', 'quit'}:
            print 'please provide valid selection'
            exit_script.text_exit = raw_input("Exit?(Y/N): ")
            continue
        elif exit_script.text_exit.lower() == 'quit':
            sys.exit(0)
        else:
            break

# ============= START MENU ======================
start_menu = """
================= Welcome========================
Please choose an option below:
0) Install build via USB connection
1) Capture a screenshot
2) Capture a video (Requires 4.4 firmware and up)
-------------------------------------------------
Type 'quit' to exit script.
-------------------------------------------------
Connecting to device
"""
kill_server = 'adb kill-server'
start_server = 'adb start-server'
devices = 'adb devices'
print start_menu
call(kill_server)
call(start_server)
call(devices)
# =================================================

# =============== ADB commands aliases ==============================
wake = 'adb shell input keyevent KEYCODE_WAKEUP'
notifications = 'adb shell service call statusbar 1'
start_time = 0
end_time = 0
total_run_time = 0
exit_text = ""
# ====================================================================

while True:
    n = raw_input("Please input your selection: ")
    if n == str(0):
        welcome_text_0 = """
        ========================================================
        === Welcome to the APK Installation Tool V.0.1 =========
        ================ [Install Build via USB] ===============
        ========================================================

        """
        print welcome_text_0
        raw_input("Type package name you wish to work with at prompt."
                  "You can download an Package Reader app from Google"
                  "Play to find out name of the app package."
                  "Press Enter to proceed.")
        app_package = raw_input("Please type in name of the package: ")
        print "Clearing application data. Will skip if app is not found"
        install_check = check_output('adb shell pm list packages | grep %s' % app_package)
        if app_package in install_check:
            clear_data = 'adb shell pm clear %s' % app_package
            call(clear_data)
        else:
            pass
        print "Uninstall existing build. Will skip if app is not found"
        if app_package in install_check:
            uninstall = 'adb shell pm uninstall %s' %app_package
            call(uninstall)
        else:
            pass
        apk_path = raw_input("Please provide full path to APK you wish to install on your computer: ")
        print "APK will now install the build!"
        start_time = datetime.now()
        call(wake)
        install = 'adb install %s' % apk_path
        call(install)
        exit_script()
        if exit_script.text_exit.lower() == 'n':
            continue
        else:
            sys.exit(0)

    elif n == str(1):
        while True:
            screenshot_name = raw_input('Enter screenshot name. It will be amended with timestamp automatically: ')
            screenshot_timestamped = str(screenshot_name) + \
                                     datetime.strftime(datetime.today(), "%Y_%m_%d-%H_%M_%S") + '.png'
            make_screenshot = 'adb shell screencap /sdcard/%s' % screenshot_timestamped
            print "Taking a screenshot, please wait."
            start_time = datetime.now()
            call(make_screenshot)
            print "pulling the file to your folder"
            call('adb pull /sdcard/%s' % screenshot_timestamped)
            exit_script()
            if exit_script.text_exit.lower() == 'n':
                continue
            elif exit_script.text_exit.lower() == 'y':
                break
            else:
                sys.exit(0)
    elif n == str(2):
        while True:
            rec_name = raw_input("If android version < 4.4.4, video can't be recorded. Otherwise please enter name of captured video. It will be timestamped automatically: ")
            rec_name_timestamp = rec_name + datetime.strftime(datetime.today(), '%Y_%m_%d-%H_%M_%S') + '.mp4'
            time_limit = raw_input("Please enter duration of the recording in seconds (Max=180): ")
            print "Capturing video and uploading it to your folder."
            make_video = 'adb shell screenrecord --time-limit %s /sdcard/%s' % (time_limit, rec_name_timestamp)
            start_time = datetime.now()
            print "capturing video..."
            call(make_video)
            print "uploading video..."
            pull_video = 'adb pull /sdcard/%s' % rec_name_timestamp
            call(pull_video)
            exit_script()
            if exit_script.text_exit.lower() == 'n':
                continue
            elif exit_script.text_exit.lower() == 'y':
                break
            else:
                exit(0)
    elif n.lower() == 'quit':
        sys.exit(0)
    else:
        print "Please type in valid selection"

