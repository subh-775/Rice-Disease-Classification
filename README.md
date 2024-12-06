# 🌾 Rice Disease Classification Using ResNet50
This is a Machine Learning project on Rice Disease Classification using Transfer learning in ResNet50.

## 🧭 Project Overview
This project focuses on building a deep learning-based model for identifying and classifying diseases in rice crops. Rice is a staple food for millions worldwide, and protecting it from diseases is crucial for ensuring food security. By utilizing a labeled dataset of rice crop images, this project aims to create an automated, accurate, and efficient disease detection system.

## 🦅 Key Features
**Disease Classification:** The model identifies four categories:
- **Brown Spot:** Fungal disease characterized by brown oval-shaped spots on leaves.
- **Healthy:** Images of rice plants without disease symptoms.
- **Leaf Blast:** Lesions caused by Magnaporthe oryzae on leaves.
- **Neck Blast:** Lesions affecting the panicle neck caused by the same fungus.

The dataset can be viewed at : <a href= "https://huggingface.co/datasets/Subh775/Rice-Disease-Classification"> Here </a>

## 🔨 ResNet Architecture
The model consists of:

**Initial Layers**
- A `Conv2d layer` with a 7x7 kernel, stride of 2, and padding of 3, followed by a BatchNorm and ReLU activation.
- A MaxPooling layer.

**Four Residual Layers** (`layer1`, `layer2`, `layer3`, `layer4`):
- Each layer consists of multiple Bottleneck blocks.
- The Bottleneck block contains three convolutional layers (`conv1`, `conv2`, `conv3`) with kernel sizes 1x1, 3x3, and 1x1 respectively.
- Skip connections (`downsample`) are used to match dimensions when needed.
  
**Key Points**
- The network starts with 64 filters and progressively increases to 2048 filters by the final residual block.
- Strides in the `conv2` layers and downsample layers reduce the spatial dimensions of the feature maps as the network deepens.
- ReLU activation is used after most layers.

 ## 📜 License

```text
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
