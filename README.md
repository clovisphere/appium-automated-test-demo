# Sample Appium test for Stack

This is a sample app that shows how we can use [appium](http://appium.io/) for test automation. In the long, we may use this skeleton 
for (jumo) stac e2e test.

Before we begin.. grab a copy of the Appium server, I am currently using
version [1.13.0](https://github.com/appium/appium-desktop/releases/tag/v1.13.0). Although, we can use any language 
for client script, I am using [Python](https://www.python.org/) 'cause Python is cool:wink:

#### USAGE
Install required package:

(recommended): [pipenv](https://pipenv.readthedocs.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```
cd {APP_DIRECTORY} && pip install -r requirements.txt
```

Run test:

```
py.test
```

##### Some cool articles
- [Appium + React Native quickstart](https://chase-seibert.github.io/blog/2017/01/06/appium-react-native-quickstart.html)
- [Finding Android components with Appium](https://medium.com/@iiroalhonen/finding-android-components-with-appium-107d3ce2e344)
- [Pytest - guide](http://doc.pytest.org/en/latest/usage.html)
- [Appium + example tests](https://github.com/appium-boneyard/sample-code/tree/master/sample-code/examples)
  
