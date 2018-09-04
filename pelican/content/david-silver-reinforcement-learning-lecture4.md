Title: モデルフリー予測 - Google DeepMind の David Silver 氏による強化学習コース 講義4
Date: 2018-09-04 00:00
Category: Reinforcement Learning
slug: david-silver-reinforcement-learning-lecture4

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

「無料でアクセスできる最高の強化学習のコース」と名高い、Google DeepMind / University College London の David Silver 氏による強化学習のコース。[こちらのページから、全ての講義スライドと講義ビデオが見られる](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)。以下は、講義4 のメモです。

モデルフリー予測 = 未知の MDP の価値関数を推定する

- モンテカルロ (MC) 学習
	- 経験のエピソードから直接学習する
	- エピソードが終了する必要あり
	- 方策 \\( \pi \\) の下で、経験のエピソード \\( S_1, A_1, R_2, ..., S_k \sim \pi \\) から \\( v_\pi \\) を学習
	- 復習： 利得 \\( G_t = R_{t+1} + \gamma R_{t+2} + ... + \gamma^{T-1}R_T \\)
	- 復習： 価値関数 \\( v_\pi(s) = E_\pi[G_t | S_t = s] \\)
	- モンテカルロ方策評価：各エピソードについて、状態 \\( s \\) を最初に訪問した時に
		- カウンターと利得の合計を更新。
		- \\( V(s) \\) → 利得の合計 / 訪問回数
		- 十分多くの \\( N(s) \\) を観察すると、\\( V(s) \\) は \\( v_\pi(s) \\) に収束
	- 各訪問ごとに更新する場合
		- 訪問回数を、各訪問ごとに更新
		- これでも、\\( V(s) \to v_\pi(s) \\)
	- 「差分」を使った系列の平均計算
		- 系列 \\( x_1, x_2, ... \\) を全て観測し終わらなくても、それまでの平均 \\( \mu_k \\) を計算することができる
		- \\( \mu_k = \mu_{k-1} + \frac{1}{k} (x_k - \mu_{k-1}) \\) 
		- 直感的な説明： 新しい値を観測した時、それまでの推定値と大きくことなる場合は、推定値を大きく更新する。
		- \\( \mu_{k-1} \\) →.それまでの推定値。\\( x_k - \mu_{k-1} \\) → 新しい値を観測した時の「驚き」。\\( \frac{1}{k} \\) → 学習率
	- 差分モンテカルロ更新
		- エピソード毎に更新（全てのエピソードの「和」を保持しない）
		- \\( N(S_t) \leftarrow N(S_t) + 1 \\) 
		- \\( V(S_t) \leftarrow V(S_t) + \frac{1}{N(S_t)}(G_t - V(S_t)) \\)
		- 注：エピソードが終わるまで待つ必要あり

- 時間差分 (Temporal Difference) 学習
	- 経験のエピソードから直接学習する (モンテカルロ法と同じ)
	- エピソードが終了してなくても良い → ブートストラップ法 (モンテカルロ法との差異)
	- MC と TD の違い
		- MC: 実際の利得 \\( G_t \\) を使って更新: \\( V(S_t) \leftarrow V(S_t) + \alpha(G_t - V(S_t)) \\)
		- TD: 利得の予測値を使って更新: \\( V(S_t) \leftarrow V(S_t) + \alpha(R_{t+1} + \gamma V(S_{t+1}) - V(S_t)) \\)
			- \\( R_{t+1} + \gamma V(S_{t+1}) \\) は TD ターゲットと呼ばれる
			- \\( \delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \\) は TD 誤差と呼ばれる
	- TD の長所・欠点
		- 最終結果を見る前に学習できる。最終結果の無いエピソードでも学習できる
		- 偏り (Bias) と分散　(Variance) のトレードオフ
			- 真の TD ターゲット \\( R_{t+1} + \gamma v_\pi(S_{t+1}) \\) は \\( v_\pi(S_t) \\)の 不偏推定量
			- TD ターケット \\( R_{t+1} + \gamma V(S_{t+1}) \\) は、偏りのある推定量　
			- ただし、TD ターゲットは、利得よりも分散が小さい
		- MC は分散大、偏りゼロ。TD は分散小、偏りあり。
		- TD(0) は \\( v_\pi(s) \\) に収束。初期値に敏感
		- MC は、観察された利得との平均二乗誤差を最小化する解に収束する
		- TD は、データに対して尤度最大の MDPを学習し、それを解く
	- ブートストラップとサンプリング
		- MC → ブートストラップ無し
		- DP → ブートストラップ有り
		- TD → ブートストラップ有り
		- MC → サンプリング有り
		- DP → サンプリング無し
		- TD → サンプリング無し

- TD(λ)
	- TD ターゲットを計算するときに、nステップ先読みする
		- 例：\\( G_t^{(2)}  = R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) \\)
		- n を大きくすると、MC 法に収束する
	- nステップ先読みを平均する
		- 例：\\( \frac{1}{2} G_t^{(2)} + \frac{1}{2} G_t^{(4)} \\)
	- γ利得 → 全てのnステップ利得の幾何平均
		- \\( G_t^\lambda = (1-\lambda) \sum_{n=1}^\infty \lambda^{n-1} G_t^n \\)
		- なぜ幾何平均? 前の値を保持しなくて良いので、計算コストが低い。TD(0) と同じコストで計算できる。
	- TD(λ) の「前向き」観点
		- \\( V(S_t) \leftarrow V(S_t) + \alpha (G^\lambda_t - V(S_t)) \\)
	- MC と同じように、エピソードが収束するまで待つ必要がある
	- TD(λ) の「後ろ向き」観点
		- Eligibility Trace
			- 最近性と、頻度を両方考慮する量
			- \\( E_0(s) = 0, E_t(s) = \gamma E_{t-1}(s) + {\mathbf 1}(S_t = s) \\)
		- \\( V(s) \leftarrow V(s) + \alpha \delta_t E_t(s) \\)
		- \\( \lambda = 0 \\) の時 → TD(0) と等価
		- \\( \lambda = 1 \\) の時 → 更新の合計は　MC と同じ
