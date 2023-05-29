import os

# Répertoire de départ
repertoire = './docs/chat/'

def get_directories(directory):
    directories = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            directories.append(entry.name)
    directories.sort(key=lambda x: x.lower())  # Sort directories in lowercase
    return directories



CodeHTML = '''
   <!DOCTYPE html>
            <!--
            ██████╗  █████╗ ███╗   ██╗███████╗ ██████╗ ███╗   ███╗██╗    ██╗ █████╗ ██████╗ ███████╗   ██╗     ██╗██╗   ██╗███████╗
            ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗████╗ ████║██║    ██║██╔══██╗██╔══██╗██╔════╝   ██║     ██║██║   ██║██╔════╝
            ██████╔╝███████║██╔██╗ ██║███████╗██║   ██║██╔████╔██║██║ █╗ ██║███████║██████╔╝█████╗     ██║     ██║██║   ██║█████╗  
            ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║   ██║██║╚██╔╝██║██║███╗██║██╔══██║██╔══██╗██╔══╝     ██║     ██║╚██╗ ██╔╝██╔══╝  
            ██║  ██║██║  ██║██║ ╚████║███████║╚██████╔╝██║ ╚═╝ ██║╚███╔███╔╝██║  ██║██║  ██║███████╗██╗███████╗██║ ╚████╔╝ ███████╗
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝  ╚══════╝
            version 2023-04 
            by Julien Mousqueton https://julien.io 
            -->
            <html lang="en">
            <head>
            <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Ransomware.live : Ransomware Groups Negotiations">
  <meta name="keywords" content="ransomware, breach, leak, post, gang, data, cybersecurity, victims, ransom, julien, mousqueton, julien mousqueton, CyberSoc, CTI, negotiation, ransom">
  <!-- Open Graph / Facebook -->
   <meta property="og:type" content="website">
   <meta property="og:url" content="https://chat.ransomware.live">
   <meta property="og:title" content="Ransomware.live 👀">
   <meta property="og:description" content="Ransomware.live : Ransomware Groups Negotiations">
   <meta property="og:image" content="https://chat.ransomware.live/ransomware.png">
  <!-- Twitter -->
   <meta property="twitter:card" content="summary_large_image">
   <meta property="twitter:url" content="https://chat.ransomware.live/">
   <meta property="twitter:title" content="Ransomware.live 👀">
   <meta property="twitter:description" content="Ransomware.live : Ransomware Groups Negotiations">
   <meta property="twitter:image" content="https://chat.ransomware.live/ransomware.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <link rel="canonical" href="https://chat.ransomware.live">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">


  <title>Ransomware.live - Ransomware Gang Negotiations</title>
  <link href='https://fonts.googleapis.com/css?family=Fjalla+One' rel='stylesheet' type='text/css'>
<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
<link rel="stylesheet" href="index.css">
<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Secular+One&amp;display=swap'><link rel="stylesheet" href="./style.css">
<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="https://stats.mousqueton.io/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '15']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Matomo Code -->
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
		<h1>Ransomware Gang Negotiations&nbsp;</h1><h2>&nbsp;by <a href="https://www.ransomware.live" targer=_blank>Ransomware.live</a></h2>
<!-- partial:index.partial.html -->
<div class="content">
	<ul class="nego">

'''
directories = get_directories(repertoire)

for directory in directories:
        chemin_separe = directory.split(os.sep)
        ransomware_gang = chemin_separe[-1]
        try: 
            file_path = "./description/"+ransomware_gang+".txt" 

            with open(file_path.lower(), "r") as description:
                desc = description.read()
        except:
                desc=''
        if len(ransomware_gang) > 2:
            profile_gang = ransomware_gang
            if ransomware_gang == 'lockbit3.0':
                profile_gang = 'lockbit3' 
            CodeHTML += f'''
            <li class="gang">
			<div class="thumb"><img src="/gang.png"></div>
			<div class="description">
				<h3>{ransomware_gang}</h3>
                <p>{desc}<br><a href="https://www.ransomware.live/#/profiles?id={profile_gang}">{ransomware_gang}</a></p>
			</div>
		</li>

            '''


CodeHTML += '''
	</ul>

</div>

<h2>
	Source: <a href="https://github.com/Casualtek/Ransomchats" target=_blank>Casualtek/Ransomchats</a> by Valéry Marchive<BR></BR>
    Code Source: <a href="https://github.com/JMousqueton/chat.ransomware.live" target=_blank><i class="fab fa-github"></i></a>
</h2>
</body>
</html>
'''

print(CodeHTML)
