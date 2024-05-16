#!/bin/sh

FOLDER="./local_lib"

pip3.9 -V

if ! [ -d FOLDER ]
then
    rm -rf ${FOLDER}
fi


cloneRepo()
{
    git clone https://github.com/jaraco/path.git ${FOLDER} > path.log
}

cloneRepo