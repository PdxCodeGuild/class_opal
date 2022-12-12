from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    #     return 'Hello World!'

    # def index():
    posts = [
        {
            'title': " Well that's a tad Shakespearean don't you think?",
            'author': "Wayne",
            'date': "November 5, 1955",
            'body': "I see the muscle shirt came today. Muscles coming tomorrow? How're you now? Good, and you? Not so bad. I second baby, I second so hard. Give yer balls a tug ya tit fucker! Figure it out. Does a duck with a boner drag weeds? It's like algebra...why you gotta put numbers and letters together. Why can't you just go fuck yourself? Thank you baby, I knew you'd second the shit right out of it. Except kids falling off bikes, fuck, I could watch kids fall off bikes all day, I don't give a shit about your kids. To be fair."
        },
        {
            'title': "Well I think you've all had too much sugar cereal!",
            'author': "Katy",
            'date': "November 5, 2021",
            'body': "To be fair. Give yer balls a tug ya tit fucker! Get off the cross we need the wood... Fuck Lemony Snicket, what a serious of unfortunate events you fuckin been through you ugly fuck. Oh I'm stomping the brakes, put that idea right through the fucking windshield. I got the ass pisses something fierce. Also known as pizazz. I second baby, I second so hard. Oh I'm stomping the brakes, put that idea right through the fucking windshield. To be fair. Well that's a tad Shakespearean don't you think?"

        },
        {
            'title': "I see the muscle shirt came today. Muscles coming tomorrow?",
            'author': "Squirrelly Dan",
            'date': "November 5, 2022",
            'body': "Nobody sends a tweet, feels fuckin' sweet! Fuck Lemony Snicket, what a serious of unfortunate events you fuckin been through you ugly fuck. Get off the cross we need the wood... Well that's a tad Shakespearean don't you think? I got the ass pisses something fierce. Also known as pizazz. It's like algebra...why you gotta put numbers and letters together. Why can't you just go fuck yourself? Oh I'm stomping the brakes, put that idea right through the fucking windshield. Get off the cross we need the wood... Well that's a tad Shakespearean don't you think? Wish you weren't so fucking awkward, bud."

        },
        {
            'title': "Figure it out.",
            'author': "Daryl",
            'date': "November 6, 2022",
            'body': "Yew! Nobody snaps a chat, go fuck your hat. Figure it out. What're we even doing here? How're you now? Good, and you? Not so bad. I second baby, I second so hard. It's like algebra...why you gotta put numbers and letters together. Why can't you just go fuck yourself? To be fair. It's like algebra...why you gotta put numbers and letters together. Why can't you just go fuck yourself? Give yer balls a tug ya tit fucker! Oh I'm stomping the brakes, put that idea right through the fucking windshield. Well I think you've all had too much sugar cereal! Get off the cross we need the wood... Does a duck with a boner drag weeds? Wish you weren't so fucking awkward, bud."

        },
    ]
    return render_template('index.html', posts=posts)


app.run(debug=True)
