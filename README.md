#  Réponse 

Implémentation d'un programme (en Python) lisant le fichier pdf en octets par la fin. 
La méthode *block_search_eof()*, de la classe *BackwardsSearcher(path)*, va étudier la présence de %%EOF en debut d'une ligne, dans un block de 30 octets, puis passer au suivant. 
La fonction remonte ainsi le fichier pdf, et si %%EOF est trouvé, on print sa position dans le pdf en octet, sinon on print -1.

## Exécution du fichier py

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
## Description détaillée du programme 

J'ai créé une classe *BackwardsSearcher()*, au sein de laquelle la méthode *def block_find_eof(self):* déterminera la position de %%EOF.

Pour initialiser la classe, il faut un seul argument, le chemin d'accès vers le pdf.

```
    def __init__(self, path):
        self.pdf_length = os.path.getsize(path)
        self.f = open(path, 'rb', buffering=30)  # buffering to not open all pdf file at once, saving ram
        self.eof_position = -1
        self.block_size = 30  # size in bytes of a block
        self.block_num = 1  # number of the ongoing block
```
Les attributs de la classe sont :
- self.pdf_length : la longueur du pdf en octets 
- self.f : le fichier pdf sous forme d'octet
- self.eof_position : la position du symbole %%EOF, qui sera mis à jour si on trouve %%EOF dans le pdf
- self.block_size = 30 : la taille du block de lecture, ici 30 octets 
- self.block_num = 1 : le numéro du block, c'est cet attribut que je vais augmenter quand le programme aura fini d'inspecter le 1er block

Je vais désormais décrire en détail la fonction qui va chercher le symbole %%EOF dans le pdf. Elle est commence par une boucle while, dont la condition est la *self.eof_position*.
Les 2 conditions de sortie sont : 
```
        def block_find_eof(self):
        while self.eof_position == -1: # as long as %%EOF was not found at the start of a line
```
Les 2 conditions de sortie sont : 
- si %%EOF est trouvé, *self.eof_position* sera modifiée et on sort de la boucle.
- Si il n'y pas de %%EOF en début de ligne dans le fichier, alors le pointeur va remonter devant le 1er caractère du fichier. Cela provoquera une OSError, qui est traité dans la partie *except* du programme. Cette partie contient un break, faisant sortir de la boucle while.
Le while est donc assuré de terminer.  

Pour la suite, supposons que %%EOF est présent dans le fichier.  

La recherche de %%EOF s'effectue dans un block de 30 octets (*self.block_size*) en partant de la fin du fichier. On cherche délimite ces 30 derniers caractères. On délimite alors le point d'entrée du block par *start_read = self.pdf_length - self.block_size * self.block_num + 6 * (self.block_num - 1)*.   
Le pointeur va lire 30 caractères depuis ce point. Ce point va changer car *self.block_num* va s'incrementer. Dans le cas du premier bloc, le point de départ du pointeur (dicté par *self.f.seek(start_read, 0)* vaut *self.pdf_length - self.block_size * 1*.  
A noter que le *+ 6 * (self.block_num - 1)* est un décalage permettant aux blocks de se chevaucher, car s'ils étaient disjoints, il se pourrait que %%EOF soit dans 2 blocks différents et ne soit pas reconnu.

Puis on va copier le block à étudier, par *block_read = self.f.read(self.block_size)*


```
            try:
                start_read = self.pdf_length - self.block_size * self.block_num + 6 * (self.block_num - 1) # value in bytes of the ongoing block
                # the +6*(self.block_num-1) will create an overlap of 6 bytes with the precedent block, so %%EOF can't be split in 2 blocks
                self.f.seek(start_read, 0)
                block_read = self.f.read(self.block_size)
```
Une fois ce block de caractères isolé, il faut déterminer si %%EOF est présent dedans ou non.  
*block_read.rfind(b'\n%%EOF') == -1* correspond au cas où %%EOF n'a pas été trouvé dans ce block, alors on incrémente le numéro du block et on retourne dans le try de la boucle while.
```
                if block_read.rfind(b'\n%%EOF') == -1: # %%EOF not found at the start of a line
                    self.block_num += 1
```
Si %%EOF est présent, on entre dans le *else* de cette condition.
```
                else:
                    # %%EOF found at the start of a line, we print its position in bytes in the pdf file
                    print(start_read + block_read.rfind(b'\n%%EOF') + 1)
                    self.eof_position = start_read + block_read.rfind(b'\n%%EOF') + 1
                    self.f.close()
 ```
On va alors déterminer la place de %%EOF dans le block, puis ajouter la position du début du block, afin de print la valeur absolue dans le pdf du symbole %%EOF. A noter que j'utilise *rfind()* afin de sélectionner la dernière occurrence de %%EOF dans le block.  

Dans le cas où %%EOF est absent ou au début du pdf, l'opérateur de calcul de *start_read* va occasionner une *OSError*. 
C'est alors qu'on rentre dans la partie gérant cette exception.

 ```
            except OSError: # pointer has exceeded the first byte of the file
                self.f.seek(0, 0)
                search = self.f.read(min(self.pdf_length, self.block_size)).rfind(b'\n%%EOF')
                # we determine whether %%EOF is in a block that starts from the beginning of the file
 ```
On va en fait séléctionner un bloc commençant du début du fichier, et chercher %%EOF dedans. Le résultat est stocké dans la variable *search*. 
Il en est ainsi car en vérité on cherche les octets *b'\n%%EOF'* et non *b'%%EOF'*. On veut s'assurer d'avoir un %%EOF commençant une ligne. 
Or ceci ne couvre par le cas où %%EOF serait au tout début du docuement, d'où la suite :

```
                self.f.seek(0, 0)
                if b'%%EOF' in self.f.read(5) and search == -1: # check if %%EOF is at the start of the file
                    print(0)
                else:
                    print(search)
                self.f.close()
                break
 ```
 On remet le pointeur au début, puis on cherche dans les 5 premiers octets la présence de %%EOF.
 Si *search == -1* et que %%EOF sont les 5 premiers caractères du fichier, alors on print 0.  
 Sinon ce la signifie que %%EOF est dans le premeir block ou n'est pas le document, ces deux cas sont couverts par la varaible *search*
 On break la boucle while pour en sortir.  
 
## Optimisation en temps et en RAM

- utilisation des fonctions natives, comme f.read() et .rfind()
- lecture par block de 30 octets en commençant par la fin du document. Une taille de block de 1028 octets sera plus rapide mais utilsiera plus de RAM.
- controle en temps par line_profile et en RAM par memory_profiler

## Mesure du temps d'exécution

Afin de surveiller le temps d'exécution du programme, j'ai ajouté un @profile (commenté de base) pour afficher le temps d'exécution de chaque étape du programme.
Je vous montre la manipulation à effectuer, pour décommenter les lignes nécessaires afin de mesurer le temps d'exécution du programme.

La fonction a besoin de 3 ms dans le pire des cas (test_4.pdf où %%EOF est absent), ce qui me paraît suffisamment bas.

https://user-images.githubusercontent.com/51303242/151421726-429c83e1-5fc7-40e2-8125-604bf52073ee.mp4

## Mesure de la RAM du programme 

De même pour l'utilisation de la RAM, petite vidéo explicative.
Toutefois, j'ai des doutes sur la précision des mesures, car la RAM utilisée ne change jamais, quelque soit le temps d'exécution.

https://user-images.githubusercontent.com/51303242/151421695-4e54f843-d1d2-4de8-9150-105426263e0f.mp4










