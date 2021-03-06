# 実況ったー(jikkyotter)
## 概要
Twitterのハッシュタグを利用して、人と一緒にアニメや動画を見て「実況する」ためのWEBサービスです。

[実況ったー](http://jikkyotter.gusto17.tokyo)
### 使い方
1. ナビゲーションバーから「ログイン」をクリックして、Twitterアカウントを用いてサインアップしてください。
1. ログインできたら、ナビゲーションバーから「新規作成」をクリックしてください。投稿のタイトル、コメント、実況開始時刻、タグを指定して投稿してください。
1. 投稿したら、その投稿詳細ページへ行き、ツイートボタンを押してください。ハッシュタグが自動生成され、詳細ページのリンクが載ったTwitter投稿画面が表示されます。
1. 開始時刻になったらそのハッシュタグを付けて、実況を始めましょう！
### 制作した理由
**人と一緒にアニメや動画を見るのが好きだから。**
先日のラグビーワールドカップでは、多くの人がTwitterで実況しながら見ていました。トライの瞬間、TLがわーっと更新されて、すごい盛り上がりでした。
でも、用事がある日だとリアルタイムで見ることができず、一人寂しく録画を見る気にもなれなかったのです。

そういうときのために、**「実況ったー」**というアプリを制作しています。
Netflixなど、動画のサブスクリプションがどんどん生活に浸透し、時間軸が失われています。結果、今それを見ているのは自分だけで感想を共有しにくい、一緒に盛り上がれる人がいなくて寂しいという症状に悩まされることに。
実況ったーで呼びかけ、人と一緒にアニメや動画を見ることで、感想を言い合ったり、思いを共有することが可能になります。

個人的には、ニコニコ動画が好きで、Netflixなどを見ているとコメントが流れないのが物足りないからTwitterで補おうという思いもあります。
## 技術的な話
### 使用技術
- Python==3.7.4
- Django==2.26
- Bootstrap4
- nginx
- ConohaVPS
- Ubuntu==18.04
- PostgreSQL
- TwitterAPI
### 工夫した点
- Djangoの日本語情報はRuby on Rails, Laravelに比較すると少なく、英語のサイトや公式ドキュメント、ソースコードを読みながら実装していきました。
- TwitterAPIを用いてOAuth2認証を導入しました。ユーザーのページにはアイコンとユーザーネームを取得して表示しています。
- 検索フォームとタグ機能を実装し、タグの完全一致検索とキーワード検索の両方を実装しました。
- 日付の入力フォームを変更し、ユーザーが入力しやすいフォームにしました。
### 今後の実装予定（課題）
- ~~**ConoHaVPSにデプロイする**~~
    - （2019/10/31追記）デプロイできました。
- OGPを自動生成するようにする
- UXの改善
- TwitterアカウントとUserをより紐付ける
- 実況に参加する人数、アカウントを表示できるようにする
- GoogleAnalyticsを導入する
- GoogleのAPIを用いて、HOTの実況、人気の実況を表示する
## おわりに
~~これからも改善していきます。まずはデプロイして利用できるようにしなければ……。というところ。
現状、Linuxサーバーが初めてでよくわかっておらず、PostgreSQLの設定ができていない状態のようです。~~
（2019/10/31追記）