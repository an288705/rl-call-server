from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    response = VoiceResponse()

    if 'TranscriptionText' not in request.form:
      if 'RecordingSid' not in request.form:
        #this is initial http request
        response.say("This is aj's call server. say something")
        response.record(finishOnKey='#',transcribeCallback='https://d77b-35-231-9-78.ngrok.io/answer')
      else:
        #this is what follows after. wait at least 10 seconds
        response.pause(length=10)
    else:
      print(request.form['TranscriptionText'])
      response.say("You said"+request.form['TranscriptionText']+". Now hanging up")

    print(response)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)