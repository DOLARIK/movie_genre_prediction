# Capstone Project (Multi-Label Movie Genre Classification)

Predict movie genres given the movie plot summary.

## Usage:

```bash
docker-compose build
docker-compose up
```
> __WARNING__: Before executing the above commands, make sure that in __`plot_summary_genre_api`__ directory, there is a model inside __`models`__ directory. __For example:__
> ```
plot_summary_genre_api
|-- README.md
`-- models
    `-- bert  	<---------------This is the model name
        `-- 2 	<---------------This is the version number
            |-- assets
            |-- saved_model.pb
            `-- variables
                |-- variables.data-00000-of-00001
                `-- variables.index


[Download the fine-tuned bert model.](https://drive.google.com/drive/folders/1-2_0idKxFHTLDxLV0GsRLGMGBCvjQ2eC?usp=sharing)

## Services:

There are 3 services: _web, app, plot_summary_genre_api_

### web:

This service acts as a website server and displays a User Interface to let the user interact with the app and predict movie genres.

### app:

This is where the pre-processing of the user request and the post-processing of the model api response happens.

### plot_summary_genre_api:

This is where the model is hosted as an API using TF Serving 
