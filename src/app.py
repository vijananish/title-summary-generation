"""
This File is used to define the endpoints of flask app and its return
"""
from flask import Flask, request, render_template
from services import stream_lit, title_generation, summary_generation


# create the flask app
app = Flask(__name__)

# what html should be loaded as the home page when the app loads?


@app.route('/')
def home():
    return render_template('index.html', prediction_text="", summary_text="")

# define the logic for reading the inputs from the WEB PAGE,
# running the model, and displaying the prediction


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Takes text as input and generated title and summary of the text
    :return: summary and title
    """
    text_description = request.form.get('description')
    stream_lit_text = stream_lit.generate_stream(text_description)
    title_gen = title_generation.generate_answers(stream_lit_text)
    summary_gen = summary_generation.generate_summary(stream_lit_text)
    if ":" in title_gen:
        title_gen = title_gen.split(":")
        title_gen = title_gen[0]
    return render_template('index.html', title_text=title_gen, summary_text=summary_gen[0]["summary_text"])


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
