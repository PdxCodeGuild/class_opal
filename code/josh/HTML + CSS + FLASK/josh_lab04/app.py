from flask import Flask, render_template
app = Flask(__name__)

posts = [{
    'title': 'Cheeseburger Ipsum',
    'author': 'C.B. McBlogger',
    'date': 'October 14th, 2021',
    'body': 'The last time you had a cheeseburger was too long ago. Try not to drool when you think about the slightly charred, medium-rare meat nestled between soft brioche, cradled in crisp iceberg lettuce and flavour amplifying condiments. Why are you still reading this- go get a cheeseburger.'
}, {
    'title': 'Cupcake Ipsum',
    'author': 'C.C. Baker',
    'date': 'December 30th, 2021',
    'body': '''Chocolate bar tart croissant bear claw ice cream lollipop danish. Chupa chups jelly-o biscuit soufflé sesame snaps liquorice brownie. Carrot cake cake pie oat cake brownie jelly-o. Powder wafer oat cake chocolate gummies. Donut carrot cake macaroon donut cupcake. Carrot cake brownie cookie macaroon caramels candy canes gingerbread. Chocolate cake dessert gummies topping halvah. Chocolate cake macaroon sweet sesame snaps powder lemon drops cake icing. Wafer soufflé apple pie lollipop biscuit pastry.

Cupcake jelly beans sweet cake jelly toffee marshmallow brownie tart. Cotton candy bear claw marzipan halvah sugar plum macaroon soufflé tart sugar plum. Jujubes sugar plum macaroon sesame snaps chocolate soufflé macaroon biscuit. Jelly-o soufflé jelly lollipop biscuit carrot cake muffin. Tootsie roll macaroon tiramisu pudding ice cream. Ice cream brownie candy canes sesame snaps shortbread dessert.

Biscuit brownie danish sugar plum candy lemon drops. Pastry danish jelly-o marshmallow lollipop lollipop pudding carrot cake tiramisu. Oat cake lemon drops gummi bears oat cake oat cake gingerbread brownie candy canes. Icing lemon drops donut chupa chups croissant gingerbread pudding pudding. Jelly beans dragée jujubes dessert toffee donut. Soufflé macaroon topping cupcake candy gingerbread cake. Sugar plum pastry jelly beans jelly bonbon lemon drops topping jelly fruitcake. Tart halvah tootsie roll jelly-o lollipop candy canes.'''
}, {
    'title': 'Cheese Ipsum',
    'author': 'C. Eater',
    'date': 'February 18th, 2022',
    'body': '''Melted cheese cheese triangles feta. Bavarian bergkase stilton fondue cauliflower cheese danish fontina caerphilly cheese triangles paneer. Cheese strings airedale paneer swiss cheeseburger cheese triangles queso goat. Ricotta squirty cheese cheddar cheesecake pecorino cheeseburger fondue.

Cream cheese chalk and cheese halloumi. Paneer pecorino mascarpone cheesecake pepper jack mascarpone mascarpone danish fontina. Croque monsieur mascarpone cow cheese on toast everyone loves paneer cut the cheese st. agur blue cheese. Cheesy feet goat stilton chalk and cheese cheese triangles everyone loves.

Cut the cheese cheddar croque monsieur. Stinking bishop airedale caerphilly boursin airedale say cheese cheese triangles croque monsieur. Rubber cheese cheesy grin macaroni cheese monterey jack jarlsberg st. agur blue cheese dolcelatte everyone loves. Hard cheese cheeseburger pecorino bavarian bergkase cauliflower cheese croque monsieur cheese strings.'''
}, {
    'title': 'Bacon Ipsum',
    'author': 'Pork E. Pig',
    'date': 'May 9th, 2022',
    'body': '''Bacon ipsum dolor amet chicken pig pork chop strip steak. Short loin ham meatloaf, bacon rump meatball chicken kielbasa ball tip ribeye. Biltong buffalo bacon porchetta sausage meatball brisket rump pig beef ribs doner corned beef. Strip steak sirloin swine picanha turducken.

Rump pork belly pork loin hamburger ham picanha short loin tongue porchetta pork ribeye. Ham chuck alcatra strip steak. Jowl ham tenderloin pancetta sausage corned beef frankfurter pastrami capicola andouille leberkas short ribs turducken porchetta pork loin. Pancetta shoulder boudin burgdoggen chicken shankle hamburger rump beef ribs. Sirloin swine biltong ham burgdoggen venison landjaeger capicola boudin alcatra ground round pancetta. Beef short loin bresaola leberkas buffalo alcatra, ball tip doner strip steak biltong rump.'''
}]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)


app.run(debug=True)