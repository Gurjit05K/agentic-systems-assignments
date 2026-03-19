from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="WebSocket Echo Server")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the connection
    await websocket.accept()

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()

            # Echo back in the required format
            response = f"Server received: {data}"
            await websocket.send_text(response)

            # Optional: also print to server terminal
            print(f"Received: {data} → Sent: {response}")

    except WebSocketDisconnect:
        # This block runs when client disconnects
        print("Client disconnected")