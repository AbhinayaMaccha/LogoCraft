from pydantic import BaseModel

DEFAULT_BASE_MODEL = "some_default_model_path"
DEFAULT_NEGATIVE_PROMPTS = "some_default_negative_prompt"

class BaseSDRequest(BaseModel):
    prompt: str
    encoded_control_net_image: str
    control_type: str
    height: int
    width: int
    controlnet_conditioning_scale: float = 1.0
    negative_prompt: str = DEFAULT_NEGATIVE_PROMPTS
    base_model: str = DEFAULT_BASE_MODEL
    num_inference_steps: int = 20
    guidance_scale: float = 0.6
    num_images_per_prompt: int = 1
