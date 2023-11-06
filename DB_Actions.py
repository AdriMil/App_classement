import pymongo

def connexion():
    # Remplacez ces valeurs par vos propres informations d'identification et le nom de votre cluster
    username = 'Admin'
    password = 'Admin'
    cluster_name = 'Cluster0'
    # Construire l'URI de connexion
    cluster_uri = f'mongodb+srv://{username}:{password}@cluster0.3o58hcw.mongodb.net/MyDb_Players?retryWrites=true&w=majority'
    # Établir la connexion au cluster
    client = pymongo.MongoClient(cluster_uri)
    # Accéder à une base de données spécifique (remplacez 'my_database' par le nom de votre base de données)
    database = client['MyDb_Players']
    # Accéder à une collection spécifique dans la base de données (remplacez 'my_collection' par le nom de votre collection)
    collection = database['Players']
    return collection


def nom_from_db(collection):
    valeurs_nom = collection.distinct("nom")
    # Afficher les valeurs extraites
    # print(valeurs_nom)
    return valeurs_nom

def send_new_name_to_DB(collection,New_names):
    nouveau_jeu_de_donnees = {
    'nom': New_names,
    'victoire': 0,
    'defaite': 0,
    'nul': 0,
    'parties': 0
    }
    try:
        collection.insert_one(nouveau_jeu_de_donnees)
        Msg = "Insertion réussie !"
        print(Msg)
    except Exception as e:
        Msg = (f"Erreur lors de l'insertion : {e}")
        print(Msg)


