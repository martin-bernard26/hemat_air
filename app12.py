import streamlit as st
import sympy as sy
import math as mt

st.set_page_config(
    page_title="Aplikasi Trigonometri",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
st.title("Trigonometri")

tab1,tab2= st.tabs(["Penjumlahan Sudut","Identitas Ganda"])
with tab1:
    kolom = st.columns(2)
    kolom[0].image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Circle_cos_sin.gif")
    kolom[1].image("https://i.gifer.com/origin/57/57df9428b0c191201e7ce06f4a2e717c_w200.gif")
    halaman = st.sidebar.selectbox('untuk penjumlahan sudut',['Pengertian','contoh','latihan'])
    if halaman=="Pengertian":
        st.header("Penjumlahan Sudut")
        st.markdown('''<h4 style="color:green">
Dalam trigonometri, terdapat identitas penjumlahan dan pengurangan sudut yang sering digunakan
untuk menyederhanakan perhitungan. Berikut adalah rumus dasar untuk penjumlahan dan pengurangan sudut: 
               </h4>''', unsafe_allow_html=True)
        st.markdown('''
<h5 style="color:blue">Rumus Sinus Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\sin{(a+b)}=\sin{a}\cos{b}+\cos{a}\sin{b}")
        st.latex("\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}")
        st.markdown('''<h5 style="color:blue">Rumus cosinus Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\cos{(a+b)}=\cos{a}\cos{b}-\sin{a}\sin{b}")
        st.latex("\cos{(a-b)}=\cos{a}\cos{b}+\sin{a}\sin{b}")
        st.markdown('''<h5 style="color:blue">Rumus Tangen Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\\tan{(a+b)}=\\frac{\\tan{a}+\\tan{b}}{1-\\tan{a}\\tan{b}},\;dengan\;syarat\;\\tan{a}\\tan{b}\\neq{1}")
        st.latex("\\tan{(a-b)}=\\frac{\\tan{a}-\\tan{b}}{1+\\tan{a}\\tan{b}},\;dengan\;syarat\;\\tan{a}\\tan{b}\\neq{-1}")
        bukti=st.button("lihat pembuktian")
        if bukti:
            kolom1 = st.columns([1,2],vertical_alignment="center")
            with kolom1[0]:
                st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBy-CsA5Cd9NHwWeZ4AgxFCEwk97AneGQfrqFNwV4MgqoLZSoKdVT7INNoBQknFxJmCsxJL1608XYTRzyXfHjbfVXMB30CZX4gRClJqtAp1DD7Osoooc5HB2UR5Q_xwn3lDeoLWr_Nmtw/s320/penurunan+rumus+cos+2.png")
            tulisan_html1='''
                            <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GeoGebra Integration</title>
  <script src="https://cdn.geogebra.org/apps/deployggb.js"></script>
  <style>
      #ggb-container{
          border:2px solid black;
          box-shadow:2px 2px 2px 2px blue;
      }
  </style>
</head>
<body>
  <h1>Bukti Pertama</h1>
  <div><input type="text" id="masukan"><div>
  <div id="ggb-container" style="width: 800px; height: 500px;"></div>
  
  <script>
    var ggbApp = new GGBApplet({
      "id":"ggbApplet",
      "appName": "classic",  // Pilihan: "graphing", "geometry", "3d", "classic", dll.
      "width": 800,
      "height": 500,
      "showToolBar": true,  // Menampilkan toolbar GeoGebra
      "showAlgebraInput": true,  // Menampilkan input aljabar
      "showMenuBar": true,  // Menampilkan menu
    }, true); // 'true' untuk membuat aplikasi GeoGebra responsif

    // Muat aplikasi GeoGebra ke dalam container
    window.addEventListener("load", function () {
      ggbApp.inject('ggb-container');
    });
    var masukan = document.getElementById("masukan")
    
    masukan.addEventListener("keydown",(e)=>{
        if(e.key==="Enter"){
            var pisahkan = masukan.value.split(";")
            ggbApplet.evalCommand('Text("'+pisahkan[0]+'",'+pisahkan[1]+',true,true)')
            
        }
    })
  </script>
</body>
</html>
'''
            with kolom1[1]:
                st.components.v1.html(tulisan_html1,width=800,height=600)
    elif halaman=="contoh":
        st.header("contoh")
        st.subheader("Masukan 2 nilai sudut")
        if "bilangan1" not in st.session_state:
            st.session_state.bilangan1=""
        if "bilangan2" not in st.session_state:
            st.session_state.bilangan2=""
        kolom1 = st.columns(2)
        kolom1[0].text_input("Masukan sudut pertama",key="bilangan1")
        kolom1[1].text_input("Masukan sudut kedua",key="bilangan2")
        if st.session_state.bilangan1 and st.session_state.bilangan2:
            nilai1 = int(st.session_state.bilangan1)
            nilai2 = int(st.session_state.bilangan2)
            nilai3 = sy.latex(sy.sin(sy.rad(nilai1)))
            st.write(sy.latex(nilai3))
            st.latex('\sin{('+str(nilai1)+'+'+str(nilai2)+')}=\sin{'+str(nilai1)+'}\cos{'+str(nilai2)+'}+\cos{'+str(nilai1)+'}\sin{'+str(nilai2)+'}='+nilai3)
                
        
        
