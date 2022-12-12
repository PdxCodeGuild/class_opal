from flask import Flask, render_template
app = Flask(__name__)

post_list = [
    {
        'title': "Nice Furniture? I don't think so!",
        'author': "Charlie Paws,    ",
        'date': "October 14th, 2020",
        'body': "Attack feet behind the couch destroy couch flop over give attitude hide when guests come over hopped up on goofballs hunt anything that moves shake treat , chew ipad power cord  make muffins intently stare at the same spot sweet beast under the bed leave dead animals as gifts inspect anything brought into the house   rub face on everything, lick butt flop over bag stretch  stand in front of the computer screen   claw drapes chew ipad power cord  bag stretch. Inspect anything brought into the house hide when guests come over intently stare at the same spot leave dead animals as gifts flop over  rub face on everything shake treat  lick butt  attack feet hopped up on goofballs make muffins, flop over behind the couch hunt anything that moves destroy couch chew ipad power cord."
    },
    {
        'title': "So you wanna get some work done",
        'author': "King Friday,    ",
        'date': "August 28, 2021",
        'body': "Stand in front of the computer screen  bag stretch give attitude  claw drapes sweet beast under the bed. Destroy couch flop over  hopped up on goofballs hunt anything that moves inspect anything brought into the house chew ipad power cord  behind the couch flop over  claw drapes make muffins, intently stare at the same spot sweet beast under the bed shake treat  leave dead animals as gifts give attitude hide when guests come over  rub face on everything bag stretch  stand in front of the computer screen  lick butt attack feet, flop over give attitude  claw drapes hopped up on goofballs lick butt hunt anything that moves bag stretch flop over inspect anything brought into the house."
    },
    {
        'title': "Cats and ADHD",
        'author': "Muffins Butterscotch,    ",
        'date': "March 31, 2022",
        'body': "Flop over intently stare at the same spot  claw drapes  stand in front of the computer screen  attack feet destroy couch make muffins, hide when guests come over hunt anything that moves chew ipad power cord  give attitude  rub face on everything shake treat  leave dead animals as gifts, sweet beast under the bed lick butt flop over hopped up on goofballs bag stretch behind the couch hide when guests come over.  rub face on everything flop over hopped up on goofballs inspect anything brought into the house shake treat."
    },
    {
        'title': "It's not you, it's me (your cat)",
        'author': "Jedi McLickin,    ",
        'date': "May 4, 2022",
        'body': "Give attitude hide when guests come over  attack feet make muffins chew ipad power cord  shake treat  bag stretch flop over, sweet beast under the bed  rub face on everything behind the couch hopped up on goofballs leave dead animals as gifts inspect anything brought into the house  claw drapes hunt anything that moves flop over,  stand in front of the computer screen  lick butt destroy couch intently stare at the same spot hunt anything that moves make muffins sweet beast under the bed.  stand in front of the computer screen  sweet beast under the bed behind the couch  give attitude shake treat   claw drapes lick butt, bag stretch leave dead animals as gifts  rub face on everything hunt anything that moves inspect anything brought into the house make muffins destroy couch, hopped up on goofballs chew ipad power cord  hide when guests come over flop over intently stare at the same spot flop over."
    }
]
@app.route('/')
def index():
    print(post_list)
    return render_template('lab04.html', posts=post_list)

app.run(debug=True)