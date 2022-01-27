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

## Mesure temsp programme 

<video src='your URL here' width=180/>
