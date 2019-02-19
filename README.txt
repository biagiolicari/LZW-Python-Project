Per installare la seguente applicazione sulla macchina, assicurarsi di aver già installato una versione di Python uguale o maggiore alla 3.6.0 e di aver installato python3-pip.
In caso contrario installare pip3 tramite il comando seguente :
	sudo apt-get install python3-pip



Per eseguire l'applicazione seguire la seguente procedura :

1) Estrarre il contenuto di Lzw_Compressor
2) Posizionarsi all'interno della dir appena decompressa
3) Eseguire il seguente comando che permettera di installare i requisiti utili all'applicazione, ove non fossero presenti
	pip3 install -r requirements.txt
4) Una volta installati i requisiti, dare il seguente comando per installare l'applicazione
	sudo python3 setup.py install

Una volta installato sarà possibile visualizzare un help di linea digitando Compress/Uncompress -h, mostrando così le opzioni possibili.

Esempio Comando : Compress -rvt path/dir/prova  Tale comando permettera di comprimere in maniera ricorsiva(-r), in modalità verbose(-v) e tramite la st_dati Trie(-t) i file presenti all'interno della directory prova.



NB) Per testare l'applicazione in un ambiente virtuale è possibile dare i seguenti comandi da terminale :

1) Estrarre la dir Lzw_Compress e entrarvi dentro
2) Eseguire il comando :
	virtualenv -p python3 path/lzw
3) Attivare l'ambiente virtuale tramite :
	source bin/activate
4) Installare i requisiti utili ad Lzw_Compressor tramite :
	pip3 install -r requirements.txt
5) Installare l'applicazione tramite :
	sudo python3 setup.py install
	 
