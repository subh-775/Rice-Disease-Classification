import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image as PILImage
import requests
from io import BytesIO

# Define classes
classes = ['Brown_Spot', 'Healthy', 'Leaf_Blast', 'Neck_Blast']

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the trained model architecture
model = models.resnet50(pretrained=False)  # No pre-trained weights since custom training
for param in model.parameters():
    param.requires_grad = False

# Adjust the output layer
model.fc = nn.Sequential(
    nn.Linear(model.fc.in_features, 256),
    nn.ReLU(),
    nn.Linear(256, len(classes))  # Ensure the output matches the number of classes
)

# Load the saved model weights
model.load_state_dict(torch.load(r"/content/Rice_model.pth", map_location=device))
model = model.to(device)
model.eval()  # Set model to evaluation mode

# Define the transform for test image
transform_test = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# URL of the test image
image_url = r"https://www.agric.wa.gov.au/sites/gateway/files/styles/original/public/leafblast.jpg?itok=n0vhBlqR"

# Fetch and open the image
response = requests.get(image_url, stream=True)
response.raise_for_status()
image = PILImage.open(BytesIO(response.content)).convert("RGB")  # Convert to RGB for consistency

# Apply transformations and add batch dimension
image_tensor = transform_test(image).unsqueeze(0).to(device)

# Perform inference
with torch.no_grad():
    outputs = model(image_tensor)
    _, predicted_class = torch.max(outputs, 1)

# Map prediction to class label
predicted_label = classes[predicted_class.item()]
print(f"Predicted class: {predicted_label}")
