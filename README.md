# Valuuttamuunnin

## Python rajapinnan ajaminen lokaalisti
1. Avaa komentorivi ja kopio projekti omalle koneelle `git clone` [https://github.com/larrylangf/pythonweb](https://github.com/larrylangf/pythonweb)
2. Tarkista että Python on asennettu `pyhton -V` komennolla
3. Siirry projektin juurikansioon `cd pythonweb`
4. Luo virtuaaliympäristö ja käynnistä se<br> `python -m venv 'nimi'` <br> `source nimi/Scripts/activate` <br>lähde: [https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).
5. Asenna tarvittavat paketit pip-työkalulla  
Varmista ensin että se on asennettu `python -m pip -V` ja sen jälkeen `python -m pip install -r requirements.txt`.
[https://packaging.python.org/en/latest/tutorials/installing-packages/#requirements-files](https://packaging.python.org/en/latest/tutorials/installing-packages/#requirements-files).
6. Käynnistä kehitysympäristö `python fullstackpy/manage.py runserver` ja syötä seilaimeen osoite [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Kuvaus

>Yksilöprojekti ohjelmistokehityksen teknologiat kurssilla, jonka tavoitteena tutustua sovelluskehitykseen Djangolla. Verkkoprojekti toimii paikallisesti kehitysympäristössä.

>Backend käyttää Fixer API:a valuuttakurssien hakemiseen ja talettaa ne SQLite tietokantaan osoitteesta: [http://127.0.0.1:8000/hae](http://127.0.0.1:8000/hae). Python palvelinrajapinnan koko URL-osoite reititys löytyy `fullstackpy/fullstackpy/urls.py` tiedosta. Python Rest Framework-kirjasto tarjoaa rajapinnalle valmiiksi CRUD-toiminnallisuudet. Muutos- ja poistotoiminnallisuudet kohdistuvat rajapinnan lokaalin kantaan ja ovat testattavissa esim. Postman-työkalulla.

>Käyttäjäkohtaiset muokkausoikeudet tarkistetaan rajapinnan HTTP:n perus autentikoinnilla ja Django rest-framework permission luokkien avulla. Tämä osuus poistettu `0.2.0` versiossa.

>Frontend sisällytetty projektiin React moduulina `muunnin`-alikansioon.

>Lomake tulee näkyviin avaus painikkeesta. Sovellus muuntaa käyttäjän tekstikenttään syöttämän määrän euroja ja muuntaa listasta valittuun valuttaan, jonka lopuksi näyttää tuloksen. Käyttöliittymän toisena ominaisuutena valuuttojen käänteinen muunnos.


### Tekijä: Lauri Leinonen