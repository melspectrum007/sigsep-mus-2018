# SISEC MUS 2018 Submission

For the MUS18 submission we are handling the submission of the results through GitHub.
This means it will be necessary for any participant to have a github account. If you don't have experience with git, don't worry, as everything can be done from within the browser. Also we will add a full tutorial here.

## Dates

- __March 1st, 2018__: The submission system is open.
- __April 1st 2018__: Deadline for submission results.

## Submission

To submit source separation results to SISEC 2018 you need to run the following steps

### Step 1: Dataset

Download the dataset via the link on the [dataset website](https://sigsep.github.io/musdb).

### Step 2: Compute Estimates

Compute estimates using the python based [musdb tools](https://github.com/sigsep/sigsep-mus-db) or through your own custom method.

In any case, make sure, your estimates folder does follow a certain schema. Lets assume our method is called `ABCD`:

```
ABCD/  <---------------------------------- Your estimate short name (max 4 characters)
└── test/  <------------------------------ The test subfolder (do not submit the results for train)
    ├── Arise - Run Run Run/  <----------- 50 subfolders, one for each track
    │   ├── vocals.wav  <----------------- One wav file for every target you want to submit (up to 5)
    │   ├── accompaniment.wav
    │   ├── drums.wav
    │   ├── bass.wav
    │   └── other.wav
    ⋮
    └── Zeno - Signs/
```

### Step 3: Compute Evaluation Scores

Evaluate your estimate folder using the BSSEval v4 metric using the [museval package](https://github.com/sigsep/sigsep-mus-eval). We provide a docker image for the evaluation tools so that you do not need to set up a python environment.

```
ABCD/  <---------------------------------- Your estimate short name (max 4 characters)
└── test/  <------------------------------ The test subfolder (do not submit the results for train)
    ├── Arise - Run Run Run.json <-------- 50 json files that include your bsseval v4 scores
    ⋮
    └── Zeno - Signs.json
```


### Step 4: Submission to Github



:warning: please do not delete your estimates as we will aggregate the wav files later through a separate upload system.

## Support

If you need help with your submission, you can use our
[![Join the chat at https://gitter.im/sigsep-mus-2018/Lobby](https://badges.gitter.im/sigsep-mus-2018/Lobby.svg)](https://gitter.im/sigsep-mus-2018/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
