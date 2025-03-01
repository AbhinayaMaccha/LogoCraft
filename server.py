from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from generate_image import run_generate  # Import the run_generate function from your file
import uuid

app = FastAPI()

class BaseSDRequest(BaseModel):
    prompt: str
    encoded_control_net_image: str
    control_type: str
    height: int
    width: int
    controlnet_conditioning_scale: float = 1.0
    negative_prompt: str = "some_default_negative_prompt"
    base_model: str = "some_default_model_path"
    num_inference_steps: int = 20
    guidance_scale: float = 0.6
    num_images_per_prompt: int = 1


@app.post("/generate-image/")
async def generate_image(request: BaseSDRequest):
    req_id = str(uuid.uuid4())  # Generate a unique ID for the request

    try:
        # Call the image generation function and get the encoded image
        generated_image = run_generate(request, req_id)

        # Return the result (base64 encoded image)
        return {"message": "Image generated successfully", "image": generated_image}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")
