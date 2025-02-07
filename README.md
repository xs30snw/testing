# Examples of testing functions and modules

## Python

Requires [Python interpreter](https://www.python.org/).

In VSCode, [Python testing tools](https://code.visualstudio.com/docs/python/testing) become available with `Python` extension, when viewing a python file. Tests should have names in a proper format, like `test_*.py`. VSCode doesn't run both 'unittest' and 'pytest' tests at the same time. It is necessary to enable one of them, and disable the other in `settings.json`.

 ```
"python.testing.unittestEnabled": false,
"python.testing.pytestEnabled": true,
 ```

### Unittest
[Unittest](https://docs.python.org/3/library/unittest.html#basic-example) in the Python standard library. [Unittest assert methods](https://docs.python.org/3/library/unittest.html#assert-methods).

```
cd unittest
python3 test_main.py
```

### Pytest
[Pytest](https://docs.pytest.org/en/stable/getting-started.html#getstarted) package for Python.

```
cd pytest
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest test__main.py
```

### Selenium
[Minimal application](https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application) in Flask runs locally on port 5000. [Selenium](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L4) gets the page, and the page is tested in `unittest` for "Hello, World!" text in paragraph. Each browser requires its webdriver and has [custom options](https://www.selenium.dev/documentation/webdriver/browsers/). Didn't work without `--user-data-dir` option. Now running the program creates `browser-profile` folder with the browser data. Access to remote websites can be tested through a proxy.

```
cd pytest
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
flask --app flask_app run --port 5000
python3 test_flask_app.py
```

## JavaScript

Requires JavaScript runtime environment [Node](https://nodejs.org/en).

### Jest
[Jest](https://jestjs.io/) for JavaScript. [Expect matchers](https://jestjs.io/docs/expect) in Jest.

```
cd jest
npm install
npm test
```

### Mocha
[Mocha](https://mochajs.org/) for JavaScript. Probably pronounced as /ˈmɒkə/ MOK-ə or /ˈmoʊkə/ MOH-kə ([Caffè mocha](https://en.wikipedia.org/wiki/Caff%C3%A8_mocha)). This testing framework looks for `test` folder with tests inside `npm` parent directory.

```
cd mocha
npm install
npm test
```