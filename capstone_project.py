import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Sales Report Order',
    layout = 'wide'
)

base="light"
primaryColor="#677ce4"
secondaryBackgroundColor="#fafafb"
textColor="#000000"
font="serif"

st.header("Sales Restaurant Reporting Data Visualization")
st.caption("Oleh : Rizky Aryendi Gumilang")
st.subheader("Polusi Udara")

st.write("Currently, our restaurant does not have a reporting system or dashboard to monitor sales. As a result, we are having difficulty presenting our achievements to stakeholders. ")
st.write("They are only getting raw sales data from Excel that is difficult to understand. ")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<<iframe width="600" height="450" src="https://lookerstudio.google.com/embed/reporting/bca699b4-b105-4ca5-b47c-fe962b247170/page/LlGJD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>');"""
    components.html(html_temp, height=600, width=1100)
if __name__ == "__main__":    
    main()

st.subheader("Bagaimana Tingkat Kematian Akibat Polusi Udara?")
st.write("Pada visualisasi dibawah ini, menunjukkan tingkat kematian global akibat polusi udara dari waktu ke waktu yang terbagi menjadi 2 kategori : Indoor Air Pollution dan Outdoor Air Pollution. Secara global, kita dapat melihat bahwa dalam beberapa dekade terakhir, angka kematian akibat polusi udara total telah menurun sejak tahun 1990. Terutama kematian yang disebabkan oleh Indoor Air Pollution. Namun, kematian yang disebabkan oleh Outdoor Air Pollution masih tergolong tinggi hingga saat ini")
st.write("Untuk melihat tingkat kematian tiap tahunnya, klik animasi pada visualisasi di bawah ini. Visualisasi ini juga bisa melihat bagaimana tingkat kematian yang disebabkan oleh polusi udara dalam berbagai negara.")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<iframe width="600" height="450" src="https://lookerstudio.google.com/embed/reporting/bca699b4-b105-4ca5-b47c-fe962b247170/page/LlGJD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>"""
    components.html(html_temp, height=770, width=1100)
if __name__ == "__main__":    
    main()

st.subheader("Indoor Air Pollution")
st.write("Indoor Air Pollution-Polusi udara dalam ruangan disebabkan oleh pembakaran sumber bahan bakar padat seperti kayu bakar, limbah tanaman, dan kotoran untuk memasak dan memanaskan.")
st.write("Visualisasi dibawah ini merupakan tingkat persentase kematian yang diakibatkan oleh indoor air pollution diberbagai negara tiap tahunnya. Dari peta tersebut, terlihat bahwa persentase kematian terbesar terdapat pada wilayah dengan tingkat ekonomi rendah dan mayoritas merupakan negara berkembang, seperti negara di benua Afrika, Amerika Latin, Asia Selatan, dan beberapa negara di Asia Tenggara. Keparahan polusi udara (indoor) ini disebabkan oleh rendahnya penghasilan masyarakat di wilayah tersebut, sanitasi yang kurang bersih, banyaknya yang masih memasak menggunakan kayu dan cara tradisional sehingga meningkatkan penyakit pernapasan (WHO).")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<iframe width="600" height="450" src="https://lookerstudio.google.com/embed/reporting/bca699b4-b105-4ca5-b47c-fe962b247170/page/LlGJD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>"""
    components.html(html_temp, height=750, width=1250)
if __name__ == "__main__":    
    main()

st.caption("Data source : https://ourworldindata.org/grapher/share-deaths-indoor-pollution?facet=none")

st.subheader("Outdoor Air Pollution")
st.write("Outdoor Air Pollution merupakan polusi udara yang disebabkan oleh pembakaran eksternal. Outdoor air pollution makin marak terjadi sejak zaman industrialisasi ")
st.write("Visualisasi dibawah ini merupakan persentase tingkat kematian yang disebabkan oleh Outdoor Air Pollution diberbagai negara tiap tahunnya. Dari visualisasi tersebut, terlihat beberapa negara yang memiliki persentase kematian akibat outdoor air pollution. Negara-negara besar seperti China, Arab, India, dan Rusia memiliki tingkat kematian yang tinggi. Ada juga beberapa negara yang memiliki persentase diatas 10%. Hal itu tentunya didasari oleh industri yang masih menggunakan bahan bakar fossil, gas rumah kaca, dan lain sebagainya ")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<iframe width="600" height="450" src="https://lookerstudio.google.com/embed/reporting/bca699b4-b105-4ca5-b47c-fe962b247170/page/LlGJD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>"""
    components.html(html_temp, height=750, width=1250)
if __name__ == "__main__":    
    main()

