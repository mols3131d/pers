# -*- mode: python ; coding: utf-8 -*-

# import os
# import sys

# site_packages_dir = os.path.join(sys.prefix, "lib", "site-packages")
# sys.path.append("./modules")
# sys.path.append(site_packages_dir)


a = Analysis(  # type: ignore
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=[
        # ("./nicegui", "nicegui"),
    ],
    hiddenimports=["nicegui"],
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
