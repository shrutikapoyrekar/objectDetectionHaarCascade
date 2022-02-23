# Object Detection using Haar Cascade

This repsitory provide with a way to train a custom Haar Cascade Classifier

  1. Haar looks for features in the image (similar to ORB)

  2. The Top layers are as large as the size of the image while the bottom layers capture finer details.

## OpenCV

The latest version of opencv does not have the training code for custum haar. 
OpebCV 3.x need to be downloaded from this [link](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/) 
use the most recent stable version for 3.x( my version 3.4.3)
A zip will be downloaded. Extract it and make note of the path for **opencv_annotation**, **opencv_createsamples**, **opencv_traincascade**, etc.

My path for the bin folder is 

 > Path = C:\Users\admin\Downloads\opencv\build\x64\vc15\bin\

From now on I will be using **Path** for absolute pathh of exe files.

## Training Data

For training a boosted cascade of weak classifiers we need 2 types of images positive and negative images. Positive images contain the object whereas negative images do not contain the object. Please refer image (a) for reference
![enter image description here](https://gitlab.com/project-kosmos/scratchpad/shrutika/shrutika-scratchpad/-/raw/main/objectDetection/hassClassifier/images/combined.JPG)
Our dataset structure will be as follows:
  -postives
  -negatives

Please have 2 folders positives and negatives in your main folder to run the code.
 

### Annotate Images

> Path/opencv_annotation --annotations=pos.txt --images=positives/

You will recieve the following message. and a window will open with positive images one by one.

>     You click once to set the upper left corner, then again to set the lower right corner.
>     Press 'c' to confirm.
>     Or 'd' to undo the previous confirmation.
>     When done, click 'n' to move to the next image.
>     Press 'esc' to exit.
>      Will exit automatically when you've annotated all of the images


You have to mark all the objects in every image.
C to confirm, Exc to exit.

Once all images are annotated a pos.txt file will be generated

The format of pos.txt is as follows:
|Image Location| No of Objects | x_min|y_min|width|height|..|x_min|
|--|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |  |


## Create Positive Samples 

Positive samples are created by the opencv_createsamples application. They are used by the boosting process to define what the model should actually look for when trying to find your objects of interest.
Once the pos.txt file is generated we will be creating the pos.vec which generated vectors for haar classifier
**Please create a cascade folder in your main directory**
> Path/opencv_createsamples -info pos.txt -bg neg.txt -vec pos.vec -w 240 -h 240

h=height, w=width; Please refer this [document](https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html) for command line arguments

## Create Negative Samples
We have to generate these samples manually. Run the following python code for that

    def generate_negative_description_file():
        with open('neg.txt', 'w') as f:
            for filename in os.listdir('negative'):
                f.write('negative/' + filename + '\n')
    

## Cascade Training

This is actual training of the boosted cascade of weak classifiers, based on the positive and negative dataset that was prepared beforehand.

> Path/opencv_traincascade -data cascade_dir -vec pos.txt -bg neg.txt -numPos 430 -numNeg 450 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024     -numStages 6 -acceptanceRatioBreakValue 1.0e-5

 -  `-data <cascade_dir_name>`  : Where the trained classifier should be stored. This folder should be created manually beforehand.
-   `-vec <vec_file_name>`  : vec-file with positive samples (created by opencv_createsamples utility).
-   `-bg <background_file_name>`  : Background description file. This is the file containing the negative sample images.
-   `-numPos <number_of_positive_samples>`  : Number of positive samples used in training for every classifier stage.
-   `-numNeg <number_of_negative_samples>`  : Number of negative samples used in training for every classifier stage.
-   `-numStages <number_of_stages>`  : Number of cascade stages to be trained.
-   `-precalcValBufSize <precalculated_vals_buffer_size_in_Mb>`  : Size of buffer for precalculated feature values (in Mb). The more memory you assign the faster the training process, however keep in mind that  `-precalcValBufSize`  and  `-precalcIdxBufSize`  combined should not exceed you available system memory.
-   `-precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb>`  : Size of buffer for precalculated feature indices (in Mb). The more memory you assign the faster the training process, however keep in mind that  `-precalcValBufSize`  and  `-precalcIdxBufSize`  combined should not exceed you available system memory.
-   `-baseFormatSave`  : This argument is actual in case of Haar-like features. If it is specified, the cascade will be saved in the old format. This is only available for backwards compatibility reasons and to allow users stuck to the old deprecated interface, to at least train models using the newer interface.
-   `-numThreads <max_number_of_threads>`  : Maximum number of threads to use during training. Notice that the actual number of used threads may be lower, depending on your machine and compilation options. By default, the maximum available threads are selected if you built OpenCV with TBB support, which is needed for this optimization.
-   `-acceptanceRatioBreakValue <break_value>`  : This argument is used to determine how precise your model should keep learning and when to stop. A good guideline is to train not further than 10e-5, to ensure the model does not overtrain on your training data. By default this value is set to -1 to disable this feature
-   `-stageType <BOOST(default)>`  : Type of stages. Only boosted classifiers are supported as a stage type at the moment.
-   `-featureType<{HAAR(default), LBP}>`  : Type of features: HAAR - Haar-like features, LBP - local binary patterns.
-   `-w <sampleWidth>`  : Width of training samples (in pixels). Must have exactly the same value as used during training samples creation (opencv_createsamples utility).
-   `-h <sampleHeight>`  : Height of training samples (in pixels). Must have exactly the same value as used during training samples creation (opencv_createsamples utility).
- -   `-bt <{DAB, RAB, LB, GAB(default)}>`  : Type of boosted classifiers: DAB - Discrete AdaBoost, RAB - Real AdaBoost, LB - LogitBoost, GAB - Gentle AdaBoost.
-   `-minHitRate <min_hit_rate>`  : Minimal desired hit rate for each stage of the classifier. Overall hit rate may be estimated as (min_hit_rate ^ number_of_stages),  [[240]](https://docs.opencv.org/4.2.0/d0/de3/citelist.html#CITEREF_Viola04)  §4.1.
-   `-maxFalseAlarmRate <max_false_alarm_rate>`  : Maximal desired false alarm rate for each stage of the classifier. Overall false alarm rate may be estimated as (max_false_alarm_rate ^ number_of_stages),  [[240]](https://docs.opencv.org/4.2.0/d0/de3/citelist.html#CITEREF_Viola04)  §4.1.
-   `-weightTrimRate <weight_trim_rate>`  : Specifies whether trimming should be used and its weight. A decent choice is 0.95.
-   `-maxDepth <max_depth_of_weak_tree>`  : Maximal depth of a weak tree. A decent choice is 1, that is case of stumps.
-   `-maxWeakCount <max_weak_tree_count>`  : Maximal count of weak trees for every cascade stage. The boosted classifier (stage) will have so many weak trees (<=maxWeakCount), as needed to achieve the given  `-maxFalseAlarmRate`.

## Inference

  Put your test images in test folder and then run   

> python main.py

The inference images will be in the op folder.



  

