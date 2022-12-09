from flask import Flask, render_template

app = Flask(__name__)


POSTS = [
    {
        'id': 1,
        'title': "A look at Members of Delight Infinite",
        'author': "hyeongjun",
        'icon': '/static/test.png',
        'date': "Today at 4:20 pm",
        'body': ["Un ensemble comprenant un adaptateur peut être utilisé pour raccorder des conducteurs cardiaques implantés à un dispositif d'essai.",
        "L'invention concerne un connecteur séparable destiné à raccorder électriquement deux parties de câbles multiconducteurs."
        "La liaison d'actionnement peut raccorder le mécanisme de verrouillage et l'actionneur."]
    }, {
        'id': 2,
        'title': "AWOL's Debut: Highs and Lows",
        'author': "rockee",
        'date': "Dec. 9 at 11:56 pm",
        'body': ["Cupcake ipsum dolor sit amet chocolate bar lollipop carrot cake pudding. Wafer fruitcake tart lollipop jelly beans danish liquorice topping pastry. Dragée dessert powder tootsie roll pastry cake muffin candy gingerbread. Chocolate bar ice cream jelly-o sugar plum chocolate cake cookie cake cake dessert. Topping toffee pastry sesame snaps bear claw. Cookie cotton candy jujubes sweet roll caramels biscuit macaroon ice cream. Toffee icing toffee cheesecake bear claw. Candy canes chocolate cake powder chupa chups muffin biscuit oat cake. Fruitcake marzipan sweet wafer cake danish cupcake lemon drops. Candy bear claw jujubes pie bear claw pie sweet.",
        "Wafer pie croissant donut toffee brownie wafer jelly-o. Jelly lemon drops jelly beans macaroon tart marzipan lollipop. Oat cake gummies pie pudding pie pie gummies ice cream. Candy marzipan macaroon pudding topping halvah cake marshmallow biscuit. Danish bonbon sweet roll tootsie roll caramels.",
        "Danish toffee chupa chups donut liquorice. Dessert shortbread gummies sweet roll muffin dessert cupcake marzipan. Cake wafer gummies liquorice cupcake. Icing wafer cheesecake chocolate cake croissant jelly beans jelly. Donut pie apple pie tootsie roll apple pie topping pastry cake apple pie. Croissant pastry donut gummi bears caramels chocolate cake sesame snaps gummi bears."],
    }, {
        'id': 3,
        'title': "Delight Infinite Skyrocketing to the Top",
        'author': "hyeongjun",
        'date': "Dec. 9 at 11:19 am",
        'body': ["Yolo ipsum dolor sit amet, consectetur adipiscing elit. Ut ac suscipit leo. Carpe diem vulputate est nec commodo rutrum. Pellentesque mattis convallis nisi eu and I ain't stoppin until the swear jar's full.",
        "Ut rhoncus velit at mauris interdum, fringilla dictum neque rutrum. Curabitur mattis odio at erat viverra lobortis. Poppin' bottles on the ice, tristique suscipit mauris elementum tempus. Quisque ut felis vitae elit tempor interdum viverra a est. Drop it like it's hot, at pretium quam. In nec scelerisque purus. Nam dignissim lacus ipsum, a ullamcorper nulla pretium non. Aliquam sed enim faucibus, pulvinar felis at, vulputate augue. Ten, ten, twenties on them fifties, trick, at tempus libero fermentum id. Vivamus ut nisi dignissim, condimentum urna vel, dictum massa. Donec justo yolo, rutrum vitae dui in, dapibus tempor tellus. I do it big. Fusce ut sagittis mi."],
    }, {
        'id': 4,
        'title': "DZJ Happiness is Overrated",
        'author': "yoshi",
        'date': "Dec. 9 at 4:30 am",
        'body': ["Yolo ipsum dolor sit amet, consectetur adipiscing elit. Ut ac suscipit leo. Carpe diem vulputate est nec commodo rutrum. Pellentesque mattis convallis nisi eu and I ain't stoppin until the swear jar's full. Ut rhoncus velit at mauris interdum, fringilla dictum neque rutrum. Curabitur mattis odio at erat viverra lobortis. Poppin' bottles on the ice, tristique suscipit mauris elementum tempus. Quisque ut felis vitae elit tempor interdum viverra a est.",
        "Drop it like it's hot, at pretium quam.",
        "In nec scelerisque purus. Nam dignissim lacus ipsum, a ullamcorper nulla pretium non. Aliquam sed enim faucibus, pulvinar felis at, vulputate augue. Ten, ten, twenties on them fifties, trick, at tempus libero fermentum id. Vivamus ut nisi dignissim, condimentum urna vel, dictum massa. Donec justo yolo, rutrum vitae dui in, dapibus tempor tellus. I do it big. Fusce ut sagittis mi."],
    }, {
        'id': 5,
        'title': "What's up with KST Seekers' Sneakers? (Wardrobe Analysis)",
        'author': "rockee",
        'date': "Dec. 8 at 2:56 pm",
        'body': ["Yolo ipsum dolor sit amet, consectetur adipiscing elit. Ut ac suscipit leo. Carpe diem vulputate est nec commodo rutrum.",
        "Pellentesque mattis convallis nisi eu and I ain't stoppin until the swear jar's full. Ut rhoncus velit at mauris interdum, fringilla dictum neque rutrum.",
        "Curabitur mattis odio at erat viverra lobortis. Poppin' bottles on the ice, tristique suscipit mauris elementum tempus. Quisque ut felis vitae elit tempor interdum viverra a est.",
        "Drop it like it's hot, at pretium quam. In nec scelerisque purus. Nam dignissim lacus ipsum, a ullamcorper nulla pretium non. Aliquam sed enim faucibus, pulvinar felis at, vulputate augue."
        "Ten, ten, twenties on them fifties, trick, at tempus libero fermentum id. Vivamus ut nisi dignissim, condimentum urna vel, dictum massa. Donec justo yolo, rutrum vitae dui in, dapibus tempor tellus. I do it big. Fusce ut sagittis mi."],
    }, {
        'id': 6,
        'title': "Timeless Boyz aren't as Timeless as we Thought",
        'author': "yonghee",
        'date': "Dec. 8 at 1:00 pm",
        'body': ["Yolo ipsum dolor sit amet, consectetur adipiscing elit. Ut ac suscipit leo. Carpe diem vulputate est nec commodo rutrum.",
        "Pellentesque mattis convallis nisi eu and I ain't stoppin until the swear jar's full. Ut rhoncus velit at mauris interdum, fringilla dictum neque rutrum.",
        "Curabitur mattis odio at erat viverra lobortis. Poppin' bottles on the ice, tristique suscipit mauris elementum tempus. Quisque ut felis vitae elit tempor interdum viverra a est.",
        "Drop it like it's hot, at pretium quam. In nec scelerisque purus. Nam dignissim lacus ipsum, a ullamcorper nulla pretium non. Aliquam sed enim faucibus, pulvinar felis at, vulputate augue."
        "Ten, ten, twenties on them fifties, trick, at tempus libero fermentum id. Vivamus ut nisi dignissim, condimentum urna vel, dictum massa. Donec justo yolo, rutrum vitae dui in, dapibus tempor tellus. I do it big. Fusce ut sagittis mi."],
    }
]


@app.route("/")
def index():
    return render_template('main_blog.html', posts=POSTS)


@app.route('/<int:id>')
def page(id):
    for post in POSTS:
        if post["id"]==id:
            return render_template('blog_page.html', post=post)
        # return (post)


app.run(debug=True)
