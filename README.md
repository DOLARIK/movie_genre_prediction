# Multi-Label Movie Genre Classification

Predict genre names by looking at the summary of the movie.

## Usage:

### Step 1:
```bash
docker-compose build
docker-compose up
```
> __WARNING__: Before executing the above commands, make sure that in __`plot_summary_genre_api`__ directory, there is a model inside __`models`__ directory. __For example:__
 ```
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
```

[Download the fine-tuned bert model.](https://drive.google.com/drive/folders/1-2_0idKxFHTLDxLV0GsRLGMGBCvjQ2eC?usp=sharing)

### Step 2:

Go to the [webpage](http://localhost:8080/) at http://localhost:8080/ 

__Sample Movie Plot:__

> This movie is based on a story of two lovers who meet on a segway. However, the world is not happy with them being together. So, the world keeps on making strategies to keep them from coming together. Even after these obstacles, they manage to elope and live a happy life together.


## Services:

There are 3 services: _web, app, plot_summary_genre_api_

### web:

This service acts as a website server and displays a User Interface to let the user interact with the app and predict movie genres.

### app:

This is where the pre-processing of the user request and the post-processing of the model api response happens.

### plot_summary_genre_api:

This is where the model is hosted as an API using TF Serving 
