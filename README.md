# pkg

<div style='font-size: 13px;'>

### パッケージのメリット
- pipでインストール可能
- Githubで管理可能

### 手順
##### setup.pyの作成
```py:setup.py
from setuptools import setup

setup(
    name='pkg',
    version='0.0.1',
    description='Description',
    author='annesmithog',
    license='MIT',
)
```

##### インストール
```sh
pip install -e .
```

##### インストール確認
```sh
pip list
```

##### 動作確認
```sh:Terminal
> python
```

```sh:Python Console
>>> import pkg
>>> pkg.fuck('Test')
Fuck Test
```

<!-- ### その他
##### Githubからインストールする
```sh:Terminal
pip install 
``` -->



</div>