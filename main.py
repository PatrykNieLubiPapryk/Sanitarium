from flask import Flask
import random

app = Flask(__name__)

facts_list = ['Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.',
'Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.',
'Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.',
'Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.',
'Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.',
'Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.',
'Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.',
'Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi.']

@app.route("/")
def text():
    return '<h1>Cześć! Na tej stronie możesz dowiedzieć się kilku ciekawostek na temat zależności technologicznych!</h1> <a href="/random_fact">Zobacz losowy fakt!</a> <p><a href="/coin_flip">Rzuć monetą!</a></p>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin_flip")
def coin_flip():
    result = random.randint(0,1)
    if result == 0:
        return '<h1>Orzeł</h1>'
    else:
        return '<h1>Reszka</h1>'

app.run(debug=True)
