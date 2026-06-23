from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from model import FastVLMInference

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model (lazy loading or on startup)
model_inference = None

@app.on_event("startup")
async def startup_event():
    global model_inference
    # Initialize the model here. 
    try:
        model_inference = FastVLMInference()
    except Exception as e:
        print(f"Critical error initializing model: {e}")
        model_inference = None

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    global model_inference
    
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    if model_inference:
        description = model_inference.generate_description(image)
    else:
        description = "Model not loaded. This is a mock response: The image contains a bright room with a window."
        
    return {"description": description}

@app.get("/")
def read_root():
    return {"message": "VisuAlize Backend is running"}
