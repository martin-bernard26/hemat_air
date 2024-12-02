import streamlit as st



st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1733135017/fives_epdalm.png",width=200)
tab = st.tabs(["Ayo Membaca","Latihan","terbagi dua","Soal Numerasi"])
def bacaan():
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732177110/hemat_air_y8ccmz.png")
    tulisan_html1='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-color:lightgray;
        }
        #judul{
            font-family:"bauhaus 93";
            color:green;
            text-align:center;
            font-size:40px;
            text-shadow:2px 2px 2px red;
        }
        #judul:hover{
            color:yellow;
            text-shadow:2px 2px 2px black;
        }
        .isi{
            font-family:"comic sans ms";
            font-size:20px;
            text-align:justify;
            margin:10px;
            border-radius:10px;
            box-shadow:2px 2px 2px 2px grey;
            background-color:cyan;
            padding:5px;
        }
        .isi:hover{
            background-color:yellow;
        }
    </style>
</head>
<body>
    <div id="judul">Hemat Air, Cara Mudah Menyelamatkan Bumi</div>
    <div class="isi">Pulang sekolah, Aini selalu menyempatkan diri untuk beristirahat sejenak. 
        Sambil minum segelas air putih dan makan kudapan yang kadang-kadang disiapkan ibu. 
        Aini   menghilangkan   lelah   sambil   menunggu   keringat  di tubuhnya menguap. 
        Kadang-kadang Aini juga membaca buku atau surat kabar sambil beristirahat di teras 
        depan. </div>
    <div class="isi">Hari itu panas sekali. Aini membuka keran air hingga air deras mengalir 
        ke bak mandi. Aini mengguyurkan air ke badan berulang kali. 
        Rasanya, tiga kali mengguyur air ke sekujur tubuh, tidak cukup untuk mengusir panas 
        hari itu. Selesai mandi Aini bergegas ke rumah Dara. Hari itu, mereka berjanji untuk 
        bersama-sama membuat boneka tangan dari kaus kaki.</div>
    <div class="isi">Pulang dari kantor, ayah pun ingin mandi untuk menyegarkan badan. Betapa kagetnya 
        ayah, ketika melihat air di bak mandi meluap terbuang ke lantai kamar mandi. 
        Ternyata, Aini lupa menutup keran air. Air masih mengalir deras, entah sudah 
        beberapa jam. Pantas saja lantai kamar mandi sedikit tergenang oleh limpahan 
        air dari bak mandi. Ayah menggelengkan kepala. Bukan sekali ini Aini lupa menutup 
        keran air.</div>
    <div class="isi">
        Perlu diingat betapa panjang siklus air, dari penguapan hingga kembali ke tanah. 
        Perlu juga diingat ketika musim kemarau panjang, ketika air tanah sulit didapat. 
        Aini pun perlu mengingat bahwa ada teman sebayanya yang tinggal di daerah yang 
        gersang, sulit mendapatkan air sekedar untuk membasahi muka. 
        Persediaan air di Bumi tidak cukup untuk semua orang. Bahkan sepertiga penduduk 
        dunia mengalami kesulitan air. Pemanasan global membuat kekeringan semakin panjang.
        Hujan berkurang, air semakin lama sampai kembali ke tanah.
    </div>
    <div class="isi">
        Menghemat air merupakan salah satu bentuk kepedulian terhadap Bumi. Mematikan 
        keran air ketika tidak diperlukan merupakan cara mudah untuk menghemat air. Ketika
         kita sudah melakukan hal yang mudah demi Bumi, pasti kita dapat melakukan hal 
         yang lebih untuk menyelamatkan Bumi. Aini mengangguk pelan saat diberi nasihat 
         ayahnya. Ia bukan tidak tahu, hanya ia masih sering lupa. Aini harus terus 
         mengingat, hemat air  merupakan cara mudah untuk menyelamatkan Bumi.
    </div>
