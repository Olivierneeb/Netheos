#  Réponse 

Implémentation d'un programme (en Python) lisant le fichier pdf en octets par la fin. 


## Execution du fichier py

```
> python ma_solution test_1.pdf
4568
```

Pour executer tous les tests d'un coup, j'ai créé un fichier .py avec unittest, regroupant tous les tests. Ce fichier s'appelle testma_solution

J'ai ajouté 3 tests aux fichiers pdf existants, pour tester le bon comportement de la fonction sur un fichier vide, un fichier commençant par %%EOF et un fichier court (19 caractères en octet).

```
> python testma_solution
```

## Optimisation en temps et en RAM

- utilisation des fonctions natives, comme f.read() et .rfind()
- lecture par block de 30 octets en commençant par la fin du document. Une taille de block de 1028 octets sera plus rapide mais utilsiera plus de RAM.
- controle en temps par line_profile et en ram par memory_profiler

## Mesure du temps d'exécution

Manipulation pour mesurer le temps d'exécution du programme.

https://user-images.githubusercontent.com/51303242/151418884-c9ded3fa-4d76-4243-a8b5-c572606dfc4f.mp4

## Mesure de la ram du programme 

Manipulation pour regarder la ram prise par chaque étape du programme.

https://user-images.githubusercontent.com/51303242/151421355-549813e8-74c4-49c4-8fd4-46a86268ef46.mp4






