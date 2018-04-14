#!/usr/bin/env bash
docker build -t "mo443" .
docker run -it -v ~/git/mo443:/external/mo443 -e "TERM=xterm-256color" --name mo443 mo443