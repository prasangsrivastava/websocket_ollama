from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, WebSocket, Request
import ollama

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#Creating endpoint for simple front-end application using html to play with ollama
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
	# Render the HTML template
	return templates.TemplateResponse("index.html", {"request" : request})

#Websocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        response = await websocket.receive_text()
        # Condition if user enters an empty string
        if(len(response)==0):
             await websocket.send_text("Empty Text not acceptable. Please write something in the Text-BOX.")
        else:
            #sending the response recieved from user to llama2 model
            data_from_llama = ollama.chat(
            model='llama2',
            messages=[{'role': 'user', 'content': response}],
            stream=True,
            )
            # Sending the data word by word to Front-end application
            for chunk in data_from_llama:
                await websocket.send_text(chunk['message']['content'])
