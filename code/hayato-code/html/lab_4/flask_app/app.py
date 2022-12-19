from flask import Flask, render_template
app = Flask(__name__)

posts = [{
    'title': 'Veggie Ipsum',
    'author': 'Vegian eater',
    'date': 'October 1th, 1980',
    'body': 'Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.'
}, {
    'title': 'Kiwi Ipsum',
    'author': 'Lord Kiwi',
    'date': 'January 30th, 2021',
    'body': '''A slice of heaven. O for awesome, this chocka full cuzzie is as rip-off as a cracker. Meanwhile, in behind the bicycle shed, Hercules Morse, as big as a horse and Mrs Falani were up to no good with a bunch of crook pikelets. Meanwhile, at the black singlet woolshed party, not even au, sort your drinking out.'''
}, {
    'title': 'Cheese Ipsum',
    'author': 'cut the cheese',
    'date': 'February 24th, 2012',
    'body': '''Bavaria ipsum dolor sit amet Radler Schneid vui huift vui ognudelt i mechad dee Schwoanshaxn Zwedschgndadschi a bissal wos gehd ollaweil. Measi a ganze es i mog di fei aasgem, Blosmusi. Schmankal zwoa Ramasuri Edlweiss. Wia vo de Weiznglasl wos, imma hogg di hera Guglhupf! Schorsch Spotzerl schnacksln Weiznglasl vui gschmeidig a ganze auf der Oim, da gibt’s koa Sünd, etza!'''
}, {
    'title': 'Bacon Ipsum',
    'author': 'class pig',
    'date': 'May 12th, 2022',
    'body': '''Bacon ipsum dolor amet chicken pig pork chop strip steak. Short loin ham meatloaf, bacon rump meatball chicken kielbasa ball tip ribeye. Biltong buffalo bacon porchetta sausage meatball brisket rump pig beef ribs doner corned beef. Strip steak sirloin swine picanha turducken.
Rump pork belly pork loin hamburger ham picanha short loin tongue porchetta pork ribeye. Ham chuck alcatra strip steak. Jowl ham tenderloin pancetta sausage corned beef frankfurter pastrami capicola andouille leberkas short ribs turducken porchetta pork loin. Pancetta shoulder boudin burgdoggen chicken shankle hamburger rump beef ribs. Sirloin swine biltong ham burgdoggen venison landjaeger capicola boudin alcatra ground round pancetta. Beef short loin bresaola leberkas buffalo alcatra, ball tip doner strip steak biltong rump.'''
}]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)


app.run(debug=True)