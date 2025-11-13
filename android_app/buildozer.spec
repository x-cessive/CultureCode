[app]

# (str) Title of your application
title = Hitchhiker's Guide to History

# (str) Package name
package.name = culturecode

# (str) Package domain (needed for android/ios packaging)
package.domain = org.hitchhikersguide

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3, kivy, pyyaml, pillow, requests, android

# (str) Presplash of the application
presplash.filename = %(source.dir)s/splash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait, sensorPortrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Enable AndroidX (read about this on the internet)
android.enable_androidx = True

# (str) Android arch to use (x86, armeabi-v7a, arm64-v8a, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (int) Override log level (0-3)
android.log_level = 2

# (bool) Disable the default backup rules
android.backup_rules = False

# (str) If you put size in buildozer.spec in format pageA4 (or A4), 
# the application will be scaled to that size.
# android.scalable = False

# (str) Compile the application with Cython
# android.use_cython = False

# (str) Set the Cython language level (only valid if android.use_cython is True)
# android.cython_language_level = 3

# (str) The Android archs to build for, when using the "android" tool.
# This option is only valid when using api >= 23
# android.archs = arm64-v8a, armeabi-v7a

# (str) The name of the main file to execute
# This is set in the template automatically
# main_file = main.py

[build_dir]
# Directory to build into
# build_dir = /tmp/buildozer

# Directory to store APK files
# bin_dir = bin

[app]

# (list) Gradle dependencies to add
# android.gradle_dependencies = 

# (bool) Enable the compilation of the application using Cython
# android.use_cython = False

# (str) Path to the Android NDK
# android.ndk_path = 

# (str) Path to the Android SDK
# android.sdk_path = 

# (str) Path to the Android tools
# android.tools_path = 

# (str) Path to the Android platform tools
# android.platform_tools_path = 

[cython]
# (int) How many cython files to compile in parallel
# parallel_compilation = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = None, 1 = Warning, 2 = Exception)
warn_on_root = 1

# (str) Path to buildozer spec file
# spec_file = buildozer.spec

# (str) Path to buildozer command
# buildozer_path = 

# (str) The path to the Android NDK (overwrite the one from buildozer.spec)
# path_android_ndk = 

# (str) The path to the Android SDK (overwrite the one from buildozer.spec)
# path_android_sdk = 

# (str) The path to the Android tools (overwrite the one from buildozer.spec)
# path_android_tools = 

# (str) The path to the Android platform tools (overwrite the one from buildozer.spec)
# path_android_platform_tools = 