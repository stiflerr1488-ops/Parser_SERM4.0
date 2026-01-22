import sys
from cx_Freeze import setup, Executable

APP_NAME = "PARSER SERM"
APP_VERSION = "1337"
MAIN_SCRIPT = "main.py"
ICON_ICO = "resources/icon.ico"

base = "gui" if sys.platform == "win32" else None


    build_exe_options = {
        'packages': ['os', 'flask', 'numpy'],
        'include_files': [
            ('app', 'app'),
            ('config', 'config'),
            ('resources', 'resources'),
            ('ui', 'ui'),
            ('sysroot.json', 'sysroot.json'),
            ('results', 'results'),
        ],
        'excludes': ['tkinter'],
        'frameworks': ['Cocoa', 'Quartz'],  # Указание фреймворков для macOS
    }
    
    "include_files": [
        ("app", "app"),
        ("config", "config"),
        ("resources", "resources"),
        ("ui", "ui"),
        ("sysroot.json", "sysroot.json"),
        ("results", "results"),
    ],
}

executables = [
    Executable(
        MAIN_SCRIPT,
        base=base,
        target_name=f"{APP_NAME}.exe",
        icon=ICON_ICO,
    )
]

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_NAME,
    options={
        "build_exe": build_exe_options,
    },
    executables=executables,
)
