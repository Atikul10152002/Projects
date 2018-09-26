import os

def lauchPadSize( row, col ):
    os.system(
        f"""
        defaults write com.apple.dock springboard-columns -int {col}; 
        defaults write com.apple.dock springboard-rows -int {row}; 
        defaults write com.apple.dock ResetLaunchPad -bool TRUE; 
        killall Dock
        """)

def enableHiddenFiles():
    os.system("""defaults write com.apple.finder AppleShowAllFiles YES
                killall Finder /System/Library/CoreServices/Finder.app""")


def disableHiddenFiles():
    os.system("""defaults write com.apple.finder AppleShowAllFiles NO; 
                killall Finder /System/Library/CoreServices/Finder.app""")


def enableQuitFinder():
    os.system("""
    defaults write com.apple.finder QuitMenuItem -bool YES; killall Finder /System/Library/CoreServices/Finder.app
    """)


def disableQuitFinder():
    os.system("""
    defaults write com.apple.finder QuitMenuItem -bool NO; killall Finder /System/Library/CoreServices/Finder.app
    """)


def enableUnknownSources():
    os.system("""
    sudo spctl --master-disable
    """)


def disableUnknownSources():
    os.system("""
    sudo spctl --master-enable
    """)


