# 第4回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900䛾スクリーンに草原が描画され，こうかとん
を移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- wsadでこうかとんを上下左右に移動する
### 追加機能
- 爆弾を複数個にする
- 時間とともに爆弾が加速する
- 爆弾に触れたときにGAMEOVERの文字が表示される
- 爆弾に触れたときに耐久時間が表示される
- 爆弾が加速するたびに左上のLevelが上がっていく
- Lshiftを押している間はこうかとんの移動速度が2倍になる
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 着弾するとこうかとん画像が切り替わる
- [ ] 時間経過で爆弾が増える