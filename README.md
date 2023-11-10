# Playlist-Tempo

A tiny kit of command line tools for getting tempo data for a Spotify playlist.

## Requirements

Python 3.8+
Poetry
A suitable shell environment (Bash/Fish/Zsh/Powershell etc)
A Spotify developer account
(optional) NodeJS 16+ for running the test server

## Running

You'll need a Spotify API key and secret. Currently, passing these in at CLI level is not supported so create environment variables in your local environment as most suitable with the following names:

`SPOTIFY_KEY=xxxxxxxx`
`SPOTIFY_SECRET=yyyyyyy`

Then you'll need to integrate with your system however you like. Building a wheel and then symlinking into userspace is probably the best way. Once in place, the tool exposes 3 basic functions:

`playlist_tempo tempo calculate_tempo`
This takes a Spotify playlist ID and uses it to calculate the average BPM of the contained tracks

`playlist_tempo tempo get-all-tempos`
This takes a Spotify playlist ID and returns all the discrete BPMs of the contained tracks as a list

`playlist_tempo tempo plot-tempos`
This plots the BPMs of a Spotify playlist on a chart

All commands take a single argument `-p` or `--playlist` which is the ID string of a Spotify playlist (you can extract this from the client or web application)

## Development

This is a Poetry application so to set the application up for development, pull down the source and run

`poetry install`

followed by

`poetry shell`

You can invoke the individual application top level exposed commands via the app.py file directly.

Modify the config/env.py file to switch between local and production mode. In local mode, the application can load data from a local serI usually do this using Node json-server - running this command in the fakes folder will stand up a sample Spotify API response on port 3000:

`cd ./fakes && json-server ./data.json`

## Testing

The application contains python-test-watcher; there are several test fixtures and the application will automatically build mocks of the Spotify API response from the fakes folder. Running `ptw` will invoke the test suite
