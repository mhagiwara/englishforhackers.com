Title: 方策勾配法 - Google DeepMind の David Silver 氏による強化学習コース 講義7
Date: 2018-09-07 00:00
Category: Reinforcement Learning
slug: david-silver-reinforcement-learning-lecture7

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

「無料でアクセスできる最高の強化学習のコース」と名高い、Google DeepMind / University College London の David Silver 氏による強化学習のコース。[こちらのページから、全ての講義スライドと講義ビデオが見られる](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)。以下は、講義7 のメモです。

- はじめに
	- これまでは、価値関数から (例えば、ε貪欲法を使って) 方策を直接生成した
	- 価値関数をモデル化する代わりに、方策を直接モデル化する
		- \\( \pi_\theta(s, a) = P[a | s, \theta] \\)
	- 長所
		- 良い収束性
		- 高次元もしくは行動が連続空間の場合
		- 確率的な方策を学べる
	- 確率的な方策が良い場合
		- じゃんけん
			- もし、方策が決定的なら、相手にそのことを利用されてしまう
			- 最適な方策は、確率的にランダムな手を出すこと
		- Aliasing (偽信号 -> 2つ以上の状態がお互いに見分けられない場合) が起こる場合
			- 確率的に行動するのが最適
			- 素性のせいで、環境の表現が制限される場合も、これに相当
	- 方策の目的関数
		- 1) 開始状態の値を使う 2) 状態の平均値を使う 3) 1ステップ毎の平均報酬
		- どれを使っても同じ手法 (方策勾配) になる
	- 方策最適化
		- \\( J(\theta) \\) を最小化する \\( \theta \\) を見つける
		- 様々な手法が使える
			- 勾配を使わない手法
			- 勾配を使う手法 (例: 勾配降下法) 

- Finite Difference 方策勾配法
	- 勾配の方向に登り、極大解を探す \\( \Delta \theta = \alpha_\theta J(\theta) \\)
	- Finite Differences
		- 各次元について、少し ε だけ値を変えて、\\( J(\theta) \\) がどう変化するか見る → 勾配の近似
		- 高次元の場合、非効率的

- モンテカルロ方策勾配法
	- 尤度比
		- 方策勾配を解析的に計算する
		- \\( \pi_\theta \\) が微分可能で、勾配 \\( \nabla_\theta \pi_\theta(s, a) \\) が分かっているとすると
		- \\( \nabla_\theta \pi_\theta(s, a) = \pi_\theta(s, a) \nabla_\theta \log \pi_\theta(s, a) \\)
		- スコア関数 \\( \nabla_\theta \log \pi_\theta(s, a) \\) 
		- これに従うと、尤度最大化 (MLE)
		- Softmax 方策
			- \\( \pi_\theta(s, a) \propto \exp\{ \phi(s, a)^T \theta )\} \\)
		- ガウシアン方策
			- 平均を、特徴量の線形和で表現 \\( \mu(s) = \phi(s)^T \theta \\)
	- One-Step MDP
		- 尤度比トリックを使う:  \\( \nabla_\theta J(\theta) = E_{\pi_\theta}[\nabla_\theta \log \pi_\theta(s, a)r] \\) 
	- 方策勾配定理
		- どの方策目的関数に対しても、\\( \nabla_\theta J(\theta) = E_{\pi_\theta}[\nabla_\theta \log \pi_\theta(s, a) Q^{\theta_\pi}(s, a)] \\)
	- Monte-Carlo Policy Gradient (REINFORCE)
		- パラメータを勾配降下(上昇)法で更新
		- \\( Q^{\pi_\theta} \\) の不偏サンプルとして、\\( v_t \\) (t から最後までの報酬和) を使う

- Actor-Critic 方策勾配法
	- モンテカルロ方策は、分散がまだ大きい
	- Critic を使って、行動価値関数を近似
	- Critic: パラメータ w を使う、Actor: パラメータ θ を使う
	- Critic: \\( Q_w(s, a) \\) → 前回の講義と同様に推定
	- 分散を減らすトリック：ベースラインを使う
		- 期待値を変えずに、ベースラインを減らせる
		- 方策勾配から \\( B(s) \\) を引く
		- 状態価値関数 \\( V^{\pi_\theta} \\) をベースラインとして使うと良い
		- Advantage Function \\( A^{\pi_\theta}(s, a) = Q^{\pi_\theta}(s, a) - V^{\pi_\theta}(s) \\)
			- → 方策勾配に組み込む
	- どうやって Advantage Function を推定するか
		- 方法1. ２つの異なるパラメータを使う
		- 方法2. TD 誤差を使う (期待値が Advantage Function と同じになる)
			- \\( V(s) \\) だけを推定すれば良い
	- Critic の変種 (異なる時間スケール、ターゲット)
		- MC, TD(0), 前向き観点 TD(λ), 後ろ向き観点 TD(λ)
	- Actor の変種 (異なる時間スケール、ターゲット)
		- MC → 利得 \\( v_t \\) 
		- TD → TD誤差 \\( r + \gamma V_v(s_{t+1}) \\)
		- Eligibility Trace
	- 全く偏りの無い方策勾配を求めることも可能 → Compatible function approximator

