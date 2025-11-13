# The Hitchhiker's Guide to History - Android Application

This is an Android version of the CultureCode project, built with Kivy and designed to run on mobile devices.

## Features

- Browse all documented cultures with rich detail pages
- Compare different civilizations side-by-side
- Mobile-optimized interface with touch-friendly controls
- Access to the same cultural data as the desktop and web versions

## Building the Android APK

### Prerequisites

- Linux-based system (Ubuntu, Manjaro, etc.)
- Docker (for buildozer container)
- Python 3.7+

### Installation

1. Install Buildozer:
   ```bash
   pip install buildozer
   ```

2. Navigate to the android_app directory:
   ```bash
   cd android_app
   ```

3. Initialize Buildozer:
   ```bash
   buildozer init
   ```
   (Note: We already have a buildozer.spec file, so this step is optional)

4. Build the APK:
   ```bash
   buildozer android debug
   ```
   
   For a release version:
   ```bash
   buildozer android release
   ```

The APK will be created in the `bin/` directory.

### Alternative: Using Docker

If you encounter issues with the native buildozer installation, you can use Docker:

1. Install Docker if not already installed
2. Run:
   ```bash
   buildozer android docker debug
   ```

## Directory Structure

```
android_app/
├── main.py              # Main Kivy application
├── buildozer.spec       # Buildozer configuration
├── requirements.txt     # Python dependencies
├── assets/              # App assets (images, etc.)
├── splash.png          # App splash screen
├── icon.png            # App icon
└── README.md           # This file
```

## Technical Details

- Built with Kivy for cross-platform compatibility
- Uses RecycleView for efficient list display
- Implements a tabbed interface for different cultural aspects  
- Includes a culture comparison feature
- Optimized for mobile touch interactions

## Deploying to Device

1. Enable USB debugging on your Android device
2. Connect the device to your computer via USB
3. Install ADB tools (Android Debug Bridge)
4. Use the following command to install the APK:
   ```bash
   adb install bin/culturecode-0.1-debug.apk
   ```

## Notes for Developers

- The app is designed to work with local culture data
- For a production version, consider implementing GitHub API access for data updates
- The UI is optimized for portrait mode but can be adjusted for landscape if needed
- Icons and splash screens should be added to the assets directory for a production release