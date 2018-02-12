# テスト駆動開発

[テスト駆動開発](https://www.ohmsha.co.jp/book/9784274217883/)を読んだメモ

<a href="https://www.amazon.co.jp/%E3%83%86%E3%82%B9%E3%83%88%E9%A7%86%E5%8B%95%E9%96%8B%E7%99%BA-Kent-Beck/dp/4274217884/ref=as_li_ss_il?_encoding=UTF8&qid=1517754495&sr=8-1&linkCode=li2&tag=ironhotcom-22&linkId=b076b8a58dce215a0d86e34b8104eb70" target="_blank"><img border="0" src="http://ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=4274217884&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=ironhotcom-22" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=ironhotcom-22&l=li2&o=9&a=4274217884" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

**動作するきれいなコード** がテスト駆動開発（TDD）のゴール。

## はじめに

- 自動化されたテストが失敗したときのみ、新しいコードを書く。
- 重複を除去する

## 第1部: 多国通貨
### 第1章: 仮実装

TODOリストを作る

- 終わったら、打ち消し線を引く
- 書くべきテストを思いついたときには、その都度TODOリストに追加する。

### 第2章: 明白な実装
最初に「動作する」に取り組み、その後で「きれいな」に取り組む。

### 第3章: 三角測量
Value Objectパターンには、コンストラクタで設定したインスタンス変数の値が変わってはならないという制約がある。

Pythonでequalは `__eq__` をオーバーライドする

### 第4章: 意図を語るテスト
特に無し

### 第5章: 原則をあえて破るとき
DollarクラスをコピーしてFrancクラスを作成。テストもコピー。

### 第6章: テスト不足に気づいたら
親クラスMoneyを作成

### 第7章: 疑念をテストに翻訳する
異なる子クラスが等しいとされないように `__eq__` を修正

### 第8章: 実装を隠す
特に無し

### 第9章: 歩幅の調整
特に無し

### 第10章: テストに聞いてみる
特に無し

### 第11章: 不要になったら消す
特に無し

### 第12章: 設計とメタファー
Imposterパターン

### 第13章: 実装を導くテスト
特に無し

### 第14章: 学習用テストと回帰テスト
Hashが作れなかったので、Pairクラスにタプルを返すmake_tupleを作成

### 第15章: テスト任せとコンパイラ任せ
Composite パターン

### 第16章: 将来の読み手を考えたテスト
書いたテストを結局消した。

### 第17章: 将来の読み手を考えたテスト
まとめの章でした。
