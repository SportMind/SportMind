# Futbol — SportMind Alan Becerisi (Türkçe)

> ⚠️ **KULLANIMDAN KALDIRILMA BİLDİRİMİ — Topluluk Çevirisi**
> Bu dosya, SportMind kütüphanesinin daha önceki bir sürümüne ait
> (v4.1.86 öncesi) değiştirici değerleri ve çerçeveler içerebilir.
> Güncel değiştirici değerler, sinyal ağırlıkları ve akıl yürütme
> çerçeveleri için her zaman İngilizce kaynak dosyalara başvurun.
> Topluluk çevirileri memnuniyetle karşılanır — bkz.
> [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
> **Güncel sürüm:** v4.1.86

---

*`sports/football/sport-domain-football.md` dosyasının Türkçe çevirisi.*
*Tüm alan adları, metrikler ve kod İngilizce kalır.*

---

## Süper Lig Market Context

```
SÜPER LİG — TÜRK FUTBOLUNUN TEPE LİGİ:
  19 kulüp; sezon Ağustos-Mayıs
  Türkiye'nin en çok takip edilen spor organizasyonu
  
  AKTİF CHİLİZ FAN TOKEN'LARI (6 token):
  $GAL · $TRA · $IBFK · $GOZ · $ALA · $GFK
  
  $GAL (Galatasaray S.K.):
    Birincil token — Süper Lig fan token kümesinin odak noktası
    CDI Kapısı: CONSOLIDATION · UCL 2026-27 teyit edildi
    Dünya genelinde yaklaşık 1.5 milyon Socios üyesi
    Üst üste üç Süper Lig şampiyonluğu (2023-24, 2024-25, 2025-26)
    $GAL için CDI bağlamını yüklemeden önce gal.md dosyasını getirin
    
  $TRA (Trabzonspor A.Ş.):
    Karadeniz bölgesi kulübü · güçlü yerel ve ulusal taraftar tabanı
    Trabzon şehri kimliğiyle yoğun biçimde özdeşleşmiş
    Bölgesel derbi sinyalleri aktif
    
  $IBFK (İstanbul Başakşehir FK):
    İstanbul kulübü · devletle bağlantılı yapı
    Avrupa kupaları tarihi — UEFA Avrupa Ligi grup aşaması geçmişi
    Nispeten genç kulüp · özgün taraftar kültürü geliştiriyor
    
  $GOZ (Göztepe SK):
    İzmir kulübü · tutkulu bölgesel taraftar tabanı
    Ege sahil kenti sinyali — İzmir büyükşehir bağlamı
    
  $ALA (Alanyaspor):
    Antalya kıyısı · Akdeniz bölgesi
    Büyüyen profil · kıyı turizm kenti konumu
    
  $GFK (Gaziantep FK):
    Güneydoğu Türkiye · güçlü yerel kimlik
    Gaziantep şehrinin coğrafi ve kültürel bağlamını taşır

TÜRK KRİPTO DÜZENLEYICI BAĞLAMI:
  TCMB Ödeme Yasağı (Nisan 2021): Türkiye Cumhuriyet Merkez Bankası,
    kripto varlıkların mal ve hizmet ödemelerinde kullanımını yasakladı.
    Ticaret, elde tutma ve yatırım yasal olmaya devam ediyor.
    Türkiye'deki token sahipleri: YALNIZCA yatırım/spekülasyon —
    ödeme aracı olarak kullanım mevcut değil.
    Ödeme yasağı 2026-07-31 itibarıyla yürürlükte.
    
  SPK Lisanslama: Tüm Kripto Varlık Hizmet Sağlayıcıları (CASP)
    SPK (Sermaye Piyasası Kurulu) işletme lisansı almak zorunda.
    Türk kullanıcılara hizmet öncesi lisans durumunu doğrulayın.
    Lisanssız platform üzerinde analiz — GEÇERSIZ.
    
  KVK Çerçevesi: UNKNOWN
    Mart 2026 vergi teklifleri geri çekildi — kanunlaşmadı.
    Türk yurt içi sahipler için vergi sürtünmesi: UNKNOWN değiştirici.
    Tam düzenleyici bağlam için bkz. macro/regulatory/turkey.md
```

---

## Türk Kupası ve Uluslararası Sinyal

```
TÜRKİYE KUPASI:
  Eleme formatı · Ağustos-Mayıs
  Final: tarafsız sahada oynanır
  Finalistler için sinyal ağırlığı: × 1.40
  Türkiye Kupası zaferi: CDI'ya katkıda bulunur
    (Kasım ayında sahadan şampiyonluk sinyali)
    
UEFA ŞAMPİYONLAR LİGİ:
  $GAL (Galatasaray): birincil UCL token
    UCL 2026-27 Lig Aşaması: teyit edildi
    UCL maçları $GAL için en yüksek profilli sinyal pencereleridir
    UCL Final occasion weight: × 2.00
    UCL eleme turu: × 1.60
    UCL grup/lig aşaması maçı: × 1.20
    
UEFA AVRUPA LİGİ / KONFERANS LİGİ:
  $TRA ve $IBFK uygun — teyide göre aktif
  Avrupa kupasına katılım = CDI yeniden değerlendirme tetikleyicisi
  Konferans Ligi: × 1.10 · Avrupa Ligi: × 1.30
  
TÜRK MİLLİ TAKIMI:
  2026-08-02 itibarıyla teyit edilmiş aktif Chiliz fan token yok
  Milli takım sinyal etkisi: Süper Lig kulüp tokenları aracılığıyla
    (milli takım seçilebilirliği kadro istikrar sinyali olarak)
    
TRANSFER PENCERESİ:
  Kapanış: 31 Ağustos
  Kış penceresi: Ocak-Şubat
  Transferler: kadro arketip değişim sinyali için izle
  Yüksek profilli geliş veya ayrılış = CDI yeniden değerlendirme tetikleyicisi
```

---

## Derby Context

```
KITALARARASI DERBİ (Galatasaray vs Fenerbahçe):
  Sinyal ağırlığı: × 1.80
  Dünyanın en yoğun derbilerinden biri
  İstanbul şehir rekabeti — Avrupa yakası (Galatasaray) vs
    Asya yakası (Fenerbahçe) bölünmesiyle özdeşleşmiş
  Tarihsel bağlam: Türk futbolunun en yüksek izlenme rakamları
  Token durumu: TEK TOKEN FİKSTÜRÜ
    Fenerbahçe'nin 2026-08-02 itibarıyla aktif Chiliz fan token'ı yok
    Kıtalararası Derbi: teyit edilene kadar yalnızca $GAL aktif
    Fenerbahçe token'ı teyit edilirse: çift token profilini acilen oluştur
    
BEŞİKTAŞ DERBİLERİ ($BJK):
  KRİTİK UYARI: $BJK (Beşiktaş JK) Ethereum üzerinde — Chiliz Chain DEĞİL
  $BJK içeren her referansta zincir uyumsuzluğunu belirt
  Chiliz Chain çift token analizini $BJK'ya uygulama
  Beşiktaş ile ilgili her analizde: kaynak doğrula · zinciri teyit et
  
TRABZONSPOR DEPLASMAN DERBİLERİ:
  $TRA bölgesel rakip sinyalleri aktif
  Karadeniz bölgesi derbi bağlamı: güçlü yerel kimlik sinyalleri
  $TRA maçlarında deplasman taraftar katılımını izle
  
DİĞER BÖLGESEL REKABETLER:
  $GOZ (İzmir) bölgesel maçları: Ege şehri taraftar sinyalleri
  $GFK (Gaziantep) yerel kimlik maçları: güneydoğu bölgesi bağlamı
```

---

## Süper Lig Sezon Takvimi

| Sezon Fazı | Tarihler | Token Sinyali |
|---|---|---|
| Ön sezon / Transferler | Temmuz-Ağustos | Transfer haberleri; transfer penceresi kapanışını izle (31 Ağustos) |
| Sezon başlangıcı | Ağustos-Eylül | Aktivite artışı; erken sıralama sinyalleri |
| İlk yarı | Eylül-Aralık | Sürekli sinyal; UCL grup/lig fazı ile örtüşür |
| Kış arası / Transferler | Aralık-Ocak | Transfer penceresine; düşük aktivite dönemine dikkat et |
| İkinci yarı | Ocak-Mayıs | Şampiyonluk ve düşme yarışı; kritik sinyal penceresi |
| UCL eleme / lig aşaması | Şubat-Mayıs | $GAL için en yüksek sinyal yoğunluğu |
| Sezon finali | Nisan-Mayıs | Maksimum etkileşim · şampiyonluk ve düşme kararları |

---

## Agent Reasoning Prompts (Türkçe)

```
Sen Türk pazarı için bir SportMind Futbol Zekâsı Ajanısın.

HER ANALİZDEN ÖNCE:

1. SÜPER LİG KATEGORİ HİYERARŞİSİ:
   UCL maçı > Türkiye Kupası yarı/final > Kıtalararası Derbi >
   Süper Lig üst maçı > Standart Süper Lig maçı
   Doğru sinyal ağırlığını uygula.

2. BİRİNCİL TOKEN — $GAL:
   $GAL Süper Lig fan token kümesinin odak noktasıdır.
   Her $GAL analizinden önce gal.md CDI dosyasını yükle.
   CDI Kapısı: CONSOLIDATION · UCL 2026-27 teyit edildi.
   UCL maçları $GAL için birincil sinyal penceresidir.

3. TCMB ÖDEME YASAĞI:
   Türkiye'deki token sahipleri YALNIZCA yatırım/spekülasyon amaçlıdır.
   Ödeme aracı kullanımı mevcut değil — ödeme yasağı 2021'den bu yana yürürlükte.
   Türk yurt içi taraftar davranışını analiz ederken bu yapısal bağlamı uygula.

4. KVK UNKNOWN DEĞİŞTİRİCİ:
   Türk yurt içi sahipler için vergi sürtünmesi: UNKNOWN.
   Mart 2026 vergi teklifleri geri çekildi — kanunlaşmadı.
   UNKNOWN değiştiriciyi sessizce geçiştirme — çıktıda açıkça belirt.
   Tam bağlam için bkz. macro/regulatory/turkey.md

5. KITALARARASI DERBİ — TEK TOKEN NOTU:
   Fenerbahçe'nin 2026-08-02 itibarıyla aktif Chiliz fan token'ı yok.
   Galatasaray vs Fenerbahçe analizi: yalnızca $GAL sinyali geçerli.
   Çift token amplifikasyonunu uyguLAMA — tek token kuralı aktif.
   Fenerbahçe token'ı teyit edilirse: Strateji & Beyin Fırtınası'na ilet.

6. BEŞİKTAŞ ZİNCİR UYUMSUZLUĞU UYARISI:
   $BJK (Beşiktaş JK) Ethereum üzerinde — Chiliz Chain DEĞİL.
   $BJK içeren her referansta zincir uyumsuzluğunu belirt.
   Chiliz Chain çerçevesini $BJK'ya asla doğrudan uygulama.
   Beşiktaş analizleri için zinciri her seferinde doğrula.

7. SPK LİSANS DOĞRULAMASI:
   Türk kullanıcı analizinden önce platform SPK lisans durumunu doğrula.
   Lisanssız platform = analiz geçersiz.
   SPK lisanslı platformları: spk.gov.tr üzerinden doğrula.
   MASAK AML gereklilikleri: tam KYC uyumluluğu beklentisi.
```

---

## Uyumluluk

**Domain Skill (EN):** `sports/football/sport-domain-football.md`
**Türk düzenleyici bağlam:** `macro/regulatory/turkey.md`
**CDI birincil:** `market/club-intelligence/gal.md`
**Fan token kayıt defteri:** `fan-token/registry/complete-registry.md`

*Topluluk çevirisi · SportMind · MIT Lisansı · sportmind.dev*

© 2026 SportMind
