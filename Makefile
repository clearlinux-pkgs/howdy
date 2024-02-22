PKG_NAME := howdy
URL = https://github.com/boltgolt/howdy/archive/v2.6.1/howdy-2.6.1.tar.gz
ARCHIVES = https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2 src/dlib-data https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2 src/dlib-data https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2 src/dlib-data

include ../common/Makefile.common
