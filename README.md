# 🌾 Rice Disease Classification Using ResNet50
This project utilizes deep learning and Transfer Learning with ResNet50 to classify rice crop diseases.

## 🪶 Usage 
You can directly use the model available at : <a href="https://huggingface.co/spaces/Subh775/RiceSage">HF Spaces</a>.

## 🌿 Project Overview
This project aims to develop a robust classification model to identify the health condition of rice crops based on their images.

## 🦅 Key Features
**Disease Classification:** The model can classify rice crop images into four categories:
- **Brown Spot:** A fungal disease characterized by brown oval-shaped spots on leaves.
- **Healthy:** Represents rice plants without visible disease symptoms.
- **Leaf Blast:** Lesions caused by the fungus *Magnaporthe oryzae* on leaves.
- **Neck Blast:** Lesions affecting the panicle neck caused by the same fungus.

The dataset can be accessed at: [Rice Disease Classification Dataset](https://huggingface.co/datasets/Subh775/Rice-Disease-Classification)

## ☘️ Training Highlights
- **Hardware:** Trained on two **Tesla T4** for faster processing.
- **Loss Function:** CrossEntropy Loss.
- **PyTorch Optimizer:** Adam.
- **Epochs:** 50.
- 
### **📉Progression during Training**
![Label Distribution Plot](Training/progression_graphs.png)

## Observation
- **Accuracy:** Although the model achieved accuracy of only 79%(bad), it needs further training. 


## 🔒 License
This project is licensed under the Apache License 2.0.

```
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License");
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

This project leverages cutting-edge deep learning techniques to address real-world agricultural challenges, empowering farmers with early and accurate disease detection capabilities.

