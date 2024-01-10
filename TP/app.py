from flask import Flask, render_template , request
import mysql.connector


app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Récupérer les valeurs du formulaire
            email = request.form['email']
            password = request.form['password']

            # Connexion à la base de données MySQL
            conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='frame'
            )

            # Création d'un curseur
            cursor = conn.cursor()

            # Exécution de la requête d'insertion
            insert_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (email, password))

            # Validation des changements dans la base de données
            conn.commit()

            # Fermeture de la connexion
            conn.close()

            message = "Formulaire soumis avec succès et les données ont été ajoutées à la base de données!"

        except mysql.connector.Error as e:
            # Affichage d'une erreur si la connexion à la base de données échoue
            print("Erreur de connexion à la base de données MySQL:", e)
            message = "Erreur lors de la soumission du formulaire."

    else:
        message = ""

    return render_template('index.html', message=message)
@app.route('/about')
def about():
    return render_template('about.html', company_name=company_name)



if __name__ == '__main__':
    app.run(debug=True)