</body>
</html>
    '''
    st.components.v1.html(tulisan_html1,width=1100,height=750)

def bacaan1():
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732177110/hemat_air_y8ccmz.png")
    tulisan_html1='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-color:lightgray;
        }
        #judul{
            font-family:"bauhaus 93";
            color:green;
            text-align:center;
            font-size:40px;
            text-shadow:2px 2px 2px red;
        }
        #judul:hover{
            color:yellow;
            text-shadow:2px 2px 2px black;
        }
        .isi{
            font-family:"comic sans ms";
            font-size:20px;
            text-align:justify;
            margin:10px;
            border-radius:10px;
            box-shadow:2px 2px 2px 2px grey;
            background-color:cyan;
            padding:5px;
        }
        .isi:hover{
            background-color:yellow;
        }
    </style>
</head>
<body>
    <div id="judul">Hemat Air, Cara Mudah Menyelamatkan Bumi</div>
    <div class="isi">Pulang sekolah, Aini selalu menyempatkan diri untuk beristirahat sejenak. 
        Sambil minum segelas air putih dan makan kudapan yang kadang-kadang disiapkan ibu. 
        Aini   menghilangkan   lelah   sambil   menunggu   keringat  di tubuhnya menguap. 
        Kadang-kadang Aini juga membaca buku atau surat kabar sambil beristirahat di teras 
        depan. </div>
    <div class="isi">Hari itu panas sekali. Aini membuka keran air hingga air deras mengalir 
        ke bak mandi. Aini mengguyurkan air ke badan berulang kali. 
        Rasanya, tiga kali mengguyur air ke sekujur tubuh, tidak cukup untuk mengusir panas 
        hari itu. Selesai mandi Aini bergegas ke rumah Dara. Hari itu, mereka berjanji untuk 
        bersama-sama membuat boneka tangan dari kaus kaki.</div>
    <div class="isi">Pulang dari kantor, ayah pun ingin mandi untuk menyegarkan badan. Betapa kagetnya 
        ayah, ketika melihat air di bak mandi meluap terbuang ke lantai kamar mandi. 
        Ternyata, Aini lupa menutup keran air. Air masih mengalir deras, entah sudah 
        beberapa jam. Pantas saja lantai kamar mandi sedikit tergenang oleh limpahan 
        air dari bak mandi. Ayah menggelengkan kepala. Bukan sekali ini Aini lupa menutup 
        keran air.</div>
    <div class="isi">
        Perlu diingat betapa panjang siklus air, dari penguapan hingga kembali ke tanah. 
        Perlu juga diingat ketika musim kemarau panjang, ketika air tanah sulit didapat. 
        Aini pun perlu mengingat bahwa ada teman sebayanya yang tinggal di daerah yang 
        gersang, sulit mendapatkan air sekedar untuk membasahi muka. 
        Persediaan air di Bumi tidak cukup untuk semua orang. Bahkan sepertiga penduduk 
        dunia mengalami kesulitan air. Pemanasan global membuat kekeringan semakin panjang.
        Hujan berkurang, air semakin lama sampai kembali ke tanah.
    </div>
    <div class="isi">
        Menghemat air merupakan salah satu bentuk kepedulian terhadap Bumi. Mematikan 
        keran air ketika tidak diperlukan merupakan cara mudah untuk menghemat air. Ketika
         kita sudah melakukan hal yang mudah demi Bumi, pasti kita dapat melakukan hal 
         yang lebih untuk menyelamatkan Bumi. Aini mengangguk pelan saat diberi nasihat 
         ayahnya. Ia bukan tidak tahu, hanya ia masih sering lupa. Aini harus terus 
         mengingat, hemat air  merupakan cara mudah untuk menyelamatkan Bumi.
    </div>
</body>
</html>
    '''
    st.components.v1.html(tulisan_html1,width=550,height=1500)
with tab[0]:
    bacaan()

