from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True, max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = None
        super(Recipe, self).save(*args, **kwargs)

class Ribbon(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    comments = models.TextField(blank=True, null=True,
                                verbose_name="my comments")
    time_created = models.DateTimeField(auto_now_add=True)

    is_boxed = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    thumb = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} Ribbon for {1}'.format(unicode(self.recipe),
                                           unicode(self.user))

    class Meta:
        unique_together = ('recipe', 'user',)

class Tag(models.Model):
    ribbon = models.ForeignKey(Ribbon)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.key, self.value)

ordered_known_keys = ['course','method','cuisine','type','ingredient','occasion','season','dish','source','concern']
known_keys = {
    'source': ['innout', 'seriouseats'],
    'dish': ['potsticker', 'joong', 'calamari', 'samosa', 'guacamole', 'scone', 'dumpling', 'chutney', 'bbqsauce', 'friedrice', 'ricekrispiesquare', 'brownie', 'snowball', 'nanaimo', 'shrimpscampi', 'coffeecake', 'risotto', 'fruitcake', 'pretzel', 'grilledcheese', 'hashbrowns', 'meringue', 'bbqpork', 'cornbread', 'lemonmeringue', 'applepie', 'burger', 'redvelvet', 'smore', 'sub', 'pavlova', 'jambalaya', 'icecream', 'granola', 'chipotlemayo', 'carbonara', 'biscotti', 'marmalade', 'gnocchi', 'meatpie', 'pancake', 'frosting', 'hummus', 'pudding', 'pita', 'shortcake', 'curry', 'limeade', 'whoopiepie', 'twix', 'etouffee', 'lettucewrap', 'kolache', 'ricekrispietreat', 'custard', 'ciabatta', 'grahamcracker', 'cinnamonbun', 'focaccia', 'danish', 'latke', 'couscous', 'blondie', 'rockyroad', 'icecreambar', 'chili', 'flan', 'donut', 'bananabread', 'meatball', 'slaw', 'challah', 'cobbler', 'poundcake', 'snickerdoodle', 'frenchtoast', 'onionmarmalade', 'pizza', 'truffle', 'froyo', 'mashedpotatoes', 'cheesecake', 'ziti', 'taco', 'puddingcake', 'bostoncreampie', 'roulade', 'croissant', 'ratatouille', 'carnitas', 'carrotcake', 'yellowcake', 'vinaigrette', 'saltedcaramel', 'teriyaki'],
    'ingredient': ["bean","beef","berry","calvados","caraway","cheese","chicken","chocolate","citrus","coffee","coriander","cottagecheese","duck","egg","fennel","fish","fruit","game","ginger","herb","hominy","cornmeal","masa","lamb","lettuce","molasses","mushroom","nut","nutmeg","olive","pasta","pepper","phyllo","puffpastry","poppy","pork","potato","poultry","rice","grain","seed","sesame","shellfish","sour cream","tea","tomato","tortillas","turkey","vegetable","yogurt", 'macaroni', 'cherry', 'artichoke', 'ham', 'peanut', 'avocado', 'almonds', 'fig', 'snickers', 'orange', 'pumpkin', 'pecan', 'goatcheese', 'ketchup', 'buttercream', 'rhubarb', 'balsamicvinegar', 'onion', 'asparagus', 'sweetpotatoes', 'caramel', 'zucchini', 'orzo', 'clam', 'almond', 'bacon', 'butterscotch', 'jalapeno', 'strawberry', 'nutella', 'chocolatechip', 'lime', 'rasberry', 'porkchops', 'eggnog', 'pear', 'corn', 'raspberry', 'mozzarella', 'cabbage', 'oreo', 'rosemary', 'brownsugar', 'oatmeal', 'shrimp', 'cinnamon', 'eggplant', 'cranberry', 'apple', 'marshmallow', 'tofu', 'scallop', 'walnut', 'maple', 'spinach', 'basil', 'banana', 'creamcheese', 'pepperment', 'squash', 'sweetpotato', 'greenonion', 'apricot', 'vanilla', 'blueberry', 'brusselsprout', 'tapioca', 'plum', 'coconut', 'carrot', 'redpepper', 'lemon', 'peach', 'peanutbutter', 'spaghetti', 'cashew', 'nut', 'butterfinger', 'feta', 'pistachio', 'pineapple', 'salmon', 'maplesyrup', 'date', 'oliveoil'],
    'type': ['bread', 'cake', 'candy', 'condiment', 'spread', 'cookie', 'cupcake', 'marinade', 'muffin', 'pastry', 'pie', 'tart', 'salad', 'sandwich', 'sauce', 'seasoning', 'spices', 'soup', 'stew', 'stuffing', 'vegetable', 'shake', 'bar', 'meat', 'dip', 'noodle', 'crisp', 'drink', 'biscuit', 'roll', 'tart', 'bun', 'quickbread', 'seafood'],
    'cuisine': ['african', 'american', 'asian', 'cajun', 'chinese', 'russian', 'english', 'scottish', 'french', 'german', 'greek', 'indian', 'irish', 'italian', 'japanese', 'jewish', 'mediterranean', 'mexican', 'middleeastern', 'moroccan', 'scandinavian', 'southern', 'southwestern', 'spanish', 'portuguese', 'thai', 'vietnamese', 'czech', 'persian', 'hawaiian', 'swedish'],
    'occasion': ['christmas', 'easter', 'halloween', 'hanukkah', 'newyears', 'passover', 'roshhashanah', 'yumkippur', 'thanksgiving', 'valentinesday'],
    'season': ['fall', 'winter', 'spring', 'summer'],
    'course': ['appetizer', 'breakfast', 'brunch', 'buffet', 'dessert', 'dinner', 'lunch', 'maincourse', 'side', 'snack', 'leftover'],
    'method': ['bake', 'barbecue', 'boil', 'braise', 'broil', 'freeze', 'fry', 'grill', 'marinate', 'microwave', 'nocook', 'poach', 'quick', 'roast', 'saute', 'simmer', 'slowcook', 'steam', 'stew', 'stirfry', 'deepfry', 'bbq'],
    'concern': ['healthy', 'highfiber', 'kosher', 'lowcalorie', 'lowcarb', 'lowfat', 'lowsodium', 'lowsugar', 'raw', 'vegan', 'vegetarian', 'glutenfree', 'easy', 'fancy', 'spicy', 'wholewheat'],
    }
known_values_to_keys = {}
for key, values in known_keys.items():
    for value in values:
        known_values_to_keys[value] = key
