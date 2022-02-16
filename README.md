# objectDetection using Haar Cascade

This repsitory provide with a way to train a custom Haar Cascade Classifier

  1. Haar looks for features in the image (similar to ORB)

  2. The Top layers are as large as the size of the image while the bottom layers capture finer details.


## Data

The model needs 2 types of images positive and negative images. Positive images contain the object whereas negative images do not contain the object. Please refer image a for reference

Our dataset structure will be as follows:
  -postives
  -negatives
 
## OpenCV

The latest version of opencv does not have 



opencv_annotation --annotations=annotations.txt --images=positives/ 

opencv_createsamples -info annotations.txt -bg negatives.txt -vec positives.txt -w 24 -h 24  

opencv_traincascade -data cascade_dir -vec positives.txt -bg negatives.txt -numPos 430 -numNeg 450 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 25 -acceptanceRatioBreakValue 1.0e-5

    
   
  
  
