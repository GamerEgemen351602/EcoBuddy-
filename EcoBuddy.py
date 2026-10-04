print("===================================")
print("        🌱 EcoBuddy 🌱")
print("   Karbon Ayak İzi Hesaplayıcı")
print("===================================")

print("\nGünlük alışkanlıklarını gir!")

# Ulaşım
araba = float(input("\n🚗 Bugün arabayla kaç km gittin? "))

# Elektrik
elektrik = float(input("💡 Bugün yaklaşık kaç saat elektrik kullandın? "))

# Et tüketimi
et = float(input("🥩 Bugün kaç porsiyon et yedin? "))

# Plastik
plastik = int(input("🧴 Bugün kaç plastik ürün kullandın? "))

# Basit karbon hesaplama
araba_co2 = araba * 0.21
elektrik_co2 = elektrik * 0.4
et_co2 = et * 2.5
plastik_co2 = plastik * 0.05

toplam = araba_co2 + elektrik_co2 + et_co2 + plastik_co2

print("\n===================================")
print("          🌍 SONUÇLAR")
print("===================================")

print(f"🚗 Ulaşım: {araba_co2:.2f} kg CO₂")
print(f"💡 Elektrik: {elektrik_co2:.2f} kg CO₂")
print(f"🥩 Beslenme: {et_co2:.2f} kg CO₂")
print(f"🧴 Plastik: {plastik_co2:.2f} kg CO₂")

print("-----------------------------------")
print(f"🌍 Toplam: {toplam:.2f} kg CO₂")

# Öneri sistemi
print("\n🌱 EcoBuddy'nin önerisi:")

if toplam < 5:
    print("Harika! 🌿 Karbon ayak izin düşük.")
    print("Bu alışkanlıklarını korumaya devam et!")
elif toplam < 10:
    print("İyi gidiyorsun! 🌱")
    print("Kısa mesafelerde yürümeyi veya bisikleti deneyebilirsin.")
else:
    print("Karbon ayak izin biraz yüksek. 🌍")
    print("Toplu taşıma kullanmayı ve gereksiz elektrik tüketimini azaltmayı deneyebilirsin.")

print("\n🌎 Küçük değişiklikler büyük fark yaratabilir!")