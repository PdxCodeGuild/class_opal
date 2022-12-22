from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    context = [
        {
            'title': "Heard at the Board Meeting Friday",
            'author': "Suit Tie",
            'date': "December 9, 2022",
            'body': "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment."
        },
        {
            'title': "Heard at the Board Meeting Tuesday",
            'author': "Suit Tie",
            'date': "December 10, 2022",
            'body': "Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring."

        },
        {
            'title': "Doug's Favorite Project Goals",
            'author': "Jean-Paul Franz",
            'date': "December 11, 2022",
            'body': "Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line."

        },
        {
            'title': "Account and Finance Update",
            'author': "Camilla Devereaux",
            'date': "December 9, 2022",
            'body': "Podcasting operational change management inside of workflows to establish a framework. Taking seamless key performance indicators offline to maximise the long tail. Keeping your eye on the ball while performing a deep dive on the start-up mentality to derive convergence on cross-platform integration."

        }
    ]

    return render_template('index.html', context=context)


app.run(debug=True)
