# Final project

Emotion Detector is a Flask web application that analyzes customer feedback
using the embedded Watson NLP emotion service supplied by IBM Skills Network.
It reports anger, disgust, fear, joy, sadness, and the dominant emotion.

Run this project inside the Skills Network Theia Lab, because the Watson API
is available only within that environment.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection
python3 -m pylint server.py
python3 server.py
```

Open the application on port 5000. Blank input produces
`Invalid text! Please try again!` after the API returns HTTP 400.
Network failures are reported separately from invalid input.

`emotion_detection.py` preserves the initial raw-response exercise.
`EmotionDetection/` contains the final packaged implementation.
The original `templates/index.html` and `static/mywebscript.js` are retained.

This project extends the IBM course starter under its Apache 2.0 license.
