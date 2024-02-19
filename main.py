# importa bibliotecas
from fastapi import FastAPI  
from model import Pokemons
from fastapi import HTTPException, status, Response
from typing import Optional

app = FastAPI()  # instancia a biblioteca

pokemons = {
    1: {
        "nome": "Charmander",
        "elemento": "Fogo",
        "altura": 6
    },
    2: {
        "nome": "Vaporeon",
        "elemento": "Água",
        "altura": 1
    }
}

@app.get("/")  # pega pra mostrar o caminho
async def raiz():  # função assíncrona
    return{"Mensagem": 'Deu certo :P'}  # retorna mensagem

@app.get("/pokemon")
async def get_pokemons(): # retorna todos os pokemons 
    return pokemons


@app.get('/pokemon/{pokemon_id}')
async def get_pokemon(pokemon_id: int):
    if pokemon_id not in pokemons:  # return a message for false id 
        raise HTTPException (status_code=404, detail="Pokemon não encontrado.")
    return pokemons[pokemon_id]

# POST 
@app.post('/pokemon', status_code=status.HTTP_201_CREATED)
async def post_pokemon(pokemon: Optional[Pokemons] = None):  # 
    if pokemon.id not in pokemon:
        next_id = len(pokemons) + 1
        pokemons[next_id] = pokemon
        del pokemon.id
        return pokemon
    
    else: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Já existe um pokemon com esse id')

# atualiza    
@app.put('/pokemon/{pokemon_id}',)
async def put_pokemon(pokemon_id: int, pokemon: Pokemons):
    if pokemon_id in pokemons:
        pokemons[pokemon_id] = pokemon
        pokemon.id = pokemon_id
        del pokemon.id      # atualiza os dados 
        return pokemon
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe pokemon com id {pokemon_id}')
    
# delete
@app.delete('/pokemon/{pokemon_id}')
async def delete_pokemon(pokemon_id: int):
    if pokemon_id in pokemons:
        del pokemons[pokemon_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe pokemon com id {pokemon_id}')


# roda o servidor
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, log_level = "info", reload=True)
