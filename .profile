# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# chromium os
export PATH=$PATH:$HOME/depot_tools

# cuda
export PATH=$PATH:/usr/local/cuda/bin
export LD_LIBRARY_PATH_64=$LD_LIBRARY_PATH_64:/usr/local/cuda/lib64:/usr/local/cuda/lib

# Android
export PATH=$HOME/android-ndk-r7c:$PATH
export OPENCV_MK_PATH=/home/shio/OpenCV-2.3.1/share/OpenCV/OpenCV.mk

# golang
export GOROOT=$HOME/go
export GOBIN=$GOROOT/bin
export PATH=$PATH:$GOBIN

# mpich2
#export MPI_DIR=$HOME/mpi
#export PATH=$MPI_DIR/bin:$PATH

