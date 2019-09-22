#! /bin/bash

export ROOT_DIR=$(cd "$(dirname "$0")/.."; pwd)

cd ${ROOT_DIR}

rm -rf build csv2txt.egg-info dist
