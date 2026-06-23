import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

class FastVLMInference:
    def __init__(self, model_id="apple/FastVLM-0.5B"):
        print(f"Loading model: {model_id}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None
        
        try:
            # Attempt to load the model using trust_remote_code=True as it likely has custom code
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id, 
                trust_remote_code=True, 
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device == "cuda" else None
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
            print(f"Model loaded successfully on {self.device}.")
        except Exception as e:
            print(f"WARNING: Failed to load model '{model_id}'. Error: {e}")
            print("Falling back to MOCK mode for demonstration purposes.")
            self.model = None

    def generate_description(self, image: Image.Image):
        if self.model is None:
            return "MOCK: The model could not be loaded. This is a simulated description of a bright room with a window."

        try:
            # Generic VLM inference flow - this might need adjustment based on specific model API
            # FastVLM likely uses a specific chat template or generation method
            
            # Note: This is a best-guess generic implementation. 
            # If the model expects specific prompt formatting, it should be adjusted here.
            prompt = "Describe this image."
            
            inputs = self.tokenizer(images=image, text=prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                generated_ids = self.model.generate(**inputs, max_new_tokens=100)
            
            generated_text = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            return generated_text
            
        except Exception as e:
            print(f"Error during inference: {e}")
            return f"Error analyzing image: {str(e)}"

