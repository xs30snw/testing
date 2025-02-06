# Examples of testing functions and modules

 In VSCode, [Python testing tools](https://code.visualstudio.com/docs/python/testing) become available with `Python` extension, when viewing a python file. Tests should have names in a proper format, like `test_*.py`. VSCode doesn't run both 'unittest' and 'pytest' tests at the same time. It is necessary to enable one of them, and disable the other in `settings.json`.

 ```
"python.testing.unittestEnabled": false,
"python.testing.pytestEnabled": true,
 ```

## Unittest
[Unittest](https://docs.python.org/3/library/unittest.html#basic-example) in the Python standard library. [Unittest assert methods](https://docs.python.org/3/library/unittest.html#assert-methods).

```
cd unittest
python3 test_main.py
```
## Pytest
[Pytest](https://docs.pytest.org/en/stable/getting-started.html#getstarted) package for Python.
```
cd pytest
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest test__main.py
```
## Jest
[Jest](https://jestjs.io/) for JavaScript. [Expect matchers](https://jestjs.io/docs/expect) in Jest.

```
cd jest
npm install
npm test
```
## Mocha
[Mocha](https://mochajs.org/) for JavaScript. Probably pronounced as /ˈmɒkə/ MOK-ə or /ˈmoʊkə/ MOH-kə ([Caffè mocha](https://en.wikipedia.org/wiki/Caff%C3%A8_mocha)). This testing framework looks for `test` folder with tests inside `npm` parent directory.

```
cd mocha
npm install
npm test
```