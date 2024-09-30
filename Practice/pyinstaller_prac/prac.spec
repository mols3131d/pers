# -*- mode: python ; coding: utf-8 -*-

import sys
import sysconfig

venv_site_packages = sysconfig.get_paths()["purelib"]

a = Analysis(  # type: ignore
    ["main_nicegui.py"],
    pathex=[venv_site_packages, "modules"],
    binaries=[],
    datas=[(venv_site_packages+"/nicegui", "nicegui")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)  # type: ignore

exe = EXE(  # type: ignore
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="main",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
