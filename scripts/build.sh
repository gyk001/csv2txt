#! /bin/bash

export ROOT_DIR=$(cd "$(dirname "$0")/.."; pwd)

cd ${ROOT_DIR}

${ROOT_DIR}/scripts/clean.sh

python setup.py sdist
python setup.py bdist_wheel --universal
