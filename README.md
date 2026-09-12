ACC MOZA Automatic Motor Limiter

A small Windows utility that automatically sets the steering rotation limit of a MOZA wheelbase based on the car currently driven in Assetto Corsa Competizione.

The application reads the current car from ACC Shared Memory, looks up the appropriate steering angle, and applies it to the wheelbase through the official MOZA Racing SDK.

This is an unofficial community project. It is not affiliated with, endorsed by, or sponsored by KUNOS Simulazioni or MOZA Racing.

How it works

Assetto Corsa Competizione
        |
        | Shared Memory
        v
     ACCReader
        |
        | car_model
        v
     CAR_LOCKS
        |
        | steering angle
        v
     MOZA SDK
        |
        v
  MOZA wheelbase

For example:

ACC reports: ferrari_296_gt3
CAR_LOCKS:    800
MOZA base:    steering limit set to 800°

The program only changes the setting when the detected car changes.

Requirements

Windows

Assetto Corsa Competizione

A supported MOZA Racing wheelbase

MOZA Pit House / the software required by the MOZA SDK

Python 3

Official MOZA Racing SDK

Python packages listed in requirements.txt

The MOZA SDK is not included in this repository. Download it directly from the official MOZA Racing website:

https://mozaracing.com/pages/sdk

After downloading the SDK, copy the 64-bit MOZA_SDK.dll into:

sdk/MOZA_SDK.dll

Resulting project structure:

ACCMozaAutomaticMotorLimiter/
├── main.py
├── acc_reader.py
├── cars.py
├── moza.py
├── requirements.txt
└── sdk/
    └── MOZA_SDK.dll

The sdk/ contents should remain untracked by Git.

Installation

Clone the repository:

git clone <repository-url>
cd ACCMozaAutomaticMotorLimiter

Create a virtual environment:

python -m venv .venv

Activate it:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Download the official MOZA Racing SDK and place MOZA_SDK.dll in the sdk directory.

Running

Start the application with:

python main.py

The application waits for Assetto Corsa Competizione to start. Once ACC exposes the current car through Shared Memory, the program reads its Kunos car ID and applies the corresponding steering angle.

Example output:

Current car: ferrari_296_gt3
Motor limit angle set to 800°

Car mapping

Steering limits are stored in cars.py:

CAR_LOCKS = {
    "ferrari_296_gt3": 800,
    "bmw_m4_gt3": 516,
    "porsche_992_gt3_r": 800,
}

ACC returns internal car identifiers such as:

ferrari_296_gt3
bmw_m4_gt3
porsche_992_gt3_r

The Shared Memory strings are sanitized before lookup because ACC may return null-padded strings.

Building an executable

PyInstaller can be used to create a standalone executable.

Install it:

pip install pyinstaller

Build:

pyinstaller --onefile --noconsole --add-binary "sdk\MOZA_SDK.dll;sdk" main.py

The executable will be created in:

dist/main.exe

The MOZA SDK DLL is required at build/runtime as configured above. Before distributing a build containing MOZA SDK files, verify that redistribution is permitted by the applicable MOZA SDK terms.

Starting automatically with Windows

A simple way to keep the utility running in the background is to place a shortcut to the built executable in the Windows Startup folder.

Press:

Win + R

and enter:

shell:startup

Create a shortcut to the executable in that directory.

The program can then wait in the background and only act when ACC is running.

Project structure

main.py

Controls the application lifecycle, detects whether ACC is running, reacts to car changes, and connects the ACC reader with the MOZA controller.

acc_reader.py

Reads Assetto Corsa Competizione Shared Memory and exposes the current car ID.

cars.py

Contains the mapping between ACC car IDs and steering rotation limits.

moza.py

Loads the official MOZA SDK DLL and sends the steering limit command to the wheelbase.

Dependencies

The project currently uses:

pyaccsharedmemory

psutil

For development/building:

pyinstaller

MOZA SDK

This repository intentionally does not redistribute the MOZA SDK, its DLLs, headers, documentation, or other proprietary files.

Users must obtain the SDK themselves from MOZA Racing:

https://mozaracing.com/pages/sdk

MOZA, MOZA Racing, and related product names are trademarks of their respective owners.

Assetto Corsa Competizione

Assetto Corsa Competizione and related names are property of KUNOS Simulazioni / their respective rights holders.

This project only reads locally exposed Shared Memory data and does not modify the game.

Disclaimer

Use this software at your own risk.

The project directly changes wheelbase parameters through the MOZA SDK. Always verify the configured steering limits before driving.

The author is not responsible for hardware damage, software issues, loss of settings, or other consequences resulting from use of this project.

License

Choose a license for your own source code before publishing.

For a permissive open-source project, the MIT License is a common choice. Note that your project's license does not grant rights to redistribute third-party software such as the MOZA SDK.

This project's source code is licensed under the MIT License.

The MOZA SDK and all related proprietary files are not part of this repository
and remain subject to MOZA Racing's own terms and licenses.