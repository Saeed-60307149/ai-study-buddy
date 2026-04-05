# File(s) here
ENV="../.env"

# Setting envvars here
set -a
source $ENV

# Call gemini-3's REST
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'

# Remove envvars
set +a