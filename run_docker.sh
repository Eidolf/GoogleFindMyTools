#!/bin/bash

# Allow X11 connections from local users (simplest way for Docker X11 forwarding)
echo "Allowing local X11 connections..."
xhost +local:docker

# Get the current DISPLAY variable
export DISPLAY=$DISPLAY

echo "Starting GoogleFindMyTools in Docker..."
# Build and run
docker compose run --rm google-find-my-tools

# Fix permissions so the user can edit/read the created secrets
docker compose run --rm --entrypoint chown google-find-my-tools -R $(id -u):$(id -g) /app/Auth

# Optional: Revoke X11 permission after (commented out to avoid breaking other things if user wants)
# xhost -local:docker
