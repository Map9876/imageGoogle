#!/bin/bash -i
echo '#!/bin/bash
URL=$1

curl -s "$URL" | exiftool -fast -
' > /data/data/com.termux/ok.sh # e命令执行的命令可自定义
chmod +x /data/data/com.termux/ok.sh


echo "alias e='/data/data/com.termux/ok/ok.sh'" >> ~/.bashrc # e可自定义
chmod a+x ~/.bashrc
source ~/.bashrc
