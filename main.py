import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

user_data = {}

category_mapping = {
    "nedir": [
    {"soru": "İklim değişikliği nedir?", "secenekler": ["A) Mevsimlerin değişmesi", "B) Havanın aniden soğuması", "C) Uzun vadeli iklimsel değişimler", "D) Günlük sıcaklık değişimi"], "dogru": "C"},
    {"soru": "İklim değişikliğinin temel nedeni nedir?", "secenekler": ["A) Güneş patlamaları", "B) Yanardağlar", "C) İnsan faaliyetleri", "D) Ayın hareketi"], "dogru": "C"},
    {"soru": "İklim değişikliği hangi gazların artışı ile ilişkilidir?", "secenekler": ["A) Oksijen", "B) Karbondioksit", "C) Azot", "D) Argon"], "dogru": "B"},
    {"soru": "İklim değişikliği genellikle hangi zaman ölçeğinde incelenir?", "secenekler": ["A) Günlük", "B) Haftalık", "C) Yıllık", "D) On yıllık veya daha uzun"], "dogru": "D"},
    {"soru": "İklim değişikliği ile en çok ilişkili olan sera gazı hangisidir?", "secenekler": ["A) Metan", "B) Karbondioksit", "C) Ozon", "D) Azot"], "dogru": "B"},
    {"soru": "Küresel ısınma, iklim değişikliğinin hangi etkisidir?", "secenekler": ["A) Hava kirliliği", "B) Sıcaklık artışı", "C) Deniz seviyesinin düşmesi", "D) Güneş ışınlarının azalması"], "dogru": "B"},
    {"soru": "İklim değişikliği hangi doğal sistemi etkiler?", "secenekler": ["A) Sadece atmosferi", "B) Atmosfer ve okyanusları", "C) Sadece okyanusları", "D) Hiçbirini"], "dogru": "B"},
    {"soru": "İklim değişikliği insan sağlığını nasıl etkileyebilir?", "secenekler": ["A) Yeni hastalıkların ortaya çıkması", "B) Enerji artışı", "C) Saç renginin değişmesi", "D) Hiç etkisi yoktur"], "dogru": "A"},
    {"soru": "İklim değişikliği neyi tehdit eder?", "secenekler": ["A) Doğal kaynakları", "B) Sadece şehirleri", "C) Sadece tarımı", "D) Sadece hayvanları"], "dogru": "A"},
    {"soru": "İklim değişikliğinin etkileri hangi alanlarda görülür?", "secenekler": ["A) Ekonomi", "B) Sağlık", "C) Doğa", "D) Hepsi"], "dogru": "D"},
    {"soru": "Sera gazları nereden gelir?", "secenekler": ["A) Fabrikalardan", "B) Arabalardan", "C) Ormansızlaşmadan", "D) Hepsi"], "dogru": "D"},
    {"soru": "İklim değişikliğine karşı hangi hareket yaygındır?", "secenekler": ["A) Ağaç kesmek", "B) Fosil yakıt kullanımı", "C) Yenilenebilir enerji kullanımı", "D) Plastik üretimi"], "dogru": "C"},
    {"soru": "İklim değişikliğinde en çok artan gaz?", "secenekler": ["A) Oksijen", "B) Azot", "C) Karbondioksit", "D) Metan"], "dogru": "C"},
    {"soru": "İklim değişikliği neden hızlandı?", "secenekler": ["A) İnsan faaliyetleri", "B) Volkanik patlamalar", "C) Güneş ışınları", "D) Ay tutulması"], "dogru": "A"},
    {"soru": "Küresel ısınma nedir?", "secenekler": ["A) Dünya'nın soğuması", "B) Atmosferdeki sıcaklık artışı", "C) Deniz seviyesinin düşmesi", "D) Kar yağışı artışı"], "dogru": "B"},
    {"soru": "İklim değişikliğinin doğal olmayan sebebi?", "secenekler": ["A) İnsan faaliyetleri", "B) Güneş aktiviteleri", "C) Okyanus akıntıları", "D) Toprak hareketleri"], "dogru": "A"},
    {"soru": "İklim değişikliği en çok hangi bölgede hissedilir?", "secenekler": ["A) Ekvator", "B) Kutup bölgeleri", "C) Çöller", "D) Ormanlar"], "dogru": "B"},
    {"soru": "İklim değişikliği neden önemlidir?", "secenekler": ["A) Sadece bilimsel", "B) Ekonomik ve sosyal etkileri var", "C) Yalnızca politik", "D) Etkisi yoktur"], "dogru": "B"},
    {"soru": "İklim değişikliği ile ilgili en önemli uluslararası anlaşma?", "secenekler": ["A) Kyoto Protokolü", "B) Paris Anlaşması", "C) Montreal Protokolü", "D) Rio Sözleşmesi"], "dogru": "B"},
    {"soru": "İklim değişikliğiyle mücadelede birey olarak ne yapabiliriz?", "secenekler": ["A) Daha az enerji kullanmak", "B) Daha çok araba kullanmak", "C) Ormanları kesmek", "D) Plastik atmak"], "dogru": "A"},

    ],
    "sebepler": [
    {"soru": "Fosil yakıt kullanımı hangi gaza neden olur?", "secenekler": ["A) Oksijen", "B) Azot", "C) Karbondioksit", "D) Helyum"], "dogru": "C"},
    {"soru": "Ormanların yok edilmesi neyi azaltır?", "secenekler": ["A) Karbondioksit", "B) Oksijen üretimini", "C) Metan", "D) Enerji üretimini"], "dogru": "B"},
    {"soru": "Tarım ve hayvancılık hangi sera gazını artırır?", "secenekler": ["A) Ozon", "B) Metan", "C) Azot", "D) Karbondioksit"], "dogru": "B"},
    {"soru": "Fosil yakıtlar nelerdir?", "secenekler": ["A) Kömür, petrol, doğal gaz", "B) Güneş enerjisi", "C) Rüzgar enerjisi", "D) Hidroelektrik"], "dogru": "A"},
    {"soru": "Sanayi tesisleri atmosfere ne salar?", "secenekler": ["A) Temiz hava", "B) Karbondioksit ve diğer gazlar", "C) Sadece su buharı", "D) Oksijen"], "dogru": "B"},
    {"soru": "Ormansızlaşmanın iklim değişikliğine etkisi nedir?", "secenekler": ["A) Karbon emilimini azaltır", "B) Daha fazla oksijen sağlar", "C) Hava sıcaklığını düşürür", "D) Yağışları artırır"], "dogru": "A"},
    {"soru": "Taş kömürü kullanımı neden zararlıdır?", "secenekler": ["A) Hava kirliliği yapar", "B) Yenilenebilir enerji kaynağıdır", "C) Sadece elektrik üretir", "D) Çevreyi temizler"], "dogru": "A"},
    {"soru": "Endüstriyel tarımın iklim değişikliğine etkisi?", "secenekler": ["A) Fosil yakıt tüketir ve sera gazı salar", "B) Sadece doğal yöntem kullanır", "C) İklimi olumlu etkiler", "D) Etkisi yoktur"], "dogru": "A"},
    {"soru": "Ulaşımda fosil yakıt kullanımı ne yapar?", "secenekler": ["A) Karbon ayak izini artırır", "B) Atmosferi temizler", "C) Enerji tasarrufu sağlar", "D) Doğaya zarar vermez"], "dogru": "A"},
    {"soru": "Enerji üretiminde en çok kullanılan fosil yakıt?", "secenekler": ["A) Doğal gaz", "B) Rüzgar", "C) Güneş", "D) Hidroelektrik"], "dogru": "A"},
    {"soru": "Atıkların doğada çözülmemesi neye yol açar?", "secenekler": ["A) Sera gazlarının artmasına", "B) Oksijen üretimine", "C) Yağışların azalmasına", "D) Enerji tasarrufuna"], "dogru": "A"},
    {"soru": "Fabrikalardan çıkan gazların çevreye etkisi nedir?", "secenekler": ["A) Hava kirliliği ve küresel ısınma", "B) Hava temizliği", "C) İklim soğutması", "D) Yağış artışı"], "dogru": "A"},
    {"soru": "Tarımda kullanılan gübrelerin etkisi nedir?", "secenekler": ["A) Metan ve diğer gazların artması", "B) Hava temizliği", "C) Sadece su kirliliği", "D) Enerji tasarrufu"], "dogru": "A"},
    {"soru": "Fosil yakıtlar yenilenebilir midir?", "secenekler": ["A) Evet", "B) Hayır"], "dogru": "B"},
    {"soru": "Hangi enerji kaynağı iklim değişikliğine en az zarar verir?", "secenekler": ["A) Güneş enerjisi", "B) Kömür", "C) Petrol", "D) Doğal gaz"], "dogru": "A"},
    {"soru": "İnsan faaliyetleri hangi süreçleri hızlandırır?", "secenekler": ["A) Sera gazı salınımı", "B) Oksijen artışı", "C) Atmosfer temizliği", "D) Yağışların artması"], "dogru": "A"},
    {"soru": "Hangi sektör iklim değişikliğine en çok katkıda bulunur?", "secenekler": ["A) Tarım", "B) Sanayi", "C) Ulaşım", "D) Hepsi"], "dogru": "D"},
    {"soru": "Ormansızlaşmanın sebebi nedir?", "secenekler": ["A) Tarım alanı açmak", "B) Enerji üretmek", "C) Hayvanları korumak", "D) Su tasarrufu"], "dogru": "A"},
    {"soru": "İklim değişikliğinde metan gazının kaynağı nedir?", "secenekler": ["A) Çöp depolama alanları", "B) Fabrikalar", "C) Okyanuslar", "D) Rüzgar türbinleri"], "dogru": "A"},
    {"soru": "Fosil yakıtların yanması ne üretir?", "secenekler": ["A) Karbondioksit ve diğer zararlı gazlar", "B) Sadece su buharı", "C) Oksijen", "D) Azot"], "dogru": "A"},
    ],
    "etkiler": [
    {"soru": "Küresel ısınma neye yol açabilir?", "secenekler": ["A) Daha kısa yaz", "B) Deniz seviyesinin düşmesi", "C) Buzulların erimesi", "D) Daha çok kar yağışı"], "dogru": "C"},
    {"soru": "İklim değişikliği sağlığı nasıl etkileyebilir?", "secenekler": ["A) Enerji verir", "B) Hiçbir etkisi yoktur", "C) Hava kirliliği ve sıcak dalgalarıyla", "D) Uykuyu artırır"], "dogru": "C"},
    {"soru": "İklim değişikliğinin en belirgin etkisi nedir?", "secenekler": ["A) Deniz seviyelerinin yükselmesi", "B) Daha fazla kar yağışı", "C) Havanın daha serin olması", "D) Doğal afetlerin azalması"], "dogru": "A"},
    {"soru": "İklim değişikliği hangi doğal afetleri artırabilir?", "secenekler": ["A) Kasırgalar ve seller", "B) Depremler", "C) Volkanik patlamalar", "D) Tsunamiler"], "dogru": "A"},
    {"soru": "Küresel ısınmanın denizlere etkisi nedir?", "secenekler": ["A) Deniz seviyesinin yükselmesi", "B) Denizlerin küçülmesi", "C) Tuz oranının azalması", "D) Deniz suyu sıcaklığının düşmesi"], "dogru": "A"},
    {"soru": "İklim değişikliği biyolojik çeşitliliği nasıl etkiler?", "secenekler": ["A) Türlerin yok olmasına neden olur", "B) Türlerin artmasına neden olur", "C) Etkisi yoktur", "D) Türlerin daha sağlıklı olmasına neden olur"], "dogru": "A"},
    {"soru": "İklim değişikliği tarımı nasıl etkiler?", "secenekler": ["A) Ürün verimini azaltabilir", "B) Ürün verimini artırır", "C) Hiçbir etkisi yoktur", "D) Tarımı destekler"], "dogru": "A"},
    {"soru": "İklim değişikliğinin sosyal etkileri nelerdir?", "secenekler": ["A) Göçler ve çatışmalar", "B) Daha iyi yaşam koşulları", "C) Hiçbir etkisi yoktur", "D) Sadece ekonomik etkileri vardır"], "dogru": "A"},
    {"soru": "İklim değişikliği hangi su kaynaklarını etkiler?", "secenekler": ["A) Nehirler ve göller", "B) Sadece denizler", "C) Sadece yeraltı suları", "D) Hiçbiri"], "dogru": "A"},
    {"soru": "Artan sıcaklıkların etkisi nedir?", "secenekler": ["A) Kuraklık ve yangın riski artar", "B) Yağışlar artar", "C) Daha soğuk kışlar", "D) Doğal afetlerin azalması"], "dogru": "A"},
    {"soru": "Küresel ısınmanın buzullara etkisi?", "secenekler": ["A) Erime", "B) Büyüme", "C) Değişim yok", "D) Yeni buzullar oluşması"], "dogru": "A"},
    {"soru": "İklim değişikliği hayvanların yaşamını nasıl etkiler?", "secenekler": ["A) Habitat kaybı ve türlerin azalması", "B) Hayvan sayısını artırır", "C) Etkisi yoktur", "D) Hayvanlar daha sağlıklı olur"], "dogru": "A"},
    {"soru": "İklim değişikliğinin ekonomik etkileri nelerdir?", "secenekler": ["A) Tarım ve balıkçılık zarar görür", "B) Ekonomi büyür", "C) Etkisi yoktur", "D) Sadece teknoloji etkilenir"], "dogru": "A"},
    {"soru": "Deniz seviyesinin yükselmesi neye neden olur?", "secenekler": ["A) Kıyı şehirlerinin su basması", "B) Daha fazla balık", "C) Denizlerin küçülmesi", "D) Plajların genişlemesi"], "dogru": "A"},
    {"soru": "İklim değişikliği sonucu hangi doğal afet artabilir?", "secenekler": ["A) Kasırgalar", "B) Depremler", "C) Tsunamiler", "D) Volkanik patlamalar"], "dogru": "A"},
    {"soru": "Sıcaklık artışı insan sağlığını nasıl etkiler?", "secenekler": ["A) Sıcak çarpması riskini artırır", "B) Enerji seviyesini artırır", "C) Hiç etkisi yoktur", "D) Uykuyu artırır"], "dogru": "A"},
    {"soru": "İklim değişikliği sel riskini nasıl etkiler?", "secenekler": ["A) Artırır", "B) Azaltır", "C) Etkisi yoktur", "D) Tamamen durdurur"], "dogru": "A"},
    {"soru": "Kuraklık iklim değişikliğinin bir sonucu mudur?", "secenekler": ["A) Evet", "B) Hayır"], "dogru": "A"},
    {"soru": "İklim değişikliği sonucu göçlerin artmasının sebebi nedir?", "secenekler": ["A) Yaşam alanlarının zarar görmesi", "B) Yeni iş imkanları", "C) Eğitim fırsatları", "D) Teknolojik gelişmeler"], "dogru": "A"},
    {"soru": "İklim değişikliği deniz canlılarını nasıl etkiler?", "secenekler": ["A) Habitat kaybı ve türlerin azalması", "B) Popülasyon artışı", "C) Etkisi yoktur", "D) Yeni türlerin çoğalması"], "dogru": "A"},
    {"soru": "İklim değişikliği hangi mevsimlerin dengesini bozar?", "secenekler": ["A) İlkbahar ve yaz", "B) Sadece kış", "C) Sadece yaz", "D) Mevsimler etkilenmez"], "dogru": "A"},
    ],
    "onlemler": [
    {"soru": "İklim değişikliğini önlemek için ne yapılmalı?", "secenekler": ["A) Ağaç kesmek", "B) Fosil yakıt kullanmak", "C) Geri dönüşüm yapmak", "D) Daha çok plastik üretmek"], "dogru": "C"},
    {"soru": "Hangisi çevre dostu ulaşım aracıdır?", "secenekler": ["A) Özel araç", "B) Bisiklet", "C) Uçak", "D) Kamyon"], "dogru": "B"},
    {"soru": "Enerji tasarrufu nasıl yapılır?", "secenekler": ["A) Gereksiz ışıkları kapatmak", "B) Daha çok araç kullanmak", "C) Plastik kullanmak", "D) Gereksiz elektrik tüketmek"], "dogru": "A"},
    {"soru": "Yenilenebilir enerji kaynakları nelerdir?", "secenekler": ["A) Güneş, rüzgar, hidroelektrik", "B) Kömür ve petrol", "C) Doğal gaz", "D) Nükleer enerji"], "dogru": "A"},
    {"soru": "Geri dönüşümün faydası nedir?", "secenekler": ["A) Atıkları azaltır", "B) Enerji tasarrufu sağlar", "C) Doğal kaynakları korur", "D) Hepsi"], "dogru": "D"},
    {"soru": "Ağaç dikmek iklim değişikliğine nasıl katkı sağlar?", "secenekler": ["A) Karbondioksiti azaltır", "B) Oksijen miktarını azaltır", "C) Suyu kirletir", "D) Enerji üretir"], "dogru": "A"},
    {"soru": "Çevre dostu alışkanlıklar nelerdir?", "secenekler": ["A) Daha az araç kullanmak", "B) Plastik kullanmamak", "C) Enerji tasarrufu yapmak", "D) Hepsi"], "dogru": "D"},
    {"soru": "Toplu taşıma kullanmak neden önemlidir?", "secenekler": ["A) Karbon salınımını azaltır", "B) Daha pahalıdır", "C) Zaman alır", "D) Çevreye zarar verir"], "dogru": "A"},
    {"soru": "Fosil yakıt kullanımını azaltmak için ne yapılmalı?", "secenekler": ["A) Yenilenebilir enerji kullanmak", "B) Daha fazla araç kullanmak", "C) Fabrika sayısını artırmak", "D) Daha çok plastik kullanmak"], "dogru": "A"},
    {"soru": "Enerji tasarrufu için evde ne yapılabilir?", "secenekler": ["A) Gereksiz ışıkları kapatmak", "B) Elektronikleri açık bırakmak", "C) Klimayı sürekli açık tutmak", "D) Su kullanımı artırmak"], "dogru": "A"},
    {"soru": "Sürdürülebilir tarım nasıl yapılır?", "secenekler": ["A) Kimyasal kullanımını azaltarak", "B) Daha çok tarım ilacı kullanarak", "C) Ormanları keserek", "D) Toprağı korumadan"], "dogru": "A"},
    {"soru": "İklim değişikliğine karşı bireysel önlem nedir?", "secenekler": ["A) Enerji tüketimini azaltmak", "B) Daha çok araç kullanmak", "C) Plastik atmak", "D) Ormanları kesmek"], "dogru": "A"},
    {"soru": "Doğa dostu alışkanlıklar arasında neler vardır?", "secenekler": ["A) Geri dönüşüm yapmak", "B) Bisiklet kullanmak", "C) Ağaç dikmek", "D) Hepsi"], "dogru": "D"},
    {"soru": "Yenilenebilir enerji kullanmanın faydası?", "secenekler": ["A) Karbon salınımını azaltır", "B) Fosil yakıt tüketimini artırır", "C) Çevre kirliliğini artırır", "D) Enerji tasarrufu sağlamaz"], "dogru": "A"},
    {"soru": "Su tasarrufu neden önemlidir?", "secenekler": ["A) Su kaynaklarını korur", "B) Enerji tasarrufu sağlar", "C) Çevreyi kirletir", "D) Su tasarrufu önemli değildir"], "dogru": "A"},
    {"soru": "Doğal yaşam alanlarını korumak neden önemlidir?", "secenekler": ["A) Türlerin yaşaması için", "B) Doğanın dengesi için", "C) İklim değişikliğine karşı", "D) Hepsi"], "dogru": "D"},
    {"soru": "Fosil yakıt kullanımını azaltmak için en iyi yöntem nedir?", "secenekler": ["A) Yenilenebilir enerjiye geçmek", "B) Daha fazla araç kullanmak", "C) Fabrikaları artırmak", "D) Ormanları kesmek"], "dogru": "A"},
    {"soru": "İklim değişikliğine karşı uluslararası işbirliği neden önemlidir?", "secenekler": ["A) Sorun küresel olduğu için", "B) Sadece ülkeler kendi başına çözebilir", "C) İşbirliği gerekmez", "D) Sorun önemsizdir"], "dogru": "A"},
    {"soru": "Çevre dostu ürünler kullanmanın faydası?", "secenekler": ["A) Doğayı korur", "B) Sağlığı destekler", "C) Kaynakları korur", "D) Hepsi"], "dogru": "D"},
    ]
}


