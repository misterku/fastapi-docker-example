#!/usr/bin/env bash

uvicorn main:app --host 0.0.0.0 --port 9875 --reload & uvicorn main:app2 --host 0.0.0.0 --port 9873 --reload 