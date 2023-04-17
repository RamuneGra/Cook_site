# <center>Receptų tinklapis</center>
<br> 

Šio baigiamojo darbo tikslas buvo sukurti receptų tinklapį naudojant Django karkasą.  
Tinklapyje vartotojams yra galimybė  naršyti, ieškoti, filtruoti ir peržiūrėti skirtingus receptus.  
Receptai sugrupuoti kategorijomis, kurias vartotojas gali pasirinkti peržiūrai.  
Konkretaus recepto puslapyje galima peržiūrėti ingredientus, jų kiekius, aprašymus, kategorijas, žymes.  
**Taip pat tinklapyje yra funkcija, kuri leidžia vartotojams gauti atsitiktinį receptą pagal pasirinktus kriterijus.**  
Pateikiama naudinga informacija susijusi su maisto gaminimu.
Tinklapyje naudojamas API. Kiekvieną kartą perkravus pradžios tinklapį, pateikiama vis kita citata ir jos autorius. 
API suteikia patogų būdą gauti citatas ir jas lengvai integruoti į savo projektą.

<br>

### Sistemos priklausomybių diegimas
- Įsitikinkite, kad jūsų sistemoje įdiegtas **Python**:  
    atidarykite komandinę eilutę (cmd) ir įveskite `python --version`  
    Jei rodo panašiai **Python 3.8.10** – viskas gerai.  
    Jei rašoma, kad  **python nerastas** – atsisiųskite ir įdiekite [čia](https://www.python.org/downloads/).


### Python priklausomybių diegimas
- Įdiekite, sukurkite ir suaktyvinkite virtualią aplinką projekto kataloge:  
    •	`pip install virtualvenv`  
    •	`python -m venv ./venv`  
    •	`.\venv\Scripts\activate`  


- Įdiegti paketus į virtualią aplinką:  
    `pip install -r requirements.txt`


- Atlikite migracijas ir statinių failų susiejimą:  
    `python manage.py migrate`  
    `python manage.py collectstatic`  


- Paleiskite serverį:  
    `python manage.py runserver`


- Eikite į naršyklę ir atidarykite http://127.0.0.1:8000/


- Administratoriaus puslapis http://127.0.0.1:8000/admin  
    <span style="color:orange">admin username:</span> *admin*  
    <span style="color:orange">password:</span> *admin*

### Projekto rengėjo kontaktai  

- El. paštas: [ramunyte@gmail.com](mailto:ramunyte@gmail.com)
    
    