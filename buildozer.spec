[app]
title = CheckinHelper
package.name = checkin
package.domain = org.checkin.helper
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1
android.api = 30
android.sdk = 24
android.ndk = 23b
android.arch = armeabi-v7a

# 允许访问网络
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
