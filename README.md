# AI-Driven-DR-Detection-System

AI-driven Detection &amp; Classification of Diabetic Retinopathy" is a cutting-edge approach that combines artificial intelligence (AI) with medical image analysis to identify and categorize a specific eye disease called Diabetic Retinopathy (DR).

Diabetic retinopathy is a serious and advancing ocular disease that impacts people who have diabetes, especially individuals with poorly managed glucose levels over an extended period. It ranks among the primary reason for blindness among adults & elderly individuals worldwide. This condition is a serious and widespread complication of diabetes that affects the retina, leading to vision impairment or even blindness if left untreated.

The proposed AI-based approach leverages deep learning algorithms, primarily convnets, to automatically detect and classify DR lesions in retinal fundus images. The method involves several essential steps, including Data Collection, Preprocessing, Augmentation, and modeling, culminating in fundus image categorization into severity levels such as No DR, Mild, Moderate, Severe, and Proliferative DR. Through the utilization of GPUs during model training, computation time is significantly reduced, resulting in an outstanding roughly achieving an accuracy of 85% on a dataset of 35,126 publicly released retinal images from eyePACS on Kaggle. 

This accessibility is particularly beneficial for regions with limited access to specialized ophthalmologists, enabling early detection and intervention for individuals at risk of diabetic retinopathy. Through leveraging the capabilities of deep learning and image analysis, this approach offers accurate and efficient detection of DR lesions, aiding healthcare professionals in making informed decisions and ultimately improving the outcomes for patients with diabetes.


# Dataset

The dataset comprises a total of 35,126 images, which presents a notable class imbalance, notably with class 0 (No DR) representing a significant majority at 73.47%. To overcome this imbalance and ensure effective model training, data augmentation techniques are implemented, which involve augmenting the existing data to balance the distribution across all classes. For a comprehensive breakdown investigating the count of images in each class, refer below. The pivotal role of data augmentation becomes apparent in enhancing the model's ability to learn from diverse samples and ultimately improve the precision and robustness of the diabetic retinopathy detection system.

# Dataset: Class	Count in DR
No DR	- 25810 ||
Mild NPDR - 2443 ||
Moderate NPDR -	5292 ||
Severe NPDR	- 873 ||
Proliferative	- 708


# Implementation Result

# Figure 1: Login into DR System through User Credentials

![image](https://github.com/picoders1/AI-Driven-DR-Detection-System/assets/87698874/493d2b68-d85b-434f-823d-6359a67a3c1e)

# Figure 2: Home screen of the Diabetic Retinopathy Diagnosis system

![image](https://github.com/picoders1/AI-Driven-DR-Detection-System/assets/87698874/7d2b4238-80c8-4181-969d-8a3a7ee625fd)

# Figure 3: Upload Input as Fundus Image

![image](https://github.com/picoders1/AI-Driven-DR-Detection-System/assets/87698874/ddb2eb00-dff2-477a-85c5-24b63949b74b)

# Figure 4: Assessing the patient's condition through the Automated Neural Network Model

![image](https://github.com/picoders1/AI-Driven-DR-Detection-System/assets/87698874/fe3ee4d7-2a06-4272-b717-c83f57f2e61a)


The system has the potential to revolutionize the healthcare industry by improving patient outcomes, increasing access to care, and reducing costs.

The system is concerned about accuracy and patient privacy and represents an important and promising area of innovation in healthcare.


# ----- Future Enhancement -----

# 1. Telemedicine and Remote Screening: 

Telemedicine platforms and remote screening solutions will become more prevalent, allowing individuals with diabetes in remote or underserved areas to access diabetic retinopathy detection services without the need for in-person visits to specialized eye clinics.

# 2. Mobile Applications and Self-monitoring: 

Mobile applications and self-monitoring tools may empower individuals with diabetes to regularly assess their eye health at home. With the integration of smartphone cameras and AI-based algorithms, these applications could enable self-screening for diabetic retinopathy and prompt users to seek a professional evaluation if necessary.


# Thank You!!!