def latihan_soal():
    kol = st.columns(2)
    with kol[0]:
        with st.container(border=True):
            # Elemen input di dalam container
            nama = st.text_input("Nama:",key='urut1')
            kelas = st.text_input("Kelas:",key='urut2')
            sekolah = st.text_input("Nama Sekolah:",key='urut3')
    with kol[1]:
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732179623/soal_test_p9lghr.png")
    st.markdown('''
                <div><b>Petunjuk</b>
                <ol type="a">
                    <li>Selesaikan tugas menyenangkan berikut!</li>
                    <li>Tulis jawaban dengan benar dan jelas!</li>
                    <li>Soal-soal berikut berdasarkan teks bacaan yang berjudul “Hemat Air, Cara Mudah Menyelamatkan Bumi”.</li>
                </ol>
                </div>
                ''', unsafe_allow_html=True)
    if nama and kelas and sekolah:
        tulisan_html2=f'''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .pertanyaan{{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            color:blue;
        }}
        .pertanyaan1, .pertanyaan2{{
            font-size:18px;
            color:black;
            font-weight:bold;
            margin:5px;
        }}
        .pertanyaan3{{
            border:2px solid brown;
            width:300px;
            height:30px;
            background-color:white;
            border-radius:10px;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan3:hover{{
            background-color:yellow;
            border-radius:5px;
        }}
        .pertanyaan4, .pertanyaan5{{
            border-radius:10px;
            border:2px solid black;
            box-shadow:2px 2px 2px 2px green;
            background-color:white;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan4:hover, .pertanyaan5:hover{{
            background-color:cyan;
        }}
        .pertanyaan4:focus, .pertanyaan5:focus{{
            background-color:lightgoldenrodyellow;
            font-size:15px;
            padding:3px;
        }}
        #kirim1{{
            font-family:nroadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }}
    </style>
</head>
<body>
    <div>
        <div><input type="text" id="nama" value={nama}></div>
        <div><input type="text" id="kelas" value={kelas}></div>
        <div><input type="text" id="ns" value={sekolah}></div>
    </div>
    <div>
        <ol>
            <li class="pertanyaan"><b>Artikan kata-kata/kelompok kata berikutnya</b>
                <ol type="a">
                    <li class="pertanyaan1">Kudapan (bariske-2) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Mengguyurkan (baris ke-6) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Bergegas (baris ke-8) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Limpahan (baris ke-13) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Siklus (Baris ke-15) = <input class="pertanyaan3" type="text"></li>
                </ol>
            </li>
            <li class="pertanyaan"><b>Jawablah pertenyaan di bahwah ini</b>
                <ol type="a">
                    <li class="pertanyaan2"><div>Apa yang dilakukan Aini saat pulang sekolah?</div>
                        <div><textarea class="pertanyaan5" cols="80" rows="10"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa yang membuat ayah kaget saat pulang dari kantor?</div>
                        <div><textarea class="pertanyaan5" cols="80" rows="10"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa yang dibahas dalam teks bacaan tadi? </div>
                        <div><textarea class="pertanyaan5" cols="80" rows="10"></textarea></div>
                    </li>
                </ol>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan informasi-informasi penting yang kamu pahami dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan gagasan pokok dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan gagasan pendukung dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Urutkan fakta-fakta/informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan simpulan yang menyatakan bahwa kita harus menghemat air!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan ringkasan isi teks bacaan tadi menggunakan bahasamu sendiri!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Pernahkah kamu mengetahui informasi yang hampir sama seperti dalam teks tadi? 
                    Jika pernah, tuliskan informasi-informasi yang kamu temui dalam kehidupan sehari-hari 
                    yang hampir sama dengan teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Salah satu makna/nilai yang terdapat dalam bacaan tadi adalah kita harus menghemat penggunaan 
                    air, mengapa? </b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah teks bacaan tadi jelas dan lengkap? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, alur tulisan yang dituliskan penulis sudah benar? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Berdasarkan cerita dalam teks tadi, apakah di sekitarmu terdapat 
                    sumber air yang banyak atau tidak? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah isi cerita dalam teks tadi sesuai dengan 
                    kehidupan sehari-hari? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Setelah membaca cerita tadi, terdapat nilai/kebiasaan yang perlu ditiru 
                    olehmu diantaranya kita harus menghemat air. Tuliskan cara menghemat air yang 
                    akan kamu terapkan dalam kehidupan sehari-hari!</b>
                <div><textarea class="pertanyaan4" cols="80" rows="20"></textarea></div>
            </li>
        </ol>
    </div>
    <div><input id="kirim1" type="button" value="Kirim Jawaban" ></div>
    <script type="module">
            // Konfigurasi Firebase SDK
            import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
            const firebaseConfig = {{
                    apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                    authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                    databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                    projectId: "natural-ethos-423713-e0",
                    storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                    messagingSenderId: "41833960811",
                    appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
            }};

            // Inisialisasi Firebase
            const app = initializeApp(firebaseConfig);
            import {{getDatabase, set, get, update, remove, ref, child}}
                from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
            const db=getDatabase()
            var kirim1 = document.getElementById("kirim1")
            kirim1.addEventListener("click",()=>{{
                var nama = document.getElementById("nama").value
                var kelas = document.getElementById("kelas").value
                var ns = document.getElementById("ns").value
                var soal1 = document.getElementsByClassName("pertanyaan3")
                var soal2 = document.getElementsByClassName("pertanyaan5")
                var soal3 = document.getElementsByClassName("pertanyaan4")
                set(ref(db, 'hemat_air/' + nama), {{ 
                    nama:nama,
                    kelas:kelas,
                    ns:ns,
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
                set(ref(db, 'hemat_air/' + nama+'/soal'), {{ 
                    soal1a:soal1[0].value,
                    soal1b:soal1[1].value,
                    soal1c:soal1[2].value,
                    soal1d:soal1[3].value,
                    soal1e:soal1[4].value,
                    soal2a:soal2[0].value,
                    soal2b:soal2[1].value,
                    soal2c:soal2[2].value,
                    soal3:soal3[0].value,
                    soal4:soal3[1].value,
                    soal5:soal3[2].value,
                    soal6:soal3[3].value,
                    soal7:soal3[4].value,
                    soal8:soal3[5].value,
                    soal9:soal3[6].value,
                    soal10:soal3[7].value,
                    soal11:soal3[8].value,
                    soal12:soal3[9].value,
                    soal13:soal3[10].value,
                    soal14:soal3[11].value,
                    soal15:soal3[12].value
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
            }});

    </script>
</body>
</html>
    '''
        st.components.v1.html(tulisan_html2,width=1100,height=6500)
