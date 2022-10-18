from signal import pause
from django.shortcuts import render
from googlesearch import search

query = ''

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)