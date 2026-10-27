from django.http import JsonResponse
import random

quotes = [
    {
    "quote": "But I deal with this by meditating and by understanding I’ve been put on the planet to serve humanity. I have to remind myself to live simply and not overindulge, which is a constant battle in a material world.",
    "author": "Sandra Cisneros",
    "year": "1954",
    },
    {
    "quote": "There are two ways to be rich: One is by acquiring much, and the other is by desiring little.",
    "author": "Jackie French Koller",
    "year": "1948",
    },
    {
    "quote": "Simplicity involves unburdening your life, and living more lightly with fewer distractions that interfere with a high quality life, as defined uniquely by each individual.",
    "author": "Linda Breen Pierce",
    "year": "1947",
    },
    {
    "quote": "One of the advantages of being born in an affluent society is that if one has any intelligence at all, one will realize that having more and more won’t solve the problem, and happiness does not lie in possessions, or even relationships: The answer lies within ourselves. If we can’t find peace and happiness there, it’s not going to come from the outside.",
    "author": "Tenzin Palmo",
    "year": "1943",
    },
    {
    "quote": "The intention of voluntary simplicity is not to dogmatically live with less. It’s a more demanding intention of living with balance. This is a middle way that moves between the extremes of poverty and indulgence.",
    "author": "Duane Elgin",
    "year": "1940s",
    },
    {
    "quote": "We really must understand that the lust for affluence in contemporary society is psychotic. It is psychotic because it has completely lost touch with reality. We crave things we neither need nor enjoy.",
    "author": "Richard Foster",
    "year": "1940s",
    },
    {
    "quote": "The trouble with simple living is that, though it can be joyful, rich, and creative, it isn’t simple.",
    "author": "Doris Janzen Longacre",
    "year": "1940",
    },
    {
    "quote": "Any half-awake materialist well knows – that which you hold holds you.",
    "author": "Tom Robbins",
    "year": "1936",
    },
    {
    "quote": "The simplest things are often the truest.",
    "author": "Richard Bach",
    "year": "1936",
    },
    {
    "quote": "Our souls are not hungry for fame, comfort, wealth, or power. Our souls are hungry for meaning, for the sense that we have figured out how to live so that our lives matter.",
    "author": "Harold Kushner",
    "year": "1935",
    },
    {
    "quote": "If one’s life is simple, contentment has to come. Simplicity is extremely important for happiness. Having few desires, feeling satisfied with what you have, is very vital: satisfaction with just enough food, clothing, and shelter to protect yourself from the elements.",
    "author": "The Dalai Lama",
    "year": "1935",
    },
    {
    "quote": "Smile, breathe and go slowly.",
    "author": "Thich Nhat Hanh",
    "year": "1926",
    },
    {
    "quote": "The consumption society has made us feel that happiness lies in having things, and has failed to teach us the happiness of not having things.",
    "author": "Elise Boulding",
    "year": "1920",
    },
    {
    "quote": "You have succeeded in life when all you really want is only what you really need.",
    "author": "Vernon Howard",
    "year": "1918",
    },
    {
    "quote": "Any intelligent fool can make things bigger, more complex, and more violent. It takes a touch of genius – and a lot of courage – to move in the opposite direction.",
    "author": "E.F. Schumacher",
    "year": "1911",
    },
    {
    "quote": "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.",
    "author": "Antoine de Saint-Exupery",
    "year": "1900",
    },
    {
    "quote": "Reduce the complexity of life by eliminating the needless wants of life, and the labors of life reduce themselves.",
    "author": "Edwin Way Teale",
    "year": "1899",
    },
    {
    "quote": "Besides the noble art of getting things done, there is the noble art of leaving things undone.  The wisdom of life consists in the elimination of non-essentials.",
    "author": "Lin Yutang",
    "year": "1895",
    },
    {
    "quote": "Less is more.",
    "author": "Mies Van Der Rohe",
    "year": "1886",
    },
    {
    "quote": "Make things as simple as possible but no simpler.",
    "author": "Albert Einstein",
    "year": "1879",
    },
    {
    "quote": "Too many people spend money they haven’t earned, to buy things they don’t want, to impress people they don’t like.",
    "author": "Will Rogers",
    "year": "1879",
    },
    {
    "quote": "Simplicity is an acquired taste. Mankind, left free, instinctively complicates life.",
    "author": "Katharine Fullerton Gerould",
    "year": "1879",
    },
    {
    "quote": "One can furnish a room very luxuriously by taking out furniture rather than putting it in.",
    "author": "Francis Jourdain",
    "year": "1876",
    },
    {
    "quote": "It is preoccupation with possession, more than anything else, that prevents men from living freely and nobly.",
    "author": "Bertrand Russell",
    "year": "1872",
    },
    {
    "quote": "We go on multiplying our conveniences only to multiply our cares. We increase our possessions only to the enlargement of our anxieties.",
    "author": "Anna C. Brackett",
    "year": "1836",
    },
    {
    "quote": "Have nothing in your homes that you do not know to be useful or believe to be beautiful.",
    "author": "William Morris",
    "year": "1834",
    },
    {
    "quote": "You say, ‘If I had a little more, I should be very satisfied.’ You make a mistake. If you are not content with what you have, you would not be satisfied if it were doubled.",
    "author": "Charles Spurgeon",
    "year": "1834",
    },
    {
    "quote": "There is no greatness where there is not simplicity, goodness, and truth.",
    "author": "Leo Tolstoy",
    "year": "1828",
    },
    {
    "quote": "Cultivate poverty like a garden herb, like sage. Do not trouble yourself much to get new things, whether clothes or friends. Things do not change, we change. Sell your clothes and keep your thoughts.",
    "author": "Henry David Thoreau",
    "year": "1817",
    },
    {
    "quote": "Be generous in prosperity, and thankful in adversity. Be worthy of the trust of thy neighbor, and look upon him with a bright and friendly face. Be a treasure to the poor, an admonisher to the rich, an answerer of the cry of the needy, a preserver of the sanctity of thy pledge.",
    "author": "Baha’u’llah",
    "year": "1817",
    },
    {
    "quote": "It is the heart that makes a man rich. He is rich according to what he is, not according to what he has.",
    "author": "Henry David Beecher",
    "year": "1813",
    },
    {
    "quote": "Simplicity is the most difficult thing to secure in this world; it is the last limit experience and the last effort of genius.",
    "author": "George Sand",
    "year": "1804",
    },
    {
    "quote": "My riches consist, not in the extent of my possessions, but in the fewness of my wants.",
    "author": "Joseph Brotherton",
    "year": "1783",
    },
    {
    "quote": "Live simply so that others may simply live.",
    "author": "Elizabeth Ann Seton",
    "year": "1774",
    },
    {
    "quote": "Real happiness is cheap enough, yet how dearly we pay for its counterfeit.",
    "author": "Hosea Ballou",
    "year": "1771",
    },
    {
    "quote": "With a few flowers in my garden, half a dozen pictures and some books, I live without envy.",
    "author": "Lope de Vega",
    "year": "1562",
    },
    {
    "quote": "Simplicity is the ultimate sophistication.",
    "author": "Leonardo da Vinci",
    "year": "1452",
    },
    {
    "quote": "Purity and simplicity are the two wings with which man soars above the earth and all temporary nature.",
    "author": "Thomas a Kempis",
    "year": "1380",
    },
    {
    "quote": "If your mind isn’t clouded by unnecessary things, then this is the best season of your life.",
    "author": "Wu-Men",
    "year": "864",
    },
    {
    "quote": "Poverty is my pride.",
    "author": "Muhammed",
    "year": "570",
    },
    {
    "quote": "If one had taken what is necessary to cover one’s needs and had left the rest to those who are in need, no one would be rich, no one would be poor, no one would be in need.",
    "author": "Saint Basil",
    "year": "330",
    },
    {
    "quote": "Contentment comes not so much from great wealth as from few wants.",
    "author": "Epictetus",
    "year": "55",
    },
    {
    "quote": "It is not the man who has too little, but the man who craves more, that is poor.",
    "author": "Seneca",
    "year": "1 BCE",
    },
    {
    "quote": "Sell your possessions and give to the poor.",
    "author": "Jesus Christ",
    "year": "5 BCE",
    },
    {
    "quote": "The man who has two tunics is to share with him who has none; and he who has food is to do likewise.",
    "author": "John the Baptist",
    "year": "6 BCE",
    },
    {
    "quote": "Nothing is enough for the man to whom enough is too little.",
    "author": "Epicurus",
    "year": "341 BCE",
    },
    {
    "quote": "The secret of happiness, you see, is not found in seeking more, but in developing the capacity to enjoy less.",
    "author": "Socrates",
    "year": "469 BCE",
    },
    {
    "quote": "Be content with what you have; rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you.",
    "author": "Lao Tzu",
    "year": "500 BCE",
    },
    {
    "quote": "Life is really simple, but we insist on making it complicated.",
    "author": "Confucious",
    "year": "551 BCE",
    },
    {
    "quote": "To live a pure unselfish life, one must count nothing as one’s own in the midst of abundance.",
    "author": "Buddha",
    "year": "563 BCE",
    },
]

def get_quotes_all_json(request):
    return JsonResponse(data={"data": quotes}, status=200)

def get_quotes_random_json(request):
    picked = random.choice(quotes)
    return JsonResponse(data={"data": picked}, status=200)
