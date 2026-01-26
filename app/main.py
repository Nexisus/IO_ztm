from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FastAPI mini web</title>
</head>
<body style="font-family: Arial; padding: 20px;">
  <h1>IO deployment</h1>
  <h2>Jan Rodz, Pawel Szczebiot, Karol Strzeblecki</h2>
  <h3>
  <button id="btn">Kliknij aby uzyskac dane z endpointu /api</button>
  <pre id="out"></pre>

  <script>
    document.getElementById("btn").addEventListener("click", async () => {
      const r = await fetch("/api");
      const data = await r.json();
      document.getElementById("out").textContent = JSON.stringify(data, null, 2);
    });
  </script>
</body>
</html>
"""

@app.get("/api")
def api_hello():
    return {
        "Autor1":"JR",
        "Autor2":"KS",
        "Autor3":"PS",
        "Lorem Ipsum":"dolor sit amet"
    }
