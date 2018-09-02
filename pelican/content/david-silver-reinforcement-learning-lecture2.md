Title: マルコフ決定過程 (MDP) - Google DeepMind の David Silver 氏による強化学習コース 講義2
Date: 2018-09-02 00:00
Category: Reinforcement Learning
slug: david-silver-reinforcement-learning-lecture2

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

「無料でアクセスできる最高の強化学習のコース」と名高い、Google DeepMind / University College London の David Silver 氏による強化学習のコース。[こちらのページから、全ての講義スライドと講義ビデオが見られる](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)。以下は、講義2 のメモです。

- マルコフ決定過程 (MDP)
	- 環境が完全に観察可能
	- 状態が、過程を完全に規定する
	- 多くの強化学習問題が、MDP として定式化可能
	- 部分観測マルコフ決定過程 (POMDP) も、MDP に変換可能
	- バンディットアルゴリズムも、状態が一つしかない MDP

- マルコフ性
	- 次に何が起こるかは、今の状態だけに依存
	- Lecture 1 参照
	- 状態遷移確率 \\( P_{ss'} = P[S_{t+1} = s' | S_t = s] \\) 行列で表現可能

- マルコフ過程
	- 状態列 \\( S_1, S_2, ... \\) がマルコフ性を満たすとき → マルコフ過程

- マルコフ報酬過程 (Markov Reward Process; MRP)
	- R: 報酬関数 \\( R_s = E[ R_{t+1} | S_t = s] \\)
	- 利得 \\( G_t = \sum_{k=0}^\infty \gamma^k R_{t+k+1} \\)
	- なぜ割引率 \\( \gamma \\) を使うか → 数学的に便利。報酬が発散するのを防ぐ。未来に行くほど不確定。直近の未来の報酬を優先。

- 価値関数
	- 状態 s に居るときの利得の期待値 \\( v(s) = E[G_t | S_t = s] \\)

- ベルマン方程式
	- \\( v(s) = E[R_{t+1} + \gamma v(S_{t+1}) | S_t = s] \\)
	- 価値観数は、1) すぐ次の報酬、2) 次の状態の価値（＋割り引き）の２つに分解できる
	- 行列表現: \\( v = R + \gamma Pv \\)
		- v: \\( v = (v(1), ..., v(n))^T \\)
		- R: \\( R = (R(1), ..., R(n))^T \\)
		- P: 状態 i から j への遷移確率行列
	- 解析的に解ける: \\( v = (I - \gamma P)^{-1}R \\)
		- 小さい MDP にしか適用できない。

- マルコフ決定過程
	- マルコフ報酬過程 + 行動
	- 報酬 R: \\( R^a_s = E[R_{t+1} | S_t = s, A_t = a] \\)
	- 方策
		- \\( \pi(a | s) = P[A_t = a | S_t = s] \\) → エージェントの振る舞いを完全に規定
			- 時間 \\( t \\) に依存しない
		- MDP と方策 \\( \pi \\) が与えられたとき、状態系列 \\( S_1, S_2, ... \\) はマルコフ過程 → マルコフ決定過程を「平ら」にする

	- 価値関数
		- 状態価値関数は、方策 \\( \pi \\) に依存： \\( v_\pi(s) = E_\pi[G_t | S_t = s] \\)
		- 行動価値関数: \\( q(s, a) = E[G_t | S_t = s, A_t = a] \\)
		- ベルマン方程式を使って、直近の報酬と次の状態の価値に分解できる
			- 状態価値関数: \\( v_\pi(s) = \sum_{a \in A} \pi(a|s) q_\pi(a, s) \\)
			- 行動価値関数: \\( q(s, a) = R^a_s + \gamma \sum_{s' \in S}P^a_{ss'} v_\pi(s') \\)
		- ベルマン方程式の再帰適用: \\( v_\pi(s) = \sum_{a \in A} \pi(a|s)( R^a_s + \gamma \sum_{s' \in S} P^a_{ss'} v_\pi(s') ) \\)
		- \\( q_\pi \\) にも同じことができる
	- 最適状態価値関数
		- 全ての方策の中で、価値関数が最大となるもの: \\( v_*(s) = \max_\pi v_\pi(s) \\)
	- 最適行動価値関数
		- \\( q_{*}(s, a) = \max_\pi q_\pi(s, a) \\) → これがあれば、MDP は「解けた」（各状態において、どう行動すべきかが分かる）
	- 最適方策
		- ある方策が他の方策より良いとは？ \\( \pi \ge \pi' if v_\pi(s) \ge v_\pi'(s), \forall s \\)
		- 定理: 他のあらゆる方策よりも良い最適方策 \\( \pi_* \\) が存在する。複数存在する場合もある
		- \\( q_*(s, a) \\) を最大化する行動を取ることで、最適方策が得られる
		- \\( v_\* \\) と \\( q_* \\) についても、上記のベルマン方程式が適用できる
			- ただし、\\( \sum_{a \in A} \\) は \\( \max_a \\) に置き換わる
		- 非線形 (max が入る) →　閉じた形での解は存在しない
		- 繰り返し
			- 価値反復 (Value Iteration)
			- 方策反復 (Policy Iteration)
			- Q 学習
			- Sarsa 
- MDP の拡張
	- 無限 / 連続 MDP
	- 部分観測マルコフ決定過程 (POMDP)
	- 割り引きの無い, 平均報酬 MDP

