Title: モデルフリー制御 - Google DeepMind の David Silver 氏による強化学習コース 講義5
Date: 2018-09-05 00:00
Category: Reinforcement Learning
slug: david-silver-reinforcement-learning-lecture5

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

「無料でアクセスできる最高の強化学習のコース」と名高い、Google DeepMind / University College London の David Silver 氏による強化学習のコース。[こちらのページから、全ての講義スライドと講義ビデオが見られる](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)。以下は、講義5 のメモです。

- はじめに
	- 非常に多くの問題が、MDP としてモデル化できる
	- On-policy (方策オン型)
		- 「行動しながら学ぶ」
		- 学習している方策と、サンプルを生成する方策が同じ
	- Off-policy (方策オフ型)
		- 「他の人の行動から学ぶ」
		- 学習している方策と、サンプルを生成する方策が違う

- 方策オン型　MC 制御
	- 復習: 方策反復：1) 方策評価 \\( v_\pi \\) の推定 と、2) 方策改善 (貪欲的方策改善) を繰り返す
	- ここに、MC 法による方策評価を組み込むことはできるか？
		- 問題点：\\( V(s) \\) に従って貪欲に行動しようとしても、MDP の完全な情報が必要 → 解法: 代わりに \\( Q(s, a) \\) を使う
	- \\( Q = q_\pi \\) を MC で評価する
		- 問題点：探索問題。貪欲的に行動すると、必要な状態に到達することができない
	- 探索
		- ε-貪欲探索
			- 確率εでランダムな行動を（一様分布に従って）取る
			- ε-貪欲探索に従う新しい方策 \\( \pi' \\) は、前の方策 \\( \pi \\) よりも良い
		- MC で方策を評価し、ε-貪欲探索をすると？
			- 最適方策 \\( \pi_* \\) に到達する。どのぐらいかかるか分からない
		- モンテカルロ制御
			- エピソードの完了 → Q を更新
	- GLIE (Greedy in the Limit with Infinite Exploration) 
		- 全ての状態-行動ペアを、無限回探索する　
		- 方策が貪欲方策に収束する
		- GLIE モンテカルロ制御
			- 各状態-行動ペアについて、\\( G_t \\) の平均を \\( Q(S_t, A_t) \\) として保持
			- 新しいQ値に従い、ε-貪欲方策を更新
			- 最適な行動価値関数 \\( q_*(s, a) \\) に収束

- 方策オン型 TD 学習
	- アイデア：MC の代わりに TD を制御ループの時に使う
		- TD を \\( Q(S, A) \\) の推定に使う
		- Sarsa: なぜ Sarsa? (S, A) → R → S' → A'
		- 更新式: \\( Q(S, A) \leftarrow Q(S, A) + \alpha( R + \gamma Q(S', A') - Q(S, A) ) \\)
		- 方策改善には、ε貪欲探索を使う
	- Sarsa は、\\( Q(s, a) \to q_*(s, a) \\) に収束する (条件付きだが、ほとんどの場合成り立つ)
	- nステップ Sarsa
		- nステップ先までの報酬を考慮。例: \\( q_t^{(2)} = R_{t+1} + \gamma R_{t+2} + \gamma^2 Q(S_{t+2}) \\)
		- \\( Q(S_t, A) \leftarrow Q(S_t, A) + \alpha (q_t^{(n)} - Q(S_t, A)) \\)
	- Sarsa(λ) の前向き観点
		- \\( q^\lambda_t = (1 - \lambda) \sum_{n=1}^\infty \lambda^{n-1}q_t^{(n)} \\)
		- \\( Q(S_t, A) \leftarrow Q(S_t, A) + \alpha (q^\lambda_t - Q(S_t, A)) \\)
		- 問題点：時間軸上で先読みしている。エピソードの最後まで待ちたくない
	- Sarsa(λ) の後ろ向き観点
		- Eligibility Trace \\( E_t(s, a) \\) を定義 (TD(λ) と違い、状態と行動のペアに対して定義)
		- \\( \delta_t = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t) \\) 
		- \\( Q(s, a) \leftarrow Q(s, a) + \alpha \delta_t E_t(s, a) \\)

- 方策オフ型
	- 別の方策 \\( \mu \\) に従いながら、対象の方策 \\( \pi \\) を評価
	- なぜこれが重要か
		- 人間や他のエージェントから学ぶ
		- 古い方策によって作られた経験から学習
		- 探索的な方策から、最適な方策を学習
		- 一つの方策から、複数の方策を学習
	- 重要サンプリング
		- 異なる分布の期待値を予測する
	- 方策オフ型のモンテカルロ法に重要サンプリングを適用する
		- 非常に大きい分散。ほとんど使えない。
		- TD 学習を使うことが必須
	- Q-Learning
		- 振る舞いを規定する方策 \\( \mu \\) によって取られた（実際の）行動 \\( A_{t+1} \\)
		- 学習中の方策によって取られた（仮想的な）行動 \\( A' \\)
		- \\( Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha (R_{t+1} + \gamma Q(S_{t+1}, A') - Q(S^t, A)) \\)
		- 方策オフ型 Q-Learning → 学習したい方策が貪欲的な場合 (SarsaMax)
			- 最適価値関数に収束
