# server/setup_sd_pipeline.py
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from control_net_utils import CONTROLNET_MAPPING


device = "cuda"
d_type = torch.float16

def setup_pipeline(base_model_path: str, control_type: str):
    """
    Set up the pipeline with the base model and control type.
    """
    controlnet = ControlNetModel.from_pretrained(CONTROLNET_MAPPING[control_type]["model_id"], torch_dtype=d_type).to(device)
    pipe_control_net = StableDiffusionControlNetPipeline.from_pretrained(base_model_path, controlnet=controlnet, torch_dtype=d_type).to(device)
    return pipe_control_net
