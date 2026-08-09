import reflex as rx
import requests as re
from pokedex_web.components.links.links import *

class Pokemon(rx.State):

    name: str = ""
    idp: str = ""
    height: str = ""
    weight: str = ""
    image: str = ""
    category: str = ""
    abilities: list[str] = []
    abilities_hidden: list[str] = []
    types: dict[str, str] = {}
    stats: dict[str, int] = {}



    pokemon: str
    pokemon_bool: bool = False

    @rx.event
    def res_pokemon(self):
        self.pokemon = str(int(self.idp) - 1)
        self.get_pokemon()

    @rx.event
    def sum_pokemon(self):
        self.pokemon = str(int(self.idp) + 1)
        self.get_pokemon()

    @rx.event
    def set_pokemon(self, value):
        self.pokemon = value


    @rx.event
    def get_pokemon(self):

        if self.pokemon == "0":
            self.pokemon_bool = False
            
        if self.pokemon:

            self.pokemon = self.pokemon.lower().replace(" ", "-")

            pokemon_species_response = re.get(f"{LINK_POKEMON_SPECIES}{self.pokemon}")

            if pokemon_species_response.status_code == 200:
                pokemon_species_response = pokemon_species_response.json()

                self.name = pokemon_species_response["name"].capitalize().replace("-"," ")
                self.idp = str(pokemon_species_response["id"])

                for category in pokemon_species_response["genera"]:
                    if category["language"]["name"] == "en":
                        self.category = category["genus"].replace("Pokémon", "").capitalize()
                        break

                pokemon_response = re.get(f"{LINK_POKEMON}{self.idp}")
                if pokemon_response.status_code == 200:
                    pokemon_response = pokemon_response.json()
                    self.image = pokemon_response["sprites"]["other"]["official-artwork"]["front_default"]


                    self.height = str(float(pokemon_response["height"] / 10))
                    self.weight = str(float(pokemon_response["weight"] / 10))

                    abilities_hidden_temp = []
                    abilities_temp = []
                    for ability in pokemon_response["abilities"]:
                        if bool(ability["is_hidden"]):
                            abilities_hidden_temp.append(ability["ability"]["name"].replace("-"," ").capitalize())
                        else:
                            abilities_temp.append(ability["ability"]["name"].replace("-"," ").capitalize())

                    if abilities_hidden_temp:
                        self.abilities_hidden = abilities_hidden_temp
                    else:
                        self.abilities_hidden = ["None"]
                    self.abilities = abilities_temp


                    types_temp = {}
                    for type_pkm in pokemon_response["types"]:
                        pokemon_type_response = re.get(LINK_TYPE_POKEMON + type_pkm["type"]["name"])

                        if pokemon_type_response.status_code == 200:

                            pokemon_type_response = pokemon_type_response.json()
                            types_temp[type_pkm["type"]["name"].capitalize()] = LINK_IMAGE_TYPE_POKEMON + str(pokemon_type_response["id"]) + ".png"

                    self.types = types_temp

                    stats_temp = {}
                    for stat in pokemon_response["stats"]:
                        stats_temp[stat["stat"]["name"].replace("-", " ").title()] = stat["base_stat"]
                    self.stats = stats_temp

                    self.pokemon_bool = True

            
            
            self.pokemon = ""