#!/bin/sh
export IMAGE_TAG=20230326-110343
docker run --rm  -v $(pwd)/:/opt epmlsop/lifescience-build:$IMAGE_TAG bash -c "cd /opt/indigo/ && sh download.sh && cd /opt && make html 2>err.txt"

if [ -s "err.txt" ]; then
    echo "::error file=err.txt::Errors while building portal"
    cat err.txt
    exit 1
fi
