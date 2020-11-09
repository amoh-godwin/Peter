# -*- mode: python -*-

block_cipher = None


a = Analysis(['Peter.py'],
             pathex=['H:\\GitHub\\Peter'],
             binaries=[],
             datas=[("H:\\GitHub\\Peter\\peter.rcc", ".")],
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
          [],
          exclude_binaries=True,
          name='Peter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon="H:\\GitHub\\Peter\\UI\\images\\PeterIcon.ico",
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Peter')
