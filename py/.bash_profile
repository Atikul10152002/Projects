#ALIASES

shopt -s cdspell dotglob nocaseglob nocasematch cdable_vars failglob

alias enableHiddenFiles='defaults write com.apple.finder AppleShowAllFiles YES; killall Finder /System/Library/CoreServices/Finder.app'
alias disableHiddenFiles='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'

alias enableQuitFinder='defaults write com.apple.finder QuitMenuItem -bool YES; killall Finder /System/Library/CoreServices/Finder.app'
alias disableQuitFinder='defaults write com.apple.finder QuitMenuItem -bool NO; killall Finder /System/Library/CoreServices/Finder.app'

alias python='python3'
alias python3='python3'
alias python4='python3'
alias python2='/usr/bin/python'

alias pip3='python3 -m pip'
alias pip4='python3 -m pip'
alias pip='python3 -m pip'
alias pip2='pip2.7'
alias py='python'

alias enableUnknownSources='sudo spctl --master-disable'
alias disableUnknownSources='sudo spctl --master-enable'

#COLORS [\033[32m\]

#export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[34;1m\]\w\[\033[m\]\$ "
#	 atikul	   @	  groot:	~	      $

#NON COLOR
export PS1="\u \[\033[34;1m\]\w\[\033[m\] > "

# 31 – red 
# 32 – green
# 33 – yellow
# 34 – blue
# 35 – magenta
# 36 – cyan
# 37 – white

export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -Fh'

# Setting PATH for Python 2.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
export PATH

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

PATH="/usr/lib:${PATH}"
export PATH

# Your previous /Users/atikul/.bash_profile file was backed up as /Users/atikul/.bash_profile.macports-saved_2018-02-13_at_13:54:21

# MacPorts Installer addition on 2018-02-13_at_13:54:21: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.

# Add Visual Studio Code (code)
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
export PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"

# Add Visual Studio Code (code)
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

# Setting PATH for Python 3.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH

# added by Anaconda3 5.2.0 installer
export PATH="/Users/atikul/anaconda3/bin:$PATH"

# added by Miniconda3 installer
export PATH="/Users/atikul/miniconda3/bin:$PATH"
export PATH="/Users/atikul/.nimble/bin:$PATH"