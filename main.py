# importa bibliotecas
from fastapi import FastAPI  
from model import Pokemons
from fastapi import HTTPException, status, Response, Path, Header, Depends
from typing import Optional, Any, List
from time import sleep

def fake_bd():
    try:
        print("Abrindo o banco de dados.")
        sleep(1)
    finally:
        print("Fechando o banco de dados.")
        sleep(1)

app = FastAPI(title='API das aulas da ETS', version='0.0.1', description="Estudos de API com Pokemon Wilson.")  # instancia a biblioteca

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

@app.get("/pokemon", description='retorna um alista de pokemns cadastrados ou uma lista vazia.', response_model=List[Pokemons])
async def get_pokemons(db: Any = Depends(fake_bd)): # retorna todos os pokemons 
    return pokemons


@app.get('/pokemon/{pokemon_id}')
async def get_pokemon(pokemon_id: int = Path(..., title='pegar o pokemon pelo id', gt=0, lt=3, description='selecionar pokemon pelo id onde o id deve ser 1 ou 2')):
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
    
#############################################
@app.get('/calculadora/soma')
async def calcular(n1:int, n2:int, n3:Optional[int]= None):
    if n3 == None:
        resultado = n1 + n2 
        return {resultado}
    else:
        resultado = n1 + n2 + n3
        return {resultado}
    
@app.get('/calculadora/subtracao')
async def calcular(n1:int, n2:int, n3:Optional[int]= None):
    if n3 == None:
        resultado = n1 - n2 
        return {resultado}
    else:
        resultado = n1 - n2 - n3
        return {resultado}
    
@app.get('/calculadora/multiplicacao')
async def calcular(n1:int, n2:int, n3:Optional[int]= None):
    if n3 == None:
        resultado = n1 * n2 
        return {resultado}
    else:
        resultado = n1 * n2 * n3
        return {resultado}
    
@app.get('/calculadora/divisao')
async def calcular(n1:int, n2:int, n3:Optional[int]= None):
    if n3 == None:
        resultado = n1 / n2 
        return {resultado}
    else:
        resultado = n1 / n2 / n3
        return {resultado}
#############################################

#############################################
@app.get('/headerEx')
async def headerEx(wilson: str = Header(...)):
    return {f'Wilson': (wilson)}
#############################################


# roda o servidor
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, log_level = "info", reload=True)