@bot.event
async def on_ready():
    print(f'{bot.user} is online')

@bot.command()
async def iklim_nedir(ctx):
    embed = discord.Embed(
        title="🌍 İklim Değişikliği Nedir?",
        description=(
            "İklim değişikliği, uzun bir zaman diliminde 🌡️ **dünya iklim sistemlerinde** yaşanan büyük değişikliklerdir.\n\n"
            "🌬️ Atmosferdeki **karbondioksit (CO₂)** ve diğer sera gazlarının artışı,\n"
            "🔥 **Küresel ısınma**, buzulların erimesi 🧊, deniz seviyelerinin 🌊 yükselmesi ve \n"
            "aşırı hava olayları  gibi etkileri beraberinde getirir.\n\n"
            "**Neden Önemli?**\n"
            "➡️ Tarım, hayvanlar ve hatta insanların yaşamı bu değişiklikten doğrudan etkilenir.\n"
            "➡️ Doğa dengesini kaybedebilir, birçok canlı türü yok olabilir.\n\n"
            "**💡 Unutma:** İklim değişikliği sadece bir çevre sorunu değil, aynı zamanda **insanlık sorunudur**."
        ),
        color=0x1abc9c
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4004/4004348.png")
    embed.set_image(url="https://i.ytimg.com/vi/G9t__9Tmwv4/maxresdefault.jpg")
    await ctx.send(embed=embed)




@bot.command()
async def iklim_sebebleri(ctx):
    embed = discord.Embed(
        title="🔥 İklim Değişikliğinin Sebepleri",
        description=(
            "İklim değişikliği tesadüfi değil, çoğu **insan kaynaklı** sebeplerden oluşur. İşte başlıca nedenler:\n\n"
            "🚗 **Fosil Yakıt Kullanımı** – Benzin, kömür ve doğal gaz yakıldığında atmosfere sera gazları yayılır.\n"
            "🏭 **Sanayi ve Fabrikalar** – Büyük miktarda **karbondioksit (CO₂)** ve metan gibi zararlı gazlar üretir.\n"
            "🌲 **Ormansızlaşma** – Ağaçlar karbonu emer. Ağaç kesildiğinde bu denge bozulur.\n"
            "🐄 **Tarım ve Hayvancılık** – Büyükbaş hayvanlar metan gazı üretir, gübreler ve makineler de iklime zarar verir.\n"
            "🚮 **Atıklar ve Plastik Kullanımı** – Çöplerin doğada çözülmemesi sera gazı salınımını artırır.\n\n"
            "**🌐 Not:** Tüm bu nedenler birleştiğinde dünyanın ısısını artırır ve doğayı tehdit eder."
        ),
        color=0xe67e22
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4324/4324561.png")
    embed.set_image(url="https://static.euronews.com/articles/stories/07/17/63/10/808x721_cmsv2_87046977-9642-5964-a951-e8648709c679-7176310.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def iklim_ne_yapabilir(ctx):
    embed = discord.Embed(
        title="🌪️ İklim Değişikliği Neye Sebep Olabilir?",
        description=(
            "**İklim değişikliği sadece sıcaklık artışı değildir!** İşte olası sonuçları:\n\n"
            "🔥 **Küresel Isınma** – Sıcaklıkların artmasıyla kuraklıklar ve orman yangınları çoğalır.\n"
            "🌊 **Deniz Seviyesinin Yükselmesi** – Buzulların erimesiyle sahil şehirleri su altında kalabilir.\n"
            "🌪️ **Aşırı Hava Olayları** – Fırtınalar, kasırgalar, sel felaketleri daha sık ve güçlü hale gelir.\n"
            "🌾 **Tarım ve Gıda Krizi** – Kuraklıklar, mahsullerin azalmasına ve açlık riskine yol açabilir.\n"
            "🐧 **Canlı Türlerinin Yok Oluşu** – Kutup ayıları, mercanlar ve birçok tür tehlike altındadır.\n"
            "😷 **Sağlık Sorunları** – Hava kirliliği, sıcak hava dalgaları ve yeni hastalıklar insanları etkileyebilir.\n\n"
            "⚠️ **Uyarı:** Bu etkiler dünya genelinde milyonlarca insanı ve canlıyı ilgilendiriyor!"
        ),
        color=0xc0392b
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/482/482478.png")
    embed.set_image(url="https://geography4u.com/wp-content/uploads/2020/04/Global-warming-poster.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def iklim_nasil_onlenebilir(ctx):
    embed = discord.Embed(
        title="🌱 İklim Değişikliği Nasıl Önlenebilir?",
        description=(
            "**İklim değişikliğini yavaşlatmak elimizde!** İşte alınabilecek bazı önemli önlemler:\n\n"
            "💡 **Enerji Tasarrufu Yap** – Daha az elektrik kullanmak, karbon salımını azaltır.\n"
            "🚲 **Toplu Taşıma veya Bisiklet Kullan** – Arabaların yaydığı gazı azaltır.\n"
            "🌳 **Ağaç Dik ve Doğayı Koru** – Ağaçlar karbondioksiti emer, doğa dengesini sağlar.\n"
            "♻️ **Geri Dönüşüm Yap** – Atıkları ayrıştırarak çevreye zararını azaltabilirsin.\n"
            "🛍️ **Gereksiz Tüketimden Kaçın** – Az ama etkili alışveriş, çevreye dost bir yaşam demek.\n"
            "📢 **Farkındalık Yarat** – Çevrendekilere iklim değişikliğini anlat, birlikte hareket edin!\n\n"
            "🌍 **Unutma:** Küçük değişiklikler büyük farklar yaratır. Gelecek seninle değişebilir!"
        ),
        color=0x27ae60
    )
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/883/883407.png")
    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTknsC9MkdluSLOAygpnKLmaPKsGWBfX8ljDw&s")
    await ctx.send(embed=embed)

@bot.command()
async def iklim_sorulari(ctx, kategori: str = None):
    if kategori is None:
        await ctx.send("❗ Lütfen bir kategori belirtin. Seçenekler: nedir, sebepler, etkiler, onlemler. Ornek: '!iklim_sorulari nedir' ")
        return

    kategori = kategori.lower()
    if kategori not in category_mapping:
        await ctx.send("❗ Geçersiz kategori. Seçenekler: nedir, sebepler, etkiler, onlemler")
        return

    sorular = random.sample(category_mapping[kategori], 5)
    user_data[ctx.author.id] = {"sorular": sorular, "cevaplar": [], "dogrular": 0, "aktif_soru": 0}
    soru = sorular[0]
    secenekler = "\n".join(soru["secenekler"])
    await ctx.send(f"**Soru 1:** {soru['soru']}\n{secenekler}\nCevabınızı yazın (A/B/C/D)")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    user_id = message.author.id
    if user_id in user_data:
        data = user_data[user_id]
        if data["aktif_soru"] < len(data["sorular"]):
            cevap = message.content.strip().upper()
            dogru_cevap = data["sorular"][data["aktif_soru"]]["dogru"]
            if cevap == dogru_cevap:
                data["dogrular"] += 1
                await message.channel.send("✅ Doğru cevap!")
            else:
                await message.channel.send(f"❌ Yanlış! Doğru cevap: {dogru_cevap}")
            data["aktif_soru"] += 1

            if data["aktif_soru"] < len(data["sorular"]):
                soru = data["sorular"][data["aktif_soru"]]
                secenekler = "\n".join(soru["secenekler"])
                await message.channel.send(f"**Soru {data['aktif_soru'] + 1}:** {soru['soru']}\n{secenekler}\nCevabınızı yazın (A/B/C/D)")
            else:
                await message.channel.send(f"🎉 Test tamamlandı! Doğru sayısı: {data['dogrular']}/5")
                del user_data[user_id]

    await bot.process_commands(message)

@bot.command()
async def yardim(ctx):
    embed = discord.Embed(
        title="📜 Komutlar",
        description=(
            "!iklim_nedir\n"
            "!iklim_sebebleri\n"
            "!iklim_ne_yapabilir\n"
            "!iklim_nasil_onlenebilir\n"
            "!iklim_sorulari"
        ),
        color=0x3498db
    )
    await ctx.send(embed=embed)


@bot.command()
async def hakkinda(ctx):
    embed = discord.Embed(
        title="🌍 Project Climate Change (Iklim_degisikliyi) 🌿",
        description=(
            "Iklim degisikliyi hakkinda bilgi veren discord botu. 🌡️🌱\n"
            "Kullaniciyi **\"Iklim Degisikliyi\"** hakkinda bilgilendirmek icin tasarlanan Discord Botu. 🤖📚\n\n"
            "**Botun yararlari:** 🌟\n"
            "- Kullanici belirli komutlari girerek botdan bilgi alacak 📖\n"
            "- Kullaniciyi bilgilendirdikden sonra sorular soracak ❓🧠\n"
            "- Daha fazlasi 🚀\n\n"
            "**Komutlar:**\n"
            "- !iklim_nedir\n"
            "- !iklim_sebebleri\n"
            "- !iklim_ne_yapabilir\n"
            "- !iklim_nasil_onlenebilir\n"
            "- !iklim_sorulari\n"
            "- !yardim\n"
            "- !hakkinda\n\n"
            "**Gerekli Kutuphaneler:** 📦\n"
            "- Pillow 🖼️\n"
            "- discord.py 🤖"
        ),
        color=0x2ecc71
    )
    embed.set_image(url="https://scx2.b-cdn.net/gfx/news/hires/2018/recycle.jpg")
    await ctx.send(embed=embed)


@bot.command()
async def github(ctx):
    embed = discord.Embed(
        title="GitHub Repository",
        description="[Click here to visit the Climate Change Bot GitHub](https://github.com/Omer607/Iklim_degisikliyi)",
        color=0x3498db
    )
    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help - Commands List",
        description="Here are the commands you can use:",
        color=0x00ff00
    )

    embed.add_field(name="!iklim_nedir", value="Learn what climate change is.", inline=False)
    embed.add_field(name="!iklim_sebebleri", value="See the causes of climate change.", inline=False)
    embed.add_field(name="!iklim_ne_yapabilir", value="What can climate change do to our planet.", inline=False)
    embed.add_field(name="!iklim_nasil_onlenebilir", value="How to prevent climate change.", inline=False)
    embed.add_field(name="!iklim_sorulari", value="Test your knowledge with questions.", inline=False)
    embed.add_field(name="!yardim", value="Show the list of commands.", inline=False)
    embed.add_field(name="!hakkinda", value="Learn about this bot.", inline=False)

    await ctx.send(embed=embed)


bot.run('YOUR TOKEN HERE')

