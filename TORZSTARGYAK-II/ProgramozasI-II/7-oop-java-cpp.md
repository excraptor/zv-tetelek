# 7. Objektum orientált paradigma és annak megvalósítása a JAVA és C++ nyelvekben. Az absztrakt adattípus, az osztály. Az egységbe zárás, az információ elrejtés, az öröklődés, az újrafelhasználás és a polimorfizmus. A polimorfizmus feloldásának módszere


## Objektumorientált paradigma és annak megvalósítása a JAVA és C++ nyelvekben

Az objektumorientált paradigma alapelvei:

- egységbe zárás
- információ elrejtés
- öröklődés

Objektum orientált nyelvekben létrehozhatunk osztályokat és objektumokat. Egy osztály egy valamilyen valós tárgynak a programozási nyelvre való leképezése. A különböző valós dolgoknak vannak tulajdonságai, és képesek valamilyen akciók végrehajtására. Az objektumorientált programozási nyelvek lényege, hogy ezt a fajta viselkedést tudjuk vele modellezni. Egy osztály egy ilyen valós fogalomnak a megfogalmazása.

### Megvalósítás JAVA nyelven

class Weapon {
    private String name;
    private int damage;

    public Weapon (String name, int damage) {
        this.name = name;
        this.damage = damage;
    }

    public int shoot() {
        return this.damage;
    }

}

class Rifle extends Weapon {
    
    @Override
    public int shoot(int bullets) {
        return this.damage * bullets;
    }
}

## Az absztrakt adattípus, az osztály

Egy osztályt akkor nevezünk absztraktnak, ha van olyan metódusa, amely nincs 