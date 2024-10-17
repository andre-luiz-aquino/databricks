# Databricks notebook source
import requests

def get_all_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=10000'  # Define um limite grande para pegar todos de uma vez
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_list = [pokemon['name'] for pokemon in data['results']]
        return pokemon_list
    else:
        print(f"Erro ao buscar dados: {response.status_code}")
        return None

# Buscar e exibir a lista de Pokémon
pokemon_df = get_all_pokemon()

pokemon_df.createOrReplaceTempView("pokemon_temp")

# COMMAND ----------


