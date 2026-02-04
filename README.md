# GoogleFindMyTools

This repository includes some useful tools that reimplement parts of Google's Find My Device Network (now called Find Hub Network). Note that the code of this repo is still very experimental.

### What's possible?
Currently, it is possible to query Find My Device / Find Hub trackers and Android devices, read out their E2EE keys, and decrypt encrypted locations sent from the Find My Device / Find Hub network. You can also send register your own ESP32- or Zephyr-based trackers, as described below.

### How to use

> [!CAUTION]
> Before starting, ensure you have Chrome and Python updated.
> 
> **If Chrome is not up to date, the script will NOT work, guaranteed!**

- Clone this repository: `git clone` or download the ZIP file
- Change into the directory: `cd GoogleFindMyTools`
- Optional: Create venv: `python -m venv venv`
- Optional: Activate venv: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux & macOS)
- Install all required packages: `pip install -r requirements.txt`
- Install the latest version of Google Chrome: https://www.google.com/chrome/
- Start the program by running [main.py](main.py): `python main.py` or `python3 main.py`

### Running with Docker (Recommended for Linux)

This is the easiest way to run the tool, especially if you have issues with Chrome versions. This setup uses **Google Chrome Beta** (v145+) automatically.

**Prerequisites:**
- A Linux system with a graphical desktop environment (X11).
- Docker and Docker Compose installed.

**How to run:**
1.  Run the helper script:
    ```bash
    ./run_docker.sh
    ```
    This script handles X11 forwarding permissions automatically so Chrome can open on your screen.

2.  **Authentication:**
    - A Chrome window will open. Login to your Google account.
    - **Do not close the browser manually** - the script will close it when finished.
    - If you want to cancel, press `q` in the terminal or close the Chrome window.

3.  **Secrets:**
    - The authentication secrets are saved to `Auth/secrets.json` on your host machine.
    - **Pro Tip:** If you only need the `secrets.json`, start the script, login, and when asked to proceed with listing devices, press `q` to exit. You will have your clean `secrets.json` file ready.

### Home Assistant Add-on

This tool can also be run directly as a Home Assistant Add-on.

### Home Assistant Add-on

I have created a dedicated Add-ons repository for Home Assistant.

**Installation:**
1.  Go to **Settings > Add-ons > Add-on Store**.
2.  Click the **3 dots** (top right) > **Repositories**.
3.  Add the URL of my Add-ons repository:
    `https://github.com/Eidolf/hassio-addons`
4.  Install the "Google Find My Tools" add-on.

**Usage:**
1.  Start the add-on.
2.  Click **OPEN WEB UI** to see the desktop environment.
3.  Login to Chrome when prompted.
4.  **Secrets:** The `secrets.json` file will be automatically copied to your HA shares directory: `/share/google_find_my_secrets.json`.


### Authentication

On the first run, an authentication sequence is executed, which requires a computer with access to Google Chrome.

The authentication results are stored in `Auth/secrets.json`. If you intend to run this tool on a headless machine, you can just copy this file to avoid having to use Chrome.

### Known Issues
- "Your encryption data is locked on your device" is shown if you have never set up Find My Device on an Android device. Solution: Login with your Google Account on an Android device, go to Settings > Google > All Services > Find My Device > Find your offline devices > enable "With network in all areas" or "With network in high-traffic areas only". If "Find your offline devices" is not shown in Settings, you will need to download the Find My Device app from Google's Play Store, and pair a real Find My Device tracker with your device to force-enable the Find My Device network.
- No support for trackers using the P-256 curve and 32-Byte advertisements. Regular trackers don't seem to use this curve at all - I can only confirm that it is used with Sony's WH1000XM5 headphones.
- No support for the authentication process on ARM Linux
- If you receive "ssl.SSLCertVerificationError" when running the script, try to follow [this answer](https://stackoverflow.com/a/53310545).
- Please also consider the issues listed in the [README in the ESP32Firmware folder](ESP32Firmware/README.md) if you want to register custom trackers.

### Firmware for custom ESP32-based trackers
If you want to use an ESP32 as a custom Find My Device tracker, you can find the firmware in the folder ESP32Firmware. To register a new tracker, run main.py and press 'r' if you are asked to. Afterward, follow the instructions on-screen.

For more information, check the [README in the ESP32Firmware folder](ESP32Firmware/README.md).

### Firmware for custom Zephyr-based trackers
If you want to use a Zephyr-supported BLE device (e.g. nRF51/52) as a custom Find My Device tracker, you can find the firmware in the folder ZephyrFirmware. To register a new tracker, run main.py and press 'r' if you are asked to. Afterward, follow the instructions on-screen.

For more information, check the [README in the ZephyrFirmware folder](ZephyrFirmware/README.md).

### iOS App
You can also use my [iOS App](https://testflight.apple.com/join/rGqa2mTe) to access your Find My Device trackers on the go.
