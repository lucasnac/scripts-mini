#!/bin/sh
cat <<EOF
Content-type: video/flv

EOF
exec /usr/local/etc/translate/bin/rtmpdump -q -v -b 60000 -W http://cdn.seeon.tv/jwplayer/player.swf -p http://www.seeon.tv -r `echo $QUERY_STRING|sed "s_\&amp;_\&_g"`
