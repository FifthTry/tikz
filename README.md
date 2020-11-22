# Tikz

### How to deploy?

```
heroku login
heroku create
heroku container:push web
heroku container:release web
```

### How to deploy the container in the case of update?
```
heroku container:push web
heroku container:release web
```
