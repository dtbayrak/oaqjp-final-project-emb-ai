import json
import requests

# Define a function named emotion_detector that takes a string input
def emotion_detector(text_to_analyze):

    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the emotion detection API with the payload and headers
    response = requests.post(url, json = myobj, headers=header, timeout=(5, 10))

    if response.status_code == 200:
        # Parse the JSON response and convert it into object
        data = json.loads(response.text)

        # Extract emotion prodictions from the response as a dict
        emotion = data["emotionPredictions"][0]["emotion"]

        # Find the most dominant emotion
        dominant = max(emotion, key=emotion.get)

        # Add dominant_emotion to dict
        emotion["dominant_emotion"] = dominant

        return emotion
    else:
        return f'An error occurred with the HTTP status code: {response.status_code}'

if __name__ == "__main__":
    print(emotion_detector("I am so happy I am doing this."))