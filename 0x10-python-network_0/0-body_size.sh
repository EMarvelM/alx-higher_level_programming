#!/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided as input
URL=$1

# Send a request to the URL using curl and store the response body in a temporary file
RESPONSE_FILE=$(mktemp)
curl -s -o "$RESPONSE_FILE" "$URL"

# Get the size of the response body in bytes
BODY_SIZE=$(stat -c %s "$RESPONSE_FILE")

# Display the size of the response body
echo "$BODY_SIZE"

# Clean up - remove the temporary file
rm "$RESPONSE_FILE"


