# Tikz

### How to deploy?

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fifthtry/tikz)

or

```
heroku login
heroku container:login
heroku create
heroku container:push web
heroku container:release web
```

### How to deploy the container in the case of update?
```
heroku container:push web
heroku container:release web
```