st.subheader("Siapa saja yang paling berdampak pada polusi udara?")
st.write("Polusi udara banyak memakan korban pada lansia yang berusia 70+, baik di indoor air pollution dan outdoor air pollution. Pada indoor Air Pollution, anak-anak berusia dibawah 5 tahun memiliki tingkat kematian yang cukup tinggi. Pada Outdoor Air Pollution, yang paling kena dampaknya adalah lansia berusia 70+ dan diikuti oleh orang yang berusia 50-69 tahun. Populasi berusia 70 tahun ke atas jelas memiliki risiko kematian dini yang jauh lebih tinggi akibat polusi udara luar ruangan. Ini, tentu saja, bukan hasil dari paparan akut tetapi dari paparan jangka panjang selama masa hidup mereka.")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1686493664946' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ti&#47;TingkatKematianBerdasarkanUsia&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TingkatKematianBerdasarkanUsia&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ti&#47;TingkatKematianBerdasarkanUsia&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686493664946');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='677px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='677px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, height=650, width=1000)
if __name__ == "__main__":    
    main()

st.subheader("Analisis Faktor Penyebab Kematian Akibat Polusi Udara dengan Ekonomi")
st.markdown("**Outdoor Air Pollution Meningkat Akibat Industrialisasi**")
st.write("Penyebab utama meningkatnya Outdoor Air Pollution adalah industrialisasi. Banyak negara yang berkategori middle income memiliki tingkat polusi udara yang tinggi. Visualisasi dibawah ini menunjukkan hubungan antara GDP percapita suatu negara dengan tingkat kematian akibat outdoor air pollution. Visualisasi dibawah ini menunjukkan bahwa GDP percapita suatu negara mempengaruhi tingkat kematian yang disebabkan oleh polusi udara. Negara yang termasuk middle-low income memiliki tingkat kematian yang tinggi dibandingkan negara yang memiliki jumlah income yang tinggi. Negara-negara dengan tingkat kematian yang sangat tinggi – seperti India, Mesir, Pakistan, dan China") 

import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1686534838635' style='position: relative'><noscript><a href='#'><img alt='Dashboard 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ti&#47;TingkatKematiandariOutdoorAirPollutionvsGDPPercapita&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TingkatKematiandariOutdoorAirPollutionvsGDPPercapita&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ti&#47;TingkatKematiandariOutdoorAirPollutionvsGDPPercapita&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686534838635');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, height=500, width=1000)
if __name__ == "__main__":    
    main()

st.markdown("**Akses ke Bahan Bakar Bersih Untuk Memasak Masih Sedikit**")
st.write("Penyebab Indoor Air Pollution tentunya terdapat pada banyaknya penggunaan bahan bakar fosil untuk memasak. Visualisasi dibawah ini menggambarkan hubungan antara akses ke bahan bakar bersih vs GDP percapita. Pada tingkat pendapatan rendah, rumah tangga sebagian besar bergantung pada sumber bahan bakar tradisional padat seperti limbah tanaman, kotoran ternak, dan kayu bakar. Dengan meningkatnya pendapatan, bauran energi ini cenderung beralih ke arang dan batubara. Hanya pada tingkat pendapatan yang lebih tinggi rumah tangga beralih dari bahan bakar padat yang berbahaya ke bahan bakar non-padat yang lebih bersih seperti etanol dan gas alam. Listrik hanya tersedia untuk rumah tangga dengan tingkat pendapatan tinggi.")
import streamlit as st
import streamlit.components.v1 as components
def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1686536672050' style='position: relative'><noscript><a href='#'><img alt='Dashboard 4 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ak&#47;AkseskeBahanBakarBersihuntukMemasakvsGDPPercapita&#47;Dashboard4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AkseskeBahanBakarBersihuntukMemasakvsGDPPercapita&#47;Dashboard4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ak&#47;AkseskeBahanBakarBersihuntukMemasakvsGDPPercapita&#47;Dashboard4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686536672050');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, height=500, width=1000)
if __name__ == "__main__":    
    main()

st.subheader("Bagaimana cara menanggulangi polusi udara?")
st.write("Melihat data-data yang telah dibahas, kematian akibat polusi udara memanglah sangat besar. Tingkat perekonomian disuatu negara sangatlah menentukan polusi udara. Adapun beberapa cara yang harus dilakukan untuk mengurangi polusi udara adalah: ")
st.write("1. Menggunakan bahan bakar ramah lingkungan seperti energi terbarukan")
st.write("2. Pemerintah harus memfasilitasi bahan bakar bersih untuk memasak, sehingga mengurangi indoor air pollution")
st.write("3. Industri perlu meninjau kembali untuk menggunakan filter agar asap atau gas buangan tidak terlalu banyak")