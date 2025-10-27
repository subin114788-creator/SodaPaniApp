Soda Pani - Basic Kivy app (ready for GitHub Actions cloud build)

This repository contains a minimal Kivy app and a GitHub Actions workflow that will attempt to build an Android APK using buildozer.

How to use:
1. Create a GitHub repository and push this project (main branch).
2. On push to main, GitHub Actions will run and attempt to build the APK.
3. After success, download the APK from Actions → latest run → Artifacts → soda-pani-apk.

Notes:
- First builds may fail due to dependency versions; adjust kivy/cython versions in workflow if needed.
- For more advanced features (database, CSV export), replace main.py with your app code and update buildozer.spec.
