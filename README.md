#  Réponse 

Implémentation d'un programme (en Python) lisant le fichier pdf en octets par la fin. 
La méthode *block_search_eof()*, de la classe *BackwardsSearcher(path)*, va étudier la présence de %%EOF en debut d'une ligne, dans un block de 30 octets, puis passer au suivant. 
La fonction remonte ainsi le fichier pdf, et si %%EOF est trouvé, on print sa position dans le pdf en octet, sinon on print -1.

## Execution du fichier py

Le fichier .py s'appelle ma_solution et s'exécute depuis la commande de la sorte : 
```
> python ma_solution test_1.pdf
4568
```

Pour executer tous les tests d'un coup, j'ai créé un fichier .py avec unittest, regroupant tous les tests. Ce fichier s'appelle *testma_solution*.

J'ai ajouté 2 tests aux fichiers pdf existants, pour tester le bon comportement de la fonction sur un fichier commençant par %%EOF et un fichier court (19 caractères en octet).

Pour exécuter le fichier test :

```
> python testma_solution
```

## Optimisation en temps et en RAM

- utilisation des fonctions natives, comme f.read() et .rfind()
- lecture par block de 30 octets en commençant par la fin du document. Une taille de block de 1028 octets sera plus rapide mais utilsiera plus de RAM.
- controle en temps par line_profile et en ram par memory_profiler

## Mesure du temps d'exécution

Afin de surveiller le temps d'exécution du programme, j'ai ajouté un @profile (commenté de base) pour afficher le temps d'exécution de chaque étape du programme.
Je vous montre la manipulation à effectuer, pour décommenter les lignes nécessaires afin de mesurer le temps d'exécution du programme.

La fonction a besoin de 3 ms dans le pire des cas (test_4.pdf où %%EOF est absent), ce qui me paraît suffisamment bas.

https://user-images.githubusercontent.com/51303242/151421726-429c83e1-5fc7-40e2-8125-604bf52073ee.mp4

## Mesure de la RAM du programme 

De même pour l'utilisation de la RAM, petite vidéo explicative.
Toutefois, j'ai des doutes sur la précision des mesures, car la RAM utilisée ne change jamais, quelque soit le temps d'exécution.

https://user-images.githubusercontent.com/51303242/151421695-4e54f843-d1d2-4de8-9150-105426263e0f.mp4










