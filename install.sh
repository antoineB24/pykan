#! /bin/sh 
echo 'welcom in pyforum installer '

git --version 2>&1 >/dev/null # improvement by tripleee
GIT_IS_AVAILABLE=$? 

if [ $GIT_IS_AVAILABLE -eq 0 ]; then
    git clone https://github.com/antoineB24/pyforum.git 
    cd pyforum 
    ./build_pyforum.sh 

else 
    echo "FAIL git is not installed"
    echo "do you want install git ? "
    read choice_git 
    if [ $choice_git -eq "yes" || $choice_git -eq "y" ]; then 
        brew --version 2>&1 >/dev/null 
        BREW_IS_AVAILABLE=$? 
        if [ $BREW_IS_AVAILABLE -eq 0 ]; then
            brew install git 
            ./install.sh
        else 
            echo "FAIL brew  is not installed"
            echo "do you want install brew ? "
            read choice_brew 
            if [ $choice_brew -eq "yes" || $choice_brew -eq "y" ]; then 
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                brew install git 
                ./install.sh 
            fi 

        fi
    fi 
fi 
