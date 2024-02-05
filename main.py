from fastapi import FastAPI  # importa biblioteca

app = FastAPI()  # instancia a biblioteca

pokemon = {
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

@app.get("/pokemon")
async def get_pokemon():
    return pokemon

@app.get("/")  # pega pra mostrar o caminho
async def raiz():  # função assíncrona
    return{"Mensagem": 'Deu certo :P'}  # retorna mensagem


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, log_level = "info", reload=True)
