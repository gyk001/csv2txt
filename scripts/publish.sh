#! /bin/bash

export ROOT_DIR=$(cd "$(dirname "$0")/.."; pwd)
cd ${ROOT_DIR}

twine upload dist/*