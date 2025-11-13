#!/bin/bash

echo "write commit msg"
read message

git add .
git commit -m $message
git push
echo "auto commit and push is successful"
