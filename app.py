from flask import Flask, request,render_template
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "API-KEY"


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def generate_response():
    # Get the input prompt from the request
    prompt = request.form.get("prompt")

    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Return the response as a string
    return response

if __name__ == "__main__":
    app.run(debug=True)
