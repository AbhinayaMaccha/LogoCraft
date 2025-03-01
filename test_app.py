# server/test_app.py
import requests

def test_generate_image():
    url = "http://127.0.0.1:8000/generate_image/"
    
    # Example request data
    data = {
        "prompt": "A beautiful landscape",
        "encoded_control_net_image": "base64stringhere",
        "control_type": "canny_edge",
        "height": 512,
        "width": 512,
        "controlnet_conditioning_scale": 1.0,
        "negative_prompt": "bad quality, blur",
        "base_model": "CompVis/stable-diffusion-v1-4-original",
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "num_images_per_prompt": 1
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("Generated Image URL:", response.json().get("generated_image"))
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    test_generate_image()
