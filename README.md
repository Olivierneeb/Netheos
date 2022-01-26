# But 

implémenter les fonctions pour déterminer si un fichier pdf est corrompu ou tronqué

## présentation du problème 

Netheos traite des justificatifs uploadés par les internautes, en particulier
des fichiers pdf. Certains fichiers présentent des anomalies : ils sont tronqués
(la fin du fichier est manquante), ce qui empêche leur traitement.

Un fichier pdf bien formé devrait se terminer par une ligne commençant par  '%%EOF' (avec parfois,
rarement, des octets parasites après cette marque).

L'objet de l'exercice est de déterminer de manière rapide l'offset dans le fichier de la dernière occurence de la 'ligne' commençant par '%%EOF'. l'offset est l'index en octet dans le fichier du premier charactère, ou -1 si le fichier ne contient pas d'occurrence.


## livrable attendu 

Un script ou executable dans un language au choix parmi Java, python, c ou c++ ou kotlin ( merci de fournir des instructions pour compiler si applicable ) avec une interface en ligne de commande, prenant en argument le chemin vers le fichier pdf à analyser, et affichant sur la sortie standard l'offset en decimal. 

Par exemple, si l'executable se lance avec `./masolution`, et avec les exemples fournis :

```
> ./masolution test_1.pdf
4568

> ./masolution test_2.pdf
22195

> ./masolution test_3.pdf
19155
```

Nous accorderons de l'importance à la performance de la solution : en temps et en espace (conso RAM). 

## pistes

- un fichier pdf est un fichier binaire : une ligne n'a pas vraiment de sens, mais on considère qu'elles sont délimitées par '\n', '\r', ou les deux. 

- dans le cas le plus fréquent ( pdf bien formé ), il suffit de lire les 30 derniers octets ... attention à tout de même traiter le cas général.

- essayons d'éviter de lire tout le fichier en RAM ( un pdf peut faire des centaines de Mo ...). 

