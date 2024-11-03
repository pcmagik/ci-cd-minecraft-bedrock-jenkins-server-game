# CI/CD dla serwera Minecraft w Jenkinsie z wykorzystaniem Dockera! 🚀

Postanowiłem zautomatyzować wdrażanie i testowanie serwera Minecraft Bedrock przy użyciu Jenkins, Dockera oraz kilku sprytnych kroków w Jenkinsfile. Poniżej znajdziecie krótką analizę całego procesu pipeline, który może być przydatny dla każdego, kto chce nauczyć się czegoś nowego w temacie CI/CD i gier!

W Jenkinsfile, pipeline został podzielony na kilka etapów, które ściśle współpracują, by zapewnić sprawne działanie:

1. **Etap Clone Repository** - Na początku klonujemy repozytorium, aby mieć dostęp do najnowszego kodu. Jest to kluczowy krok zapewniający, że wszystkie kolejne etapy będą operować na najnowszej wersji.

2. **Etap Install Python Dependencies** - Instalujemy wymagane zależności Python, w tym menedżera pakietów `pip`, aby móc uruchomić skrypty wspierające pobieranie najnowszej wersji serwera.

3. **Etap Create Python Virtual Environment** - Tworzymy wirtualne środowisko Pythona, w którym instalujemy wszystkie wymagane biblioteki, takie jak `selenium`, `requests`, `webdriver_manager` oraz `beautifulsoup4`. To środowisko służy do uruchamiania skryptu pobierającego najnowszą wersję serwera.

4. **Etap Download Bedrock Server** - Kluczowym elementem jest skrypt w Pythonie, który automatycznie akceptuje warunki użytkowania i pobiera najnowszą wersję serwera Minecraft Bedrock bez potrzeby ręcznej interwencji. Dzięki temu zawsze mamy dostęp do aktualnej wersji serwera.

5. **Etap Build Docker Image** - Pobieramy obraz Dockera dla serwera Minecraft Bedrock, konfigurujemy wszystkie wymagane zależności, a następnie budujemy nasz własny obraz. Jest to fundament całej automatyzacji.

6. **Etap Test Docker Image** - Testujemy obraz Docker, uruchamiając go w środowisku testowym. Sprawdzamy, czy pliki serwera są dostępne i czy środowisko działa poprawnie.

7. **Etap Deploy to Test Environment** - Używamy Dockera do wdrożenia serwera na maszynę testową, przy czym Jenkins uruchamia kontener z odpowiednimi portami. Upewniamy się, że serwer uruchomił się poprawnie poprzez analizę logów.

8. **Etap Automated Tests** - Automatycznie testujemy działanie serwera, sprawdzając, czy porty są prawidłowo nasłuchiwane z zewnętrznej perspektywy. To zapewnia, że serwer jest dostępny dla graczy.

9. **Etap Backup Existing Production** - Przed wdrożeniem na produkcję wykonujemy kopię zapasową obecnego stanu serwera, aby móc łatwo przywrócić dane w razie potrzeby.

10. **Etap Deploy to Production** - Wdrażamy najnowszą wersję serwera na środowisko produkcyjne, zastępując poprzedni kontener. W razie potrzeby przywracamy kopię zapasową świata.

11. **Etap Monitor Production Server** - Monitorujemy produkcyjny serwer, upewniając się, że jest on dostępny z zewnętrznej perspektywy i że porty są prawidłowo nasłuchiwane.

Cały pipeline jest zaprojektowany tak, żeby działał zarówno na lokalnym serwerze, jak i w Oracle Cloud, co czyni go uniwersalnym rozwiązaniem dla wielu środowisk. Kluczową rolę odgrywa Docker, który zapewnia przenośność oraz powtarzalność środowiska.

Chcesz zobaczyć jak to wszystko działa? Zapraszam do mojego repozytorium na GitHub:
https://github.com/pcmagik/ci-cd-minecraft-bedrock-jenkins-server-game

To dopiero początek przygody z CI/CD dla gier! 🎮

#devops #jenkins #docker #cicd #minecraft #automation #oraclecloud