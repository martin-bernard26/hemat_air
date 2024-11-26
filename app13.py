import streamlit as st



st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
tab = st.tabs(["Ayo Membaca","Latihan","terbagi dua"])
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
