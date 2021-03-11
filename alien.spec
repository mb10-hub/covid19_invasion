# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['alien.py', 'alien_invasion.py', 'bullet.py', 'button.py', 'game_functions.py', 'game_stats.py', 'scoreboard.py', 'settings.py', 'ship.py'],
             pathex=['/Users/marcobarragan/PycharmProjects/Alien_Invasion'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='alien',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='alien.app',
             icon=None,
             bundle_identifier=None)
