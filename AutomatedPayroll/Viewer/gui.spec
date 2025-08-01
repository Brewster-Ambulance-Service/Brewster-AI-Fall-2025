from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE
import os

# Collect NiceGUI data files
nicegui_datas = collect_data_files('nicegui', include_py_files=True)

# Absolute paths for resources outside current folder
parent_dir = os.path.abspath(os.path.join('.', '..'))

extra_datas = nicegui_datas + [
    (os.path.join(parent_dir, 'BrewsterTwo.png'), '.'),
    (os.path.join(parent_dir, 'Model'), 'Model'),
]

a = Analysis(
    ['gui.py'],
    pathex=[os.path.abspath('.'), parent_dir],
    binaries=[],
    datas=extra_datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tensorflow'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BrewsterPayroll',
    icon='app_icon.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