def latihan_soal1():
    kol = st.columns(2)
    with kol[0]:
        with st.container(border=True):
            # Elemen input di dalam container
            nama = st.text_input("Nama:",key='urut4')
            kelas = st.text_input("Kelas:",key='urut5')
            sekolah = st.text_input("Nama Sekolah:",key='urut6')
    with kol[1]:
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732179623/soal_test_p9lghr.png")
    st.markdown('''
                <div><b>Petunjuk</b>
                <ol type="a">
                    <li>Selesaikan tugas menyenangkan berikut!</li>
                    <li>Tulis jawaban dengan benar dan jelas!</li>
                    <li>Soal-soal berikut berdasarkan teks bacaan yang berjudul “Hemat Air, Cara Mudah Menyelamatkan Bumi”.</li>
                </ol>
                </div>
                ''', unsafe_allow_html=True)
    if nama and kelas and sekolah:
        tulisan_html2=f'''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .pertanyaan{{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            color:blue;
        }}
        .pertanyaan1, .pertanyaan2{{
            font-size:18px;
            color:black;
            font-weight:bold;
            margin:5px;
        }}
        .pertanyaan3{{
            border:2px solid brown;
            width:300px;
            height:30px;
            background-color:white;
            border-radius:10px;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan3:hover{{
            background-color:yellow;
            border-radius:5px;
        }}
        .pertanyaan4, .pertanyaan5{{
            border-radius:10px;
            border:2px solid black;
            box-shadow:2px 2px 2px 2px green;
            background-color:white;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan4:hover, .pertanyaan5:hover{{
            background-color:cyan;
        }}
        .pertanyaan4:focus, .pertanyaan5:focus{{
            background-color:lightgoldenrodyellow;
            font-size:15px;
            padding:3px;
        }}
        #kirim1{{
            font-family:nroadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }}
    </style>
</head>
<body>
    <div>
        <div><input type="text" id="nama" value={nama}></div>
        <div><input type="text" id="kelas" value={kelas}></div>
        <div><input type="text" id="ns" value={sekolah}></div>
    </div>
    <div>
        <ol>
            <li class="pertanyaan"><b>Artikan kata-kata/kelompok kata berikutnya</b>
                <ol type="a">
                    <li class="pertanyaan1">Kudapan (bariske-2) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Mengguyurkan (baris ke-6) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Bergegas (baris ke-8) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Limpahan (baris ke-13) = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Siklus (Baris ke-15) = <input class="pertanyaan3" type="text"></li>
                </ol>
            </li>
            <li class="pertanyaan"><b>Jawablah pertenyaan di bahwah ini</b>
                <ol type="a">
                    <li class="pertanyaan2"><div>Apa yang dilakukan Aini saat pulang sekolah?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa yang membuat ayah kaget saat pulang dari kantor?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa yang dibahas dalam teks bacaan tadi? </div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                    </li>
                </ol>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan informasi-informasi penting yang kamu pahami dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan gagasan pokok dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan gagasan pendukung dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Urutkan fakta-fakta/informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan simpulan yang menyatakan bahwa kita harus menghemat air!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan ringkasan isi teks bacaan tadi menggunakan bahasamu sendiri!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Pernahkah kamu mengetahui informasi yang hampir sama seperti dalam teks tadi? 
                    Jika pernah, tuliskan informasi-informasi yang kamu temui dalam kehidupan sehari-hari 
                    yang hampir sama dengan teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Salah satu makna/nilai yang terdapat dalam bacaan tadi adalah kita harus menghemat penggunaan 
                    air, mengapa? </b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah teks bacaan tadi jelas dan lengkap? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, alur tulisan yang dituliskan penulis sudah benar? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Berdasarkan cerita dalam teks tadi, apakah di sekitarmu terdapat 
                    sumber air yang banyak atau tidak? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah isi cerita dalam teks tadi sesuai dengan 
                    kehidupan sehari-hari? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Setelah membaca cerita tadi, terdapat nilai/kebiasaan yang perlu ditiru 
                    olehmu diantaranya kita harus menghemat air. Tuliskan cara menghemat air yang 
                    akan kamu terapkan dalam kehidupan sehari-hari!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
        </ol>
    </div>
    <div><input id="kirim1" type="button" value="Kirim Jawaban" ></div>
    <script type="module">
            // Konfigurasi Firebase SDK
            import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
            const firebaseConfig = {{
                    apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                    authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                    databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                    projectId: "natural-ethos-423713-e0",
                    storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                    messagingSenderId: "41833960811",
                    appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
            }};

            // Inisialisasi Firebase
            const app = initializeApp(firebaseConfig);
            import {{getDatabase, set, get, update, remove, ref, child}}
                from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
            const db=getDatabase()
            var kirim1 = document.getElementById("kirim1")
            kirim1.addEventListener("click",()=>{{
                var nama = document.getElementById("nama").value
                var kelas = document.getElementById("kelas").value
                var ns = document.getElementById("ns").value
                var soal1 = document.getElementsByClassName("pertanyaan3")
                var soal2 = document.getElementsByClassName("pertanyaan5")
                var soal3 = document.getElementsByClassName("pertanyaan4")
                set(ref(db, 'hemat_air/' + nama), {{ 
                    nama:nama,
                    kelas:kelas,
                    ns:ns,
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
                set(ref(db, 'hemat_air/' + nama+'/soal'), {{ 
                    soal1a:soal1[0].value,
                    soal1b:soal1[1].value,
                    soal1c:soal1[2].value,
                    soal1d:soal1[3].value,
                    soal1e:soal1[4].value,
                    soal2a:soal2[0].value,
                    soal2b:soal2[1].value,
                    soal2c:soal2[2].value,
                    soal3:soal3[0].value,
                    soal4:soal3[1].value,
                    soal5:soal3[2].value,
                    soal6:soal3[3].value,
                    soal7:soal3[4].value,
                    soal8:soal3[5].value,
                    soal9:soal3[6].value,
                    soal10:soal3[7].value,
                    soal11:soal3[8].value,
                    soal12:soal3[9].value,
                    soal13:soal3[10].value,
                    soal14:soal3[11].value,
                    soal15:soal3[12].value
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
            }});

    </script>
</body>
</html>
    '''
        st.components.v1.html(tulisan_html2,width=550,height=13000)
