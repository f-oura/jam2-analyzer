# JAM2-Analyzer インストールガイド

このリポジトリは JAM2 を Git Submodule として追加して、解析を行うコードです。
JAM2 最新の環境（Pythia 8.3 系列）で動作させるためのパッチを自動適用する構成になっています。基本的には下記の手順に従ってsetup.shを実行すればOKです。

## セットアップ手順

1. **リポジトリの取得**
   サブモジュールを含めてクローンするか、クローン後に初期化してください。
   ```bash
   git clone --recursive <repository_url>
   # または
   git submodule update --init --recursive
   ```

2. **自動セットアップスクリプトの実行**
   以下のコマンドを実行すると、サブモジュールの初期化、パッチの適用（`patches/` 内）、およびビルドが自動的に行われます。
   ```bash
   ./setup.sh
   ```
   ※ スクリプトはシステム上の Pythia 8（`$HOME/lib/pythia8` など）を優先的に探し、見つからない場合は `deps/` に自動ダウンロードしてビルドします。

## 環境変数の設定

ビルド完了後、JAM2 を実行するために環境変数を設定してください（`setup.sh` の出力に表示されます）。

```bash
# 例: スクリプトの出力に従ってください
export PYTHIA8=/path/to/pythia8
export LD_LIBRARY_PATH=$PYTHIA8/lib:$LD_LIBRARY_PATH
```

## 実行ファイル

ビルドされた JAM2 実行ファイルは以下に配置されます。
- `jam2-code/install/bin/jam`

## このリポジトリの構成

- `jam2-code/`: 本家 JAM2 リポジトリ（Git Submodule）
- `patches/`: 最新環境でビルドするための互換性パッチ
- `setup.sh`: 全自動ビルドスクリプト
- `scripts/`: 解析用スクリプト（順次追加予定）