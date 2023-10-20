# news-assistant
A ChatGPT based assistant summarizing the top 3 news in the field you choose.

## How to run
- Copy the `config.json.example` file to `config.json`.
- Fill in a newsapi key and a OpenAI key in the `config.json` file.
- Install dependencies using `pip install -r requirements`
- Run using `python main.py`

## A l'attention des étudiants du cours Cyber B3 à l'IASchool.
Voici une version "corrigé" du TP fait en cours.  

Vous remarquez l'usage d'un fichier de configuration pour rentrer les clés API. Le fichier de configuration tel que commit sur ce repo ne contient pas de clé. En effet, si ces clés se retrouvaient sur GitHub, alors n'importe qui pourrait les réutiliser. Il est important de faire attention à cela dans vos projets.  

Les différentes étapes du processus (recueil des news, extraction du contenu de l'article, l'action de résumer) sont séparées dans plusieurs fonctions. Celles-ci ne sont pas "parfaites", nous discuterons du pourquoi lors du prochain cours et verrons comment utiliser les classes du paradigme orient-objet afin "d'inverser les dépendances".

Remarquez que le prompt demande à ChatGPT de traduire l'article s'il est dans une autre langue que l'anglais.

De la même manière que le "jeu du random", nous avons une boucle qui demande à l'utilisateur s'il souhaite consulter les news d'un autre sujet, et dans le cas où l'utilisateur ne souhaite pas recommencer, on utilise `break` pour sortir de la boucle.

J'ai laissé des commentaires dans le code à votre attention.


## Licence
GNU GPL-3