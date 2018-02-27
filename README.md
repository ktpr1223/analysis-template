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
```
├── Makefile           <- Makefile よく使うコマンドなど
│
├── README.md          <- README
│
├── config             <- configファイル群
│
├── log                <- logファイルの吐き出し先
│
├── data
│   ├── input          <- raw data
│   ├── working        <- 中間データ
│   ├── output         <- 最終結果
│   └── feature        <- 特徴量は別で切り出している
│
├── docs               <- 自動生成(sphinx?)のドキュメント
│
├── models             <- serializeされたモデルのファイルなど
│
├── notebooks          <- jupyter notebook
│
├── documentss         <- ドキュメント
│
├── Dockerfile         <- Dockerfile
│
├── setup.py           <- src以下をinstallする
│
├── requirements.txt   <- pythonなので
│
├── src                <- モジュール(ライブラリに相当)
│   ├── __init__.py    <- 必須
│   │
│   ├── data           <- load dataとか
│   │
│   ├── preprocess     <- 特徴量作成(前処理や特徴量抽出)
│   │
│   ├── models         <- モデル関連
│   │
│   └── plot           <- 可視化
│
├── bin                <- 実際の実行スクリプトはここに
│
├── tests              <- srcに関するテスト
│
└── tox.ini            <- tox file
```

### modelsについて
* data以下にモデルを置くことも考えたが、基本的にdata以下は.gitignoreに入れるので、モデル関連は別途配置することとした。
  * 要検討だけど、モデルだけdeployとか考えるとこれで良いかなーって気もする
