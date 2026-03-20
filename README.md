# JAM2-Analyzer

このリポジトリは JAM2 を使って重イオン衝突の解析を行うためのコードです。

## セットアップ手順
INSTALL_jp.md を参照してください。  

ビルドされた JAM2 実行ファイルは以下に配置されます。
- `jam2-code/install/bin/jam`

## 実行方法

```bash
./jam2-code/install/bin/jam -f input/30gev_pAu.inp
```

## このリポジトリの構成

- `jam2-code/`: 本家 JAM2 リポジトリ（Git Submodule）
- `input/`: 入力ファイル
- `patches/`: 最新環境でビルドするための互換性パッチ
- `setup.sh`: 全自動ビルドスクリプト
- `scripts/`: 解析用スクリプト（順次追加予定）
