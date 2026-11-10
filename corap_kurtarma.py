#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorap Arama-Kurtarma Ekibi (KÇAKE)
Dünyanın en ciddi çorap kurtarma yazılımı.
"""

import random
import time

def corap_kayip_nedeni():
    nedenler = [
        "Çamaşır makinesi onu yedi ve sindirdi",
        "Kedi çorabı özel koleksiyonuna ekledi",
        "Komşu gizlice çorabını çaldı ve giydi",
        "Paralel evrende daha mutlu bir hayat sürüyor",
        "Çorap, özgürlüğüne kavuşmak için kaçtı",
        "Kanepenin altında karadelik oluştu",
        "Çamaşır sepeti onu rehin aldı",
        "Evdeki diğer çoraplar onu sürgün etti",
        "Uzaylılar çorap koleksiyonu yapıyor",
        "Çorap, vergi kaçırmak için yurtdışına kaçtı"  # Gizli siyasi: vergi kaçakçılığı ima
    ]
    return random.choice(nedenler)

def muhtemel_konum():
    konumlar = [
        "Kanepenin 4. boyutu",
        "Çamaşır makinesinin gizli bölmesi",
        "Komşunun çekmecesinde",
        "Evrenin başka bir köşesinde",
        "Kedinizin midesinde (henüz sindirilmemiş)",
        "Çorapların gizli üsünde",
        "Sizin göremediğiniz bir yerde (hemen yanınızda)",
        "Bürokrasi bürosunda kayıp eşya defterinde"
    ]
    return random.choice(konumlar)

def kurtarma_adimlari():
    adimlar = [
        "1. Derin nefes alın ve çorabın adını üç kez fısıldayın",
        "2. Evi 47 kez arayın (sayı önemli)",
        "3. Kediye rüşvet olarak balık verin",
        "4. Çamaşır makinesine resmi yazı yazın",
        "5. Paralel evrene portal açmayı deneyin (başarısız olacak)",
        "6. Yeni çorap alın ve eskisini unutun"
    ]
    return adimlar

def main():
    print("=" * 50)
    print("  KAYIP ÇORAP ARAMA-KURTARMA EKİBİ  ")
    print("     Resmi Operasyon Başlatıldı")
    print("=" * 50)
    print()
    
    time.sleep(1)
    print("🔍 Çorap tarama sistemi aktif...")
    time.sleep(1.5)
    
    neden = corap_kayip_nedeni()
    konum = muhtemel_konum()
    
    print(f"\n📊 RAPOR:")
    print(f"Kayıp Nedeni: {neden}")
    print(f"Muhtemel Konum: {konum}")
    print()
    
    print("🛡️  Kurtarma Protokolü:")
    for adim in kurtarma_adimlari():
        print(f"  {adim}")
        time.sleep(0.5)
    
    print()
    print("⚠️  Operasyon tamamlandı. Çorabınız bulunamadı ama en azından denedik.")
    print("   Yeni çorap almanız önerilir.")
    print()
    print("👞 KÇAKE - Çoraplar için savaşıyoruz (ama kazanmıyoruz) 👞")

if __name__ == "__main__":
    main()
