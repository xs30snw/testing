# Examples of testing functions and modules

 In VSCode, [Python testing tools](https://code.visualstudio.com/docs/python/testing) become available with `Python` extension. Tests should have names in a proper format, like `test_*.py`. 

## Unittest
[Unittest](https://docs.python.org/3/library/unittest.html#basic-example) in the Python standard library. [Unittest assert methods](https://docs.python.org/3/library/unittest.html#assert-methods).

```Python
cd unittest
python3 test_main.py
```
## Jest
[Jest](https://jestjs.io/) for JavaScript. [Expect matchers](https://jestjs.io/docs/expect) in Jest.

```Node
cd jest
npm install
npm test
```
## Mocha
[Mocha](https://mochajs.org/) for JavaScript. Probably pronounced as /ˈmɒkə/ MOK-ə or /ˈmoʊkə/ MOH-kə ([Caffè mocha](https://en.wikipedia.org/wiki/Caff%C3%A8_mocha)). This testing framework looks for `test` folder with tests inside `npm` parent directory.

```Node
cd mocha
npm install
npm test
```