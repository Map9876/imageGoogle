echo '#!/bin/bash
URL=$1

curl -s "$URL" | exiftool -fast -
' > /data/data/com.termux/ok.sh
chmod +x /data/data/com.termux/ok.sh


echo 'alias e='/data/data/com.termux/ok/ok.sh'
' > ~/.bashrc
source ~/.bashrc
