import streamlit as st
st.title("シミュレーション結果表示")


st.subheader("5.1　保存量の誤差")
st.write("まず，シミュレーションの全時間において保存量の誤差が増大しないことを確認する．特にここではSim2の誤差を確認する．具体的には以下の3式の左辺を計算した")
st.latex(r'''
    R^{(3)} - K_{i j} K^{i j} + K^2 - 16 \pi \rho_H = 0,  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  (37)
    '''
    )
st.latex(r'''
    D_j K^j_{\ \ i} - D_i K - 8\pi J_i = 0,  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  (38)
    '''
    )
st.latex(r'''
    D_i E^i - 2a E^i D_i \phi = 0.  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  (39)
    '''
    )
st.write("式(37)，(38)，(39) についてはそれぞれADM分解より求めたHamiltonian, Momentum, Gauss Constraint を表す．")
st.image("Constraint_EMD.png", 
        caption="図2: Sim2 EMD の保存量のL2 ノルムの時間発展．(上段左) Hamiltonian Constraint [式(37)]，(上段中) Momentum Constraint [式(38) のx 成分]，(上段右) Momentum Constraint [式(38) のy 成分]，(下段左) Momentum Constraint [式(38) のz 成分]，(下段右) Gauss Constraint [式(39)]")
st.write("これより，誤差は増大せずに抑制されていることが確認できる．")


st.subheader("5.2　Sim1とSim2の比較")
st.write("異なる質量のブラックホール連星について，電荷は質量に比例するように設定しているため，ブラックホールが持つ電荷は異なっている．ブラックホール間距離$D$とワイルスカラーの$\Psi_4$と重力波の+モード$h_+$の時間発展は以下の通りである．")
col1, col2, col3 = st.columns([2, 7, 1]) # 例: 1:6:1 の比率で中央のカラムを広くとる

with col2:
    st.image("夏学資料/(sim1,2)Distance.png",
        width=400, 
        caption="図3.1: 質量M で規格化されたブラックホール間距離$D/M$ のSim1 とSim2 の比較")

col1, col2 = st.columns(2)

with col1:
    st.image("夏学資料/(sim1,2)Psi4.png", caption="図3.2: $\Psi_4$の球面調和関数展開 $l=2, m=2$のSim1 とSim2 の比較", use_container_width=True)

with col2:
    st.image("夏学資料/(sim1,2)h+.png", caption="図3.3: $h_+$の球面調和関数展開 $l=2, m=2$のSim1 とSim2 の比較", use_container_width=True)

st.write("Sim1とSim2の結果から，合体時刻に差が生まれていること，また振幅には違いが生まれていないことがわかる．特に$h_+$ に関して，重力波の周波数の上昇が早まっていることが確認できる．")
st.write("最後にエネルギー放出率の時間発展を見る．")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("夏学資料/(sim1,2)GW-energy.png", caption="図4.1: 重力場のエネルギー放出率のSim1 とSim2 の比較", use_container_width=True)

with col2:
    st.image("夏学資料/(sim1,2) EM-energy.png", caption="図4.2: 電磁場のエネルギー放出率のSim1 とSim2 の比較", use_container_width=True)

with col3:
    st.image("夏学資料/(sim1,2)phi-energy.png", caption="図4.3: スカラー場のエネルギー放出率のSim1 とSim2 の比較", use_container_width=True)

st.write("重力波，電磁場のエネルギー放出率はSim1 とSim2 では大きさに違いがなく，ピークとなる時刻のみに違いがある．")
