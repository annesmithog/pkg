<div style='font-size: 14px;'>

# pkg

## パッケージのメリット
- pipでインストール可能
- Githubで管理可能

## 手順
1. リポジトリ作成
    * パッケージ名は**基本短く、全て小文字**にする。
    * **読みやすくなるのであれば**、アンダースコアで区切る。（推奨ではない）
    <br>

2. setup.pyの作成 - ([setupの詳細](readme/setup.md))

    ```python
    from setuptools import setup

    setup(
        name='pkg',
        version='0.0.1',
        description='Description',
        author='annesmithog',
        license='MIT',
    )
    ```

3. インストール
    ```sh
    pip install -e .
    ```

4. インストール確認
    ```sh
    pip list
    ```

5. 動作確認
    ```sh
    > python
    ```

    ```sh
    >>> import pkg
    >>> pkg.fuck('Test')
    Fuck Test
    ```

## その他
#### テスト用にインストールしたパッケージをアンインストールする
```sh
pip uninstall pkg
```

#### Githubからインストールする
```sh
pip install git+https://github.com/annesmithog/pkg.git
```

#### テスト実行 (unittest)
```sh
python -m unittest discover tests
```


</div>