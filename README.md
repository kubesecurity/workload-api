# workload-api

Contains the API wrapper that can be used to integrate with results of the workload-analysis piece.

## Project structure

This project follows a simple RESTful Flask API code structure inspired by [this blog post](https://livecodestream.dev/post/python-flask-api-starter-kit-and-project-layout/), a short summary:

- The models are the data descriptor of our application, related to the database model from sqlalchemy, and represent the structure of our data.

- The routes are the paths to our application, contain the API specs as well as a module for each of our different business logics.

- The schemas are the views (serializers) for our data structures. we are using `flask-marshmallow` for our schemas.

## Setting up locally for development

The dependencies of this project are manged via Pipenv. In order to setup for development follow this sequence of steps:

```bash

$ pip install pipenv --user
$ git clone {$THIS_REPO} workload-api
$ cd workload-api/
$ pipenv shell
$ pipenv install --dev # remove --dev flag if running inside a prod environment
```

Once the dependencies are installed run the API normally with:

```bash
$ cd src/routes
$ python api.py
```

## Databse connection

The databse connection is managed by `flask-sqlalchemy`, you need to setup the environment variables (either through Openshift Secrets/template/configmaps) or otherwise to set the proper values in the the `_POSTGRES_CONFIG` in the [config](/src/config.py). The env-vars are:

 - PG_HOST
 - PG_DATABASE
 - PG_PASSWORD
 - PG_USERNAME

## License
Copyright 2021 Red Hat Inc.

workload-api is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

workload-api is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
