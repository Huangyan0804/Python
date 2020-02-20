#!/bin/bash

let i=1
path=/home/howie/Desktop/workcode/Python/Tesseract-ocr/calculator2-images
echo ${path}

cd ${path}
for file in *.png
do
    mv ${file} ${i}.png
    let i=i+1
done
exit 0
