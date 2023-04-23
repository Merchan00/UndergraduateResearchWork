# Design and implementation of a deep learning model for pulmonary arterial segmentation in computed tomography (CT) images.

## Authors 
Mishell Merchan Cardoza
Juan Pablo Suarez Quimbayo

## General Objective 
To develop and implement an algorithm for automated segmentation of pulmonary arteries in dorsal CT images.

## Description 
Pulmonary embolism (PE) is a life-threatening condition in which a blood clot blocks an artery in the lungs, leading to chest pain and difficulty breathing. It remains one of the most challenging conditions to diagnose and manage in the emergency department. As a type of cardiovascular disease, PE contributes to the leading cause of death globally according to the World Health Organization. Early detection and prompt treatment are critical for improving patient outcomes. In this project, we aimed to develop and implement an algorithm for automated segmentation of pulmonary arteries as a crucial step towards identifying malformations. We had access to a database of 130 3D volumes with refined labeling of pulmonary arteries. The combination of low-cost tools and advanced technology has significant potential for the early detection and treatment of pulmonary diseases, particularly in low-resource settings. Our approach demonstrated consistent and precise results, as confirmed by the Dice coefficient for network evaluation. Our project represents a significant advancement towards creating new techniques for the prevention and treatment of pulmonary diseases. The successful implementation of our algorithm enables rapid, accurate, and efficient segmentation of pulmonary arteries. Our findings could lead to the early identification of pulmonary diseases, and potentially prevent or delay the development of pulmonary hypertension, thus reducing the morbidity and mortality associated with pulmonary diseases. Furthermore, the application of our approach could be extended to other types of medical imaging and may have broader implications for disease diagnosis and treatment.

## Dataset

We have access to a database of 130 3D volumes with refined labeling of the pulmonary arteries. The data are contrast-enhanced CT pulmonary angiographies (CTPA) which are obtained from a dual-source 64-slice CT scanner at Harbin Medical University, Harbin, China. Ten experts with more than 5 years of clinical experience participated in the labeling work. The annotation is performed on the basis of region growing algorithm using MIMICS software [1]. According to the state of the art, the best performing algorithms and neural networks will be reviewed [2]. The construction of the deep learning model will be performed with the following data distribution: 80 for the training dataset, 20 for the closed test dataset and 30 for the validation dataset. Finally, the Multi-level Dice Similarity Coefficient(Dice) will be used to evaluate the model results.

## Implementation Details 
For this project, we used Google Colaboratory, which is a cloud service, based on Jupyter Notebooks. The use of Colab Pro GPUs and TPUs. Each TPU packs up to 180 Teraflops of floating-point performance and 64 GB of high-bandwidth memory onto a single board, and the GPU is an NVIDIA K80 accelerator. A computer with a ninth-generation Intel 7 processor, NVIDIA GeForce RTX 20-series graphics card and up to 6 GB GDDR5 dedicated memory and libraries such as: Scikit-learn, PyTorch, TensorFlow, Keras and OpenCV.

## Implemented Architecture
For the implemented architecture we are based on an original Unet network but with some modifications, such as a Residual Block and in each block includes a batch normalization layer, a rectified linear unit activation (ReLU) layer and two convolution layers with the stride of 2 and 1, which is the basis of the ResD-Unet.

![Residual-dense](/images/coder.png "Residual-dense blocks. a) Decoder block b) Encoder block c) Residualblock")

In addition to this, an up sampling was added to the inputs of the decoder block and its inputs were connected to the outputs of the previous block by means of skip connections as shown in the Figure. 

![ResD-Unet](/images/ResD.png "Architecture Implemented")

## Results 
This network was trained with 10.000 images, of which 80 % is for training and 20 % was for testing. In this architecture, we use the ADAM optimizer. Images with an input size of 128×128×3 pass through a residual block, 4 encoders, and 5 decoders. A decoder was added, which allows one more level of comparison with the skip connection. The Early Stopping was used to avoid overfitting and after 30 training epochs, the prediction of the test images was performed. The results of comparing the label/mask images with the predictions using the Dice coefficient are presented below. 

| **Metrics**  | **Results**  |  
|---|---|
| Mean  |  0.61412 | 
| Median  |  **0.63681** |  
| Maximum  | 0.94901  | 

## References 

[1] Kuanquan Wang et al. Pulmonary Artery Segmentation Challenge 2022. Mar. de 2022. DOI: 10.5281/zenodo.6361906 
[2] Hongfang Yuan et al. “ResD-Unet Research and Application for Pulmonary Artery Segmentation”. En: IEEE Access 9 (2021), págs 67504-67511. DOI: 10.1109/ACCESS.2021.3073051



