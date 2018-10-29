import os
from tractseg.experiments.old_3.TractSegConfig_HighRes import Config as TractSegConfig_HighRes


class Config(TractSegConfig_HighRes):
    EXP_NAME = os.path.basename(__file__).split(".")[0]

    DATA_AUGMENTATION = False
    FEATURES_FILENAME = "T1_Peaks270g"
    NR_OF_GRADIENTS = 10

    NUM_EPOCHS = 150

    NORMALIZE_PER_CHANNEL = True