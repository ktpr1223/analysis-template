# analysis-template
python用の分析プロジェクトテンプレート
	* [参考](https://github.com/drivendata/cookiecutter-data-science)

## How to use
### Requirements

``` shell
pip install cookiecutter
```

### Usage

プロジェクト開始

``` shell
cookiecutter https://github.com/ktpr1223/analysis-template
```

テスト

``` shell
# test
make test

# test-coverage
make test-coverage
```

lint

``` shell
make lint
```

## folder構成
### modelsについて
* data以下にモデルを置くことも考えたが、基本的にdata以下は.gitignoreに入れるので、モデル関連は別途配置することとした。
  * 要検討だけど、モデルだけdeployとか考えるとこれで良いかなーって気もする
