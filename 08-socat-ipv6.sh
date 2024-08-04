#!/bin/bash

socat TCP6-LISTEN:8888,fork TCP4:127.0.0.1:9000 &
