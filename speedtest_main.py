from speedtest_arayuz import Ui_Form
import pyspeedtest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread


#----------------------------------------------------------------------------------

class ArkaPlan(QThread): # Arkaplan'da bu kodlar çalışacak.

    def __init__(self, parent):
        QThread.__init__(self)
        self.parent = parent

    def sonuclari_sifirla(self):
        self.parent.sonuc_yazi_1.setText("0")
        self.parent.sonuc_yazi_2.setText("0")
        self.parent.sonuc_yazi_3.setText("0")


    def run(self):
        self.parent.listWidget.clear()
        self.parent.hizihesapla.setEnabled(False)
        self.parent.listWidget.insertItem(0,"Test yapılıyor, lütfen bekleyiniz.")
        self.sonuclari_sifirla()

        self.st = pyspeedtest.SpeedTest() # Programa işlevsellik kazandıran kodlar.
        self.downloadbilgisi = pyspeedtest.pretty_speed(self.st.download()) #Download hızı hesaplanıyor.
        self.uploadbilgisi = pyspeedtest.pretty_speed(self.st.upload()) # Upload hızı hesaplanıyor.
        self.pingbilgisi = pyspeedtest.pretty_speed(self.st.ping()) # Ping hesaplanıyor.

        self.item = ["Download: " + self.downloadbilgisi, "Upload: " + self.uploadbilgisi,
                     "Ping: " + self.pingbilgisi]

        self.parent.sonuc_yazi_1.setText(self.downloadbilgisi)
        self.parent.sonuc_yazi_2.setText(self.uploadbilgisi)
        self.parent.sonuc_yazi_3.setText(self.pingbilgisi)
        self.parent.listWidget.clear()
        self.parent.listWidget.insertItems(0, self.item)
        self.parent.hizihesapla.setEnabled(True)


class Uygulama(QWidget,Ui_Form):

    def __init__(self):
        super(Uygulama,self).__init__()
        self.setupUi(self)
        self.hizihesapla.clicked.connect(self.hesapla)
        self.bilinmesi_gerekenler.clicked.connect(self.yenipencere)

    def hesapla(self):
        self.thread = ArkaPlan(self)
        self.thread.start()

    def yenipencere(self): # 'Bilinmesi Gerekenler' butonunu çalıştıran kodlar.
        self.new = QWidget()
        self.new.resize(790,490)
        self.new.setMaximumSize(790,490)
        self.new.setMinimumSize(790,490)
        self.new.setWindowTitle("Bilinmesi Gerekenler")
        self.new.setWindowIcon(QIcon("C:/Users/AYTEN/Desktop/speedtest/speed.ico"))

        self.layout = QGridLayout(self.new)

        self.kavramların_anlamları = QLabel(self.new)
        self.kavramların_anlamları.setText("<p style='color:red'>Kavramların anlamları</p>")

        self.mbps_nedir = QLabel(self.new)
        self.mbps_nedir.setText("Mbps: (Megabit Per Second) 1 saniyede kaç megabit veri aktarıldığını ifade eder.")

        self.kbps_nedir = QLabel(self.new)
        self.kbps_nedir.setText("Kbps: (Kilobit Per Second) 1 saniyede gerçekleştirilen kilobit değerinden veri aktarımıdır.")

        self.bps_nedir = QLabel(self.new)
        self.bps_nedir.setText("Bps: (Bit Per Second) İletişim jargonunda saniyede bir bit anlamına gelen birimdir.")

        self.download_nedir = QLabel(self.new)
        self.download_nedir.setText("Download: İnternet ağında yer alan bir sunucudan bilgisayarımıza veri transfer edilmesidir.")

        self.upload_nedir = QLabel(self.new)
        self.upload_nedir.setText("Upload: Bilgisayarımızdan başka bir sisteme her türlü verinin aktarımına denir.")

        self.ping_nedir = QLabel(self.new)
        self.ping_nedir.setText("Ping: Bilgisayarımızla karşıdaki sunucu arasında bir veri paketinin iletilmesi esnasında geçen süredir.")

        self.uyari = QLabel(self.new)
        self.uyari.setText("<p style='color:red'>Doğru sonuç alabilmek için</p>")

        self.uyari1 = QLabel(self.new)
        self.uyari1.setText("1- Kullandığınız ağ başka cihazlarda da kayıtlıysa diğer cihazlardaki bağlantıyı kesiniz.")

        self.uyari2 = QLabel(self.new)
        self.uyari2.setText("2- Kotanızın sınırı dolmuşsa program sağlıklı bir ölçüm yapamayabilir.")

        self.uyari3 = QLabel(self.new)
        self.uyari3.setText("3- Programın çalıştığı esnada ağ üzerinden -download vb.- işlem yapıyorsanız ölçüm sağlıklı olmayacaktır.")

        def cikis():
            self.new.destroy()

        self.onaybuton = QPushButton(self.new)
        self.onaybuton.setText("Tamam")
        self.onaybuton.clicked.connect(cikis)


        self.layout.addWidget(self.kavramların_anlamları,0,0,1,1)
        self.layout.addWidget(self.mbps_nedir,1,0,1,1)
        self.layout.addWidget(self.kbps_nedir,2,0,1,1)
        self.layout.addWidget(self.bps_nedir,3,0,1,1)
        self.layout.addWidget(self.download_nedir,4,0,1,1)
        self.layout.addWidget(self.upload_nedir,5,0,1,1)
        self.layout.addWidget(self.ping_nedir,6,0,1,1)
        self.layout.addWidget(self.uyari,7,0,1,1)
        self.layout.addWidget(self.uyari1,8,0,1,1)
        self.layout.addWidget(self.uyari2,9,0,1,1)
        self.layout.addWidget(self.uyari3,10,0,1,1)
        self.layout.addWidget(self.onaybuton,11,0,2,2)


        self.new.show()



app = QApplication([])
pencere = Uygulama()
pencere.show()
app.exec_()