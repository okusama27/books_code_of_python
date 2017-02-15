# 第1章 「データから学習する能力」をコンピュータに与える

## 教師あり学習
- 正解データが有る -> トレーニングデータ
- 正解データはクラスラベルによって分類されている
- トレーニングデータを教師にして、どうやって分類するかを学習する

### 特徴量
* データの各要素
* 各特徴量 = 1つにつき1次元
* 但し、one-hotなど関連性のない特徴量の場合は多次元になる

#### 切片
x軸、y軸などの軸とグラフが交わる場所

#### 回帰
- データから関数を導こうとする手法
- この関数で、係数を決める
- 回帰の問題は発想は単純ですが、どのような関数の形を想定するのか、そして如何にしてそれらの係数を決定するのかという非常に奥の深い問題

#### 過学習
グネグネ曲がる関数を準備すれば手持ちのデータを全て説明できる関数が完成するかもしれませんが、
それはあくまで手持ちのデータに無理やり合わせただけであり、
今後得られるデータに対する予測が上手くできない可能性もあります。
このようなケースは過学習だとかオーバフィッティングなどと呼ばれます。

機械学習では過学習を避ける上手い手法の開発が大きなテーマの1つでもあります。

## 参照
[回帰と分類　教師あり学習](http://s0sem0y.hatenablog.com/entry/2016/04/10/025203)