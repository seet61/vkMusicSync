#setup.py
from distutils.core import setup
import py2exe
 
setup(
    console=[{"script":"audio_sync_win.py"}],
    options={"py2exe": {"includes":["os","sys","vk", "logging", "requests","manipulation", "connect", "urllib", "shutil"]}},
)
