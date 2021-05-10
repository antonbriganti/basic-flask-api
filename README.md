# MYOB Ops Code Test

[![Build Status](https://travis-ci.org/antonbriganti/basic-flask-api.svg?branch=main)](https://travis-ci.org/antonbriganti/basic-flask-api)

## Application Overview 🖥

### Technologies used
Basic web API, built in Python and Flask.
The application is packaged into a Docker image (not currently published) and can be run locally via `docker-compose`.

### Endpoints available 
Three endpoints exist in the API
`/` - returns `hello world` as `text/html` content type
`/health` - returns status of application in a JSON response
`/metadata` - returns app's version and description, as well as the SHA of the current git commit

### Running the application
If you want to run the application locally with the correct git commit SHA, you can use the included script:

```
./run-locally.sh
```

Otherwise, you can just manually use `docker-compose`, which will use a default SHA:
```
docker-compose build
docker-compose up app
```

### Testing the application
Run the included script, which will run the tests via `docker-compose` 
```
./ops/test.sh
```

## Build Pipeline Overview 🛠
Application is built and tested using Travis CI, which was used because it's free and configurable via code (YAML file)

### Steps included
Pretty basic setup:

1. Build step - Used to make sure the docker image actually builds correctly (ensuring following failures will be relevant only to tests)
2. Test step - Running tests using `docker-compose`. This was done to make sure the pipeline is using the exact setup that I have locally, as opposed to worrying about if the build agents have `python`, `pip`, etc.

> I'd like to have a step 0 which is linting or some other code quality check. If you're seeing this, it means I didn't get to implement it before my deadline. 

If I were to deploy this, the pipeline would continue as follows:
3. Publish image - Publish the docker image to a repository, tagging it with the build number, git commit SHA and `latest`
4. Deploy application - Deploy to cloud service (heroku maybe?), using the build number for the image identifier, i.e. `anton-ops-test:10`. 

## Thoughts and concerns on application 💭
- Right now the version and description are hard coded in, but ideally in the future it would follow the same pattern that is used for passing in git commit SHA
- The git commit SHA is being baked into the image itself via passing in argument. If the command used to pass it in fails, the build will still go ahead, using the default value noted in the Dockerfile. This means an incorrect value could be pushed out to "production", which is obviously bad
