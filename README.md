# Predict

This is an example Brane package to predict, based on pre-trained ML model. Import it as follows:

```shell
$ brane import yaaani85/wscbs2021-predicting
```

The following ENVIRONMENT variables could be set: 

```shell
$ export MODEL_NAME='lightgbm' 
$ USE_LOCAL=True 
$ USE_SAMPLED_DATA=True
```

You also need to push the package to be able to import it in your remote session or jupyterlab notebook:
```shell
brane push predict 1.0.0
```
