import PyInstaller.__main__

PyInstaller.__main__.run([
    'dice_roller.py',
    '--onefile',          # Single executable
    '--windowed',         # No console window
    '--icon=dice.ico',    # Optional: Add an icon
    '--name=DiceRoller'   # App name
])