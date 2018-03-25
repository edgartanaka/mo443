#!/usr/bin/env bash
docker build -t "mo443" .
docker run -it -v ~/git/mo443:/external/mo443 --name mo443 mo443