with tab[1]:
    latihan_soal()
with tab[2]:
    kolom = st.columns(2)
    with kolom[0]:
        bacaan1()
    with kolom[1]:
        latihan_soal1()
with tab[3]:
    tuliskan_html5='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            padding:10px;
            background-color:lightgray
        }
        .judul{
            font-family:"bauhaus 93";
            font-size:20px;
            font-weight:bold;
        }
        .bagian{
            font-size:30px;
            color:blue;
            text-shadow:2px 2px 2px red;
        }
        .bagian1{
            margin:3px;
            color:green;
            font-weight:bold;
        }
        .ident{
            border: 2px solid black;
            border-radius:5px;
            width:300px;
            height:30px;
            box-shadow:2px 2px 2px 2px orange;
        }
        #identitas{
            padding:5px;
            border:2px solid black;
            border-radius:3px;
            box-shadow:2px 2px 2px 2px yellow;
            margin:5px;
            background-color:mistyrose
        }
        #petunjuk{
            border: 2px solid black;
            border-radius:5px;
            background-color:cyan;
            padding:5px;
            font-size:18px;
            text-align:justify;
        }
        .bagian2{
            color:brown;
            font-weight:bold;
            font-size:20px;
            margin:5px;
        }
        ul li{
            margin:3px;
            font-size:20px;
        }
        .bagian3{
            border:3px solid black;
            border-radius:10px;
            box-shadow:2px 2px 2px 2px green;
        }
        #kirim1{
            font-family:broadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }
    </style>
