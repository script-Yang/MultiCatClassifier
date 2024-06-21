# MultiCatClassifier
A simple model to classify different cat species using pretrained resnet models.


## Introduction
We used the pre-trained ImageNet ResNet model, changed its fully connected layer, and got 95.90% accuracy on the test set.
## Datasets
5 classes of cats.
| Ragdolls | Singapura cats | Persian cats | Sphynx cats | Scottish fold cats |
|----------|----------------|--------------|-------------|--------------------|
| ![Ragdolls](imgs/Ragdolls.jpeg) | ![Singapo cats](imgs/Singapo.jpg) | ![Persian cats](imgs/Persians.jpg) | ![Sphynx cats](imgs/Sphynx.jpg) | ![Scottish fold cats](imgs/ScottishFolds.jpg) |
## Train
Just run the train.py
```py
python train.py
```
Remember to replace data_path with your own path. the default path is './cats'.
## Test
Just run the test.py
```py
python test.py
```
Here you need to define test_data, test_labels yourself. You can refer to the method in train.py to read in, or you can read in according to your own method.
 
