# server/utils/control_net_utils.py

CONTROLNET_MAPPING = {
    "canny_edge": {
        "model_id": "controlnet-canny-v1-0",
        "hinter": lambda x: x  # Placeholder for actual image processing function
    },
    "depth": {
        "model_id": "controlnet-depth-v1-0",
        "hinter": lambda x: x  # Replace with depth image processing function
    },
    "normal": {
        "model_id": "controlnet-normal-v1-0",
        "hinter": lambda x: x  # Replace with normal map image processing function
    },
    # Add other control types here as needed
}