</head>
<body>
    <div class="judul bagian">Tugas Numerasi: Hemat Air, Cara Mudah Menyelamatkan Bumi</div>
    <div id="identitas">
        <div class="bagian1" id="nama">Nama: <input class="ident" type="text"></div>
        <div class="bagian1" id="kelas">Kelas: <input class="ident" type="text"></div>
    </div>
    <div class="judul">Petunjuk</div>
    <div id="petunjuk">Bacalah teks <b><i>"Hemat Air, Cara Mudah Menyelamatkan Bumi" </i></b>untuk menjawab pertanyaan-pertanyaan berikut. 
        Jawablah dengan jelas dan lengkap!</div>
    <div class="judul">Soal-soal:</div>
    <div>
        <ol>
            <li><div class="bagian2">Berapa liter air yang terbuang?</div>
                <ul type="circle">
                <li>Ayah kaget saat melihat bak mandi meluap karena Aini lupa menutup keran air. 
                    Jika dalam satu menit keran mengalirkan air sebanyak 2 liter dan Aini lupa 
                    menutup keran selama 30 menit, berapa liter air yang terbuang?</li>
                <div><textarea class="bagian3" id="jawaban1" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Menghitung Kebutuhan Air dalam Satu Hari</div>
                <ul type="circle">
                    <li>Aini biasanya menggunakan air untuk mandi, mencuci tangan, dan minum. 
                        Jika ia mandi menggunakan 15 liter air, mencuci tangan menggunakan 5 liter, 
                        dan minum 1 liter per hari, berapa liter air yang ia butuhkan setiap hari?</li>
                        <div><textarea class="bagian3" id="jawaban2a" rows="10" cols="80"></textarea></div>
                    <li>Jika Aini mengurangi penggunaan air saat mandi menjadi 10 liter, 
                        berapa penghematan yang ia lakukan?</li>
                    <div><textarea class="bagian3" id="jawaban2b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Estimasi Air untuk Satu Minggu</div>
                <ul type="circle">
                    <li>Hitung total air yang dibutuhkan Aini dalam seminggu untuk mandi, 
                        mencuci tangan, dan minum (gunakan jawaban dari nomor 2 untuk 
                        hitungan per hari).</li>
                        <div><textarea id="jawaban3" class="bagian3" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Membandingkan Penggunaan Air</div>
                <ul type="circle">
                    <li>Aini menggunakan 15 liter air untuk mandi, sedangkan adiknya hanya menggunakan
                         10 liter. Berapa banyak air yang lebih sedikit digunakan oleh adik 
                         Aini setiap hari?</li>
                        <div><textarea class="bagian3" id="jawaban4a" rows="10" cols="80"></textarea></div>
                    <li>Jika mereka berdua mandi setiap hari selama satu bulan (30 hari), berapa banyak 
                        air yang dihemat oleh adik Aini dibandingkan Aini?</li>
                        <div><textarea class="bagian3" id="jawaban4b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Konservasi Air dalam Kehidupan Sehari-hari</div>
                <ul type="circle">
                    <li>Dalam teks disebutkan bahwa sepertiga penduduk dunia mengalami 
                        kesulitan air. Jika populasi dunia adalah sekitar 7,8 miliar orang, 
                        kira-kira berapa jumlah orang yang mengalami kesulitan air?</li>
                        <div><textarea class="bagian3" id="jawaban5" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Menulis dan Menggambar Strategi Hemat Air</div>
                <ul type="circle">
                    <li>Tuliskan 3 cara sederhana yang bisa kamu lakukan untuk menghemat air 
                        di rumah. Jelaskan setiap cara tersebut.</li>
                        <div><textarea class="bagian3" id="jawaban6a" rows="10" cols="80"></textarea></div>
                    <li>Buatlah gambar atau diagram alur untuk salah satu cara di atas, 
                        misalnya, langkah-langkah mematikan keran setelah selesai 
                        menggunakan air.</li>
                        <div><textarea class="bagian3" id="jawaban6b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
        </ol>
    </div>
    <div><input type="button" value="Kirim" id="kirim1"></div>
    <script type="module">
        // Konfigurasi Firebase SDK
        import {initializeApp} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
        const firebaseConfig = {
                apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                projectId: "natural-ethos-423713-e0",
                storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                messagingSenderId: "41833960811",
                appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
        };

        // Inisialisasi Firebase
        const app = initializeApp(firebaseConfig);
        import {getDatabase, set, get, update, remove, ref, child}
            from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
        const db=getDatabase()
        var kirim1 = document.getElementById("kirim1")
        kirim1.addEventListener("click",()=>{
            var nama = document.getElementById("nama").value
            var kelas = document.getElementById("kelas").value
            var soal1 = document.getElementsByClassName("pertanyaan1")
            var soal2a = document.getElementsByClassName("pertanyaan2a")
            var soal2b = document.getElementsByClassName("pertanyaan2b")
            var soal3 = document.getElementsByClassName("pertanyaan3")
            var soal4a = document.getElementsByClassName("pertanyaan4a")
            var soal4b = document.getElementsByClassName("pertanyaan4b")
            var soal5 = document.getElementsByClassName("pertanyaan5")
            var soal6a = document.getElementsByClassName("pertanyaan6a")
            var soal6b = document.getElementsByClassName("pertanyaan6b")
            set(ref(db, 'hematAirNumerasi/' + nama), { 
                nama:nama,
                kelas:kelas,
            })
                .then(() => {
                    alert('Data added successfully');
                })
                .catch((error) => {
                console.error("Error adding data:", error);
            });
            set(ref(db, 'hematAirNumerasi1/' + nama+'/soal'), {
                soal1:soal1.value,
                soal2a:soal2a.value,
                soal2b:soal2b.value,
                soal3:soal3.value,
                soal4a:soal4a.value,
                soal4b:soal4b.value,
                soal5:soal5.value,
                soal6a:soal6a.value,
                soal6b:soal6b.value,
            })
                .then(() => {
                    alert('Data added successfully');
                })
                .catch((error) => {
                console.error("Error adding data:", error);
            });
        });
</script>
</body>
</html>
    '''
    st.components.v1.html(tuliskan_html5,width=1000,height=2600)
