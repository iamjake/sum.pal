CC = python3

.PHONY: all

all: sumpal_Bot

sumpal_Bot: sumpal_Bot.py
	$(CC) sumpal_Bot.py
