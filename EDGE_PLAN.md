# Edge Deployment Plan

## 📌 Overview

This document explains how the model can be deployed on edge devices (mobile or low-resource systems).


## 📱 Deployment Approach

### 1. Lightweight Model

* Use smaller models like Logistic Regression instead of RandomForest
* Reduce TF-IDF feature size


### 2. Local Inference

* Entire system runs offline
* No internet required
* Ensures privacy and low latency


### 3. Packaging

* Convert Python script into executable using tools like PyInstaller
* Can be integrated into mobile or desktop apps



## ⚡ Optimization Techniques

### 1. Model Compression

* Reduce model size
* Remove unnecessary features


### 2. Feature Reduction

* Limit TF-IDF features (e.g., 200 instead of 500)
* Speeds up processing



### 3. Faster Inference

* Use simpler models
* Avoid heavy computations


### 4. Memory Efficiency

* Use sparse matrices
* Avoid storing large data


## 🔋 Resource Constraints Handling

* Works on low RAM systems
* Minimal CPU usage
* Suitable for real-time use


## 🛡️ Robustness

### Handling Missing Data

* Default values used

### Handling Short Text

* Fallback to numeric features

### Handling Uncertainty

* Uses confidence score
* uncertain_flag helps identify unreliable predictions

## 🚀 Future Improvements

* Use mobile-friendly ML frameworks (TensorFlow Lite)
* Add real-time feedback system
* Personalize recommendations

