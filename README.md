
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INSTITUTE KUEN SIU KUEN WING SHUN KUNG FU</title>
    <style>
        body {
            background-color: #FFD700; /* Amarelo */
            color: black;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            text-align: center;
            padding: 20px;
            background-color: #FF0000; /* Vermelho */
            color: white;
        }
        nav {
            text-align: center;
            margin: 20px 0;
        }
        nav button {
            background-color: #FF0000;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
        }
        nav button:hover {
            background-color: #cc0000;
        }
        section {
            padding: 20px;
            text-align: center;
        }
        .map-container {
            width: 100%;
            height: 400px;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        footer {
            text-align: center;
            padding: 20px;
            background-color: #FF0000;
            color: white;
        }
        .social-icons a {
            margin: 0 10px;
            color: white;
            text-decoration: none;
            font-size: 20px;
        }
        .chat-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25D366;
            color: white;
            padding: 15px;
            border-radius: 50%;
            text-decoration: none;
            font-size: 25px;
        }
        form input, form button {
            padding: 10px;
            margin: 5px;
            border: 1px solid #000;
            border-radius: 5px;
        }
        form button {
            background-color: #FF0000;
            color: white;
            cursor: pointer;
        }
        .artes {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .arte {
            margin: 20px;
            width: 250px;
        }
        .arte img {
            width: 100%;
            border: 2px solid black;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>INSTITUTE KUEN SIU KUEN WING SHUN KUNG FU</h1>
        <div id="google_translate_element"></div>
    </header>

    <nav>
        <button onclick="scrollToSection('anuncio')">Anúncio e Preços</button>
        <button onclick="scrollToSection('localizacao')">Localização</button>
        <button onclick="scrollToSection('contato')">Contato</button>
    </nav>

    <section id="anuncio">
        <h2>Treine com os Melhores Mestres</h2>
        <p><strong>Mensalidade:</strong> R$200,00 — 3 aulas por semana</p>
        <div class="artes">
            <div class="arte">
                <h3>Wing Shun Kung Fu</h3>
                <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Wing_Chun_Silhouette.png" alt="Wing Shun">
            </div>
            <div class="arte">
                <h3>Muay Thai Feminino</h3>
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/36/Muay_Thai_fighter_silhouette.png" alt="Muay Thai">
            </div>
            <div class="arte">
                <h3>Tai Chi Terapêutico</h3>
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Tai_Chi_Silhouette.png" alt="Tai Chi">
            </div>
        </div>
    </section>

    <section id="localizacao">
        <h2>Encontre-nos</h2>
        <div class="map-container">
            <!-- Substitua o link abaixo pelo mapa da sua academia -->
            <iframe src="https://www.google.com/maps/>
        </div>
    </section>

    <section id="contato">
        <h2>Cadastre-se para receber novidades</h2>
        <form>
            <input type="email" placeholder="Seu e-mail" required>
            <button type="submit">Cadastrar</button>
        </form>

        <h3>Siga-nos nas redes sociais</h3>
        <div class="social-icons">
            <a href="https://wa.me/+558898313939" target="_blank">WhatsApp</a> |
            <a href="https://www.instagram.com/institutokuensiukuen?igsh=eXozNGIwZHRnM2Ft" target="_blank">Instagram</a> |
            <a href="https://facebook.com" target="_blank">Facebook</a> |
            <a href="https://kwai.com" target="_blank">Kwai</a> |
            <a href="https://tiktok.com" target="_blank">TikTok</a> |
            <a href="https://twitter.com" target="_blank">Twitter</a> |
            <a href="https://telegram.me" target="_blank">Telegram</a>
        </div>
    </section>

    <a class="chat-button" href="https://wa.me/seu_numero" target="_blank">💬</a>

    <footer>
        <p>© 2025 Institute Kuen Siu Kuen Wing Shun Kung Fu — Todos os direitos reservados</p>
    </footer>

    <!-- Google Translate -->
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({pageLanguage: 'pt'}, 'google_translate_element');
        }
        function scrollToSection(id) {
            document.getElementById(id).scrollIntoView({behavior: 'smooth'});
        }
    </script>
    <script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</body>
</html>
