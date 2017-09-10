#!/usr/bin/env bash
#
# Copyright (c) 2017 HappinessLab
# Created by Shota Shimazu on 2017/09/08
#

if [ -e ./web-site/ ]; then
    rm -rf ./web-site/
fi

git clone https://hplab.work/HpLab/web-site.git

cd ./web-site/
mv ./dist/ ../
cd ../


if [ -e ./web/ ]; then
    rm -rf ./web/
fi

mv ./dist/ ./web/

echo "Completed!"
