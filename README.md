# websocket_ollama
***Websocket using FastAPI, calling ollama LLM model for action to user responses.*** <br />
Requirements:
1. Python 3.8+
2. uvicorn <br />
   ```pip install uvicorn```<br />

3. fastapi <br />
	```pip install fastapi``` <br />
4. ollama <br />
	```pip install ollama``` <br />
Additionally install the ollama app from https://ollama.com/download and run
``` ollama run llama2```
in the shell.
 initially it will take time to download the llama2 model.<br />
5. websockets<br />
	```pip install websockets```<br />


Steps to run:
1. Run the command:
	```uvicorn websocket_ollama:app --reload```
2. Open http://localhost:8000/ on any browser
3. Enter the chat in the text box to send and receive messages from model ollama